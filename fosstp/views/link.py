from pyramid.view import view_config


@view_config(route_name='link', renderer='templates/link.jinja2')
def link_view(request):
    return {}
