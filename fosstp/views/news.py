from pyramid.view import view_config


@view_config(route_name='news', renderer='templates/news.jinja2')
def news_view(request):
    return {}