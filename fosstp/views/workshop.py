from pyramid.view import view_config


@view_config(route_name='workshop', renderer='templates/workshop.jinja2')
def workshop_view(request):
    return {}
