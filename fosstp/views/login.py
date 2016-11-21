from pyramid.view import view_config
from ..forms.user import LoginForm

@view_config(route_name='login', renderer='templates/login.jinja2', request_method='GET')
def login_view_get(request):
    form = LoginForm()
    return {'form': form}

@view_config(route_name='login', renderer='templates/login.jinja2', request_method='POST')
def login_view_post(request):
    import bcrypt
    from pyramid.httpexceptions import HTTPFound
    from pyramid.security import remember
    from pyramid_sqlalchemy import Session
    from ..models.user import UserModel

    form = LoginForm(request.POST)
    if form.validate():
        user = Session.query(UserModel).filter_by(name=form.name.data).one_or_none()
        if user and bcrypt.hashpw(form.password.data.encode('utf-8'), user.password.encode('utf-8')) == user.password.encode('utf-8'):
            headers = remember(request, form.name.data)
            raise HTTPFound(location=request.route_path('news'), headers=headers)
        else:
            request.session.flash('帳號或密碼錯誤', 'error')
            return {'form': form}
    else:
        return {'form': form}