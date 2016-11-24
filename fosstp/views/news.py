from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid_sqlalchemy import Session
from ..forms.news import NewsAddForm, NewsForm
from ..models.news import NewsModel

@view_config(route_name='news', renderer='templates/news.jinja2')
def news_view(request):
    news = Session.query(NewsModel).all()
    return {'news': news}


@view_config(route_name='news_add', renderer='templates/news_add.jinja2', request_method='GET', permission='admin')
def news_add_view_get(request):
    form = NewsAddForm()
    return {'form': form}


@view_config(route_name='news_add', renderer='templates/news_add.jinja2', request_method='POST', permission='admin')
def news_add_view_post(request):
    import transaction

    form = NewsAddForm(request.POST)
    if form.validate():
        with transaction.manager:
            news = NewsModel()
            form.populate_obj(news)
            news.user_id = request.session['id']
            Session.add(news)
        raise HTTPFound(location=request.route_path('news'))
    else:
        return {'form': form}


@view_config(route_name='news_show', renderer='templates/news_show.jinja2')
def news_show_view_get(request):
    news_id = int(request.matchdict['id'])
    news = Session.query(NewsModel).get(news_id)
    return {'news': news}


@view_config(route_name='news_edit', renderer='templates/news_edit.jinja2', request_method='GET', permission='admin')
def news_edit_view_get(request):
    news_id = int(request.matchdict['id'])
    news = Session.query(NewsModel).get(news_id)
    form = NewsForm(obj=news)
    return {'form': form}


@view_config(route_name='news_edit', renderer='templates/news_edit.jinja2', request_method='POST', permission='admin')
def news_edit_view_post(request):
    import transaction

    form = NewsForm(request.POST)
    if form.validate():
        news_id = int(request.matchdict['id'])
        with transaction.manager:
            news = Session.query(NewsModel).get(news_id)
            form.populate_obj(news)
            Session.add(news)
        raise HTTPFound(location=request.route_path('news_show', id=news_id))
    else:
        return {'form': form}