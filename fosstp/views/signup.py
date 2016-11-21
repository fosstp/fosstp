from pyramid.view import view_config
from ..forms import SignupForm

@view_config(route_name='signup', renderer='templates/signup.jinja2', request_method='GET')
def signup_view_get(request):
    form = SignupForm()
    return {'form': form}

@view_config(route_name='signup', renderer='templates/signup.jinja2', request_method='POST')
def signup_view_post(request):
    import bcrypt
    import transaction
    from pyramid.httpexceptions import HTTPFound
    from pyramid_sqlalchemy import Session
    from ..models import UserModel

    form = SignupForm(request.POST)
    if form.validate():
        # 因為 raise exception 會造成 transaction 中斷，所以這邊手動處理
        with transaction.manager:
          user = UserModel()
          form.populate_obj(user)
          user.password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
          Session.add(user)
        raise HTTPFound(location=request.route_path('news'))
    else:
        return {'form': form}