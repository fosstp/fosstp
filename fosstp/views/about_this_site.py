from pyramid.view import view_config


@view_config(route_name='about_this_site', renderer='templates/about_this_site.jinja2')
def about_this_site_view(request):
    return {}
