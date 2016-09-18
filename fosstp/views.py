from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound


@view_config(route_name='home')
def home_view(request):
    return HTTPFound(request.route_url('news'))

@view_config(route_name='news', renderer='templates/news.jinja2')
def news_view(request):
    return {}

@view_config(route_name='about_this_site', renderer='templates/about_this_site.jinja2')
def about_this_site_view(request):
    return {}

@view_config(route_name='workshop', renderer='templates/workshop.jinja2')
def workshop_view(request):
    return {}

@view_config(route_name='planet', renderer='templates/planet.jinja2')
def planet_view(request):
    return {}

@view_config(route_name='forum', renderer='templates/forum.jinja2')
def forum_view(request):
    return {}

@view_config(route_name='download', renderer='templates/download.jinja2')
def download_view(request):
    return {}

@view_config(route_name='link', renderer='templates/link.jinja2')
def link_view(request):
    return {}

@view_config(route_name='address_book', renderer='templates/address_book.jinja2')
def address_book_view(request):
    return {}

@view_config(route_name='log', renderer='templates/log.jinja2')
def log_view(request):
    return {}

@view_config(route_name='login', renderer='templates/login.jinja2')
def login_view(request):
    return {}
