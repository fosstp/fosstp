from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid_sqlalchemy import Session
from ..models.forum import ForumCategoryModel, ForumTopicModel
from ..forms.forum import ForumCategoryAddForm, ForumTopicAddForm


@view_config(route_name='forum', renderer='templates/forum.jinja2')
def forum_view(request):
    forum_categories = Session.query(ForumCategoryModel).all()
    return {'forum_categories': forum_categories}

@view_config(route_name='forum_category', renderer='templates/forum_category.jinja2')
def forum_category_view(request):
    '''顯示特定討論分類文章列表'''
    forum_category_id = int(request.matchdict['id'])
    forum_category = Session.query(ForumCategoryModel).get(forum_category_id)
    return {'forum_category': forum_category}

@view_config(route_name='forum_category_add', renderer='templates/forum_category_add.jinja2', request_method='GET', permission='member')
def forum_category_add_view_get(request):
    form = ForumCategoryAddForm()
    return {'form': form}

@view_config(route_name='forum_category_add', renderer='templates/forum_category_add.jinja2', request_method='POST', permission='member')
def forum_category_add_view_post(request):
    import transaction

    form = ForumCategoryAddForm(request.POST)
    if form.validate():
        with transaction.manager:
            forum_category = ForumCategoryModel()
            form.populate_obj(forum_category)
            Session.add(forum_category)
        raise HTTPFound(location=request.route_path('forum'))
    else:
        return {'form': form}

@view_config(route_name='forum_topic_add', renderer='templates/forum_topic_add.jinja2', request_method='GET', permission='member')
def forum_topic_add_view_get(request):
    form = ForumTopicAddForm()
    forum_category = Session.query(ForumCategoryModel).get(int(request.matchdict['id']))
    return {'form': form, 'forum_category': forum_category}

@view_config(route_name='forum_topic_add', renderer='templates/forum_topic_add.jinja2', request_method='POST', permission='member')
def forum_topic_add_view_post(request):
    import transaction

    form = ForumTopicAddForm(request.POST)
    forum_category_id = int(request.matchdict['id'])
    if form.validate():
        with transaction.manager:
            forum_topic = ForumTopicModel()
            form.populate_obj(forum_topic)
            forum_topic.category_id = forum_category_id
            forum_topic.user_id = request.session['id']
            Session.add(forum_topic)
        raise HTTPFound(location=request.route_path('forum_category', id=forum_category_id))
    else:
        forum_category = Session.query(ForumCategoryModel).get(forum_category_id)
        return {'form': form, 'forum_category': forum_category}