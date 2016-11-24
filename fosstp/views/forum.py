from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid_sqlalchemy import Session
from ..models.forum import ForumCategoryModel, ForumTopicModel, ForumReplyModel
from ..forms.forum import ForumCategoryAddForm, ForumTopicAddForm, ForumTopicForm, ForumReplyAddForm, ForumReplyForm


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

@view_config(route_name='forum_topic', renderer='templates/forum_topic.jinja2', request_method='GET')
def forum_topic_view_get(request):
    forum_topic = Session.query(ForumTopicModel).get(int(request.matchdict['id']))
    forum_reply_form = ForumReplyAddForm()
    return {'forum_topic': forum_topic, 'forum_reply_form': forum_reply_form}

@view_config(route_name='forum_topic', renderer='templates/forum_topic.jinja2', request_method='POST', permission='member')
def forum_topic_view_post(request):
    import transaction

    forum_topic_id = int(request.matchdict['id'])
    forum_reply_form = ForumReplyAddForm(request.POST)
    if forum_reply_form.validate():
        with transaction.manager:
          forum_reply = ForumReplyModel()
          forum_reply_form.populate_obj(forum_reply)
          forum_reply.forum_topic_id = forum_topic_id
          forum_reply.user_id = request.session['id']
          Session.add(forum_reply)
        raise HTTPFound(location=request.route_path('forum_topic', id=forum_topic_id))
    else:
      forum_topic = Session.query(ForumTopicModel).get(forum_topic_id)
      return {'forum_topic': forum_topic}

@view_config(route_name='forum_reply_edit', renderer='templates/forum_reply_edit.jinja2', request_method='GET', permission='member')
def forum_reply_edit_view_get(request):
    forum_reply = Session.query(ForumReplyModel).get(int(request.matchdict['id']))
    form = ForumReplyForm(obj=forum_reply)
    return {'form': form, 'forum_reply': forum_reply}

@view_config(route_name='forum_reply_edit', renderer='templates/forum_reply_edit.jinja2', request_method='POST', permission='member')
def forum_reply_edit_view_post(request):
    import transaction

    forum_reply_id = int(request.matchdict['id'])
    forum_reply = Session.query(ForumReplyModel).get(forum_reply_id)
    forum_topic_id = forum_reply.topic.id
    form = ForumReplyForm(request.POST)
    if form.validate():
        with transaction.manager:
            form.populate_obj(forum_reply)
            Session.add(forum_reply)
        raise HTTPFound(location=request.route_path('forum_topic', id=forum_topic_id))
    else:
        return {'form': form, 'forum_reply': forum_reply}

@view_config(route_name='forum_topic_edit', renderer='templates/forum_topic_edit.jinja2', request_method='GET', permission='member')
def forum_topic_edit_view_get(request):
    forum_topic = Session.query(ForumTopicModel).get(int(request.matchdict['id']))
    form = ForumTopicForm(obj=forum_topic)
    return {'form': form, 'forum_topic': forum_topic}

@view_config(route_name='forum_topic_edit', renderer='templates/forum_topic_edit.jinja2', request_method='POST', permission='member')
def forum_topic_edit_view_post(request):
    import transaction

    forum_topic_id = int(request.matchdict['id'])
    forum_topic = Session.query(ForumTopicModel).get(forum_topic_id)
    form = ForumTopicForm(request.POST)
    if form.validate():
        with transaction.manager:
            form.populate_obj(forum_topic)
            Session.add(forum_topic)
        raise HTTPFound(location=request.route_path('forum_topic', id=forum_topic_id))
    else:
        return {'form': form, 'forum_topic': forum_topic}

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
