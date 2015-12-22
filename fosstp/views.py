from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    return {}

@view_config(route_name='about_us', renderer='templates/about_us.jinja2')
def about_us_view(request):
    return {}

@view_config(route_name='login', renderer='templates/login.jinja2')
def login_view(request):
    return {}
