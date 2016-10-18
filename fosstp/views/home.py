from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


@view_config(route_name='home')
def home_view(request):
    raise HTTPFound(request.route_url('news'))
