from pyramid.view import view_config
from ..forms.user import SettingsForm

@view_config(route_name='settings', renderer='templates/settings.jinja2', request_method='GET', permission='edit')
def settings_view_get(request):
    form = SettingsForm()
    return {'form': form}

@view_config(route_name='settings', renderer='templates/settings.jinja2', request_method='POST', permission='edit')
def settings_view_post(request):
    import bcrypt
    import transaction
    from pyramid.httpexceptions import HTTPFound
    from pyramid_sqlalchemy import Session
    from ..models.user import UserModel

    form = SettingsForm(request.POST)
    if form.validate():
        # 因為 raise exception 會造成 transaction 中斷，所以這邊手動處理
        user = Session.query(UserModel).filter_by(name=request.user).one()
        if bcrypt.hashpw(form.old_password.data.encode('utf-8'), user.password.encode('utf-8')) == user.password.encode('utf-8'):
          with transaction.manager:
            user.password = bcrypt.hashpw(form.new_password.data.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user.email = form.email.data
            Session.add(user)
          raise HTTPFound(location=request.route_path('home'))
        else:
          request.session.flash('舊密碼不對', 'error')
          return {'form': form}
    else:
        return {'form': form}
