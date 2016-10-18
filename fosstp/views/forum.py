from pyramid.view import view_config


@view_config(route_name='forum', renderer='templates/forum.jinja2')
def forum_view(request):
    return {}
