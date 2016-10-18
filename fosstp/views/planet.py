from pyramid.view import view_config


@view_config(route_name='planet', renderer='templates/planet.jinja2')
def planet_view(request):
    return {}