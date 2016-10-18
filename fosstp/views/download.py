from pyramid.view import view_config


@view_config(route_name='download', renderer='templates/download.jinja2')
def download_view(request):
    return {}
