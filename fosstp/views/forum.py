from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid_sqlalchemy import Session
from ..models.forum import ForumCategoryModel
from ..forms.forum import ForumCategoryAddForm


@view_config(route_name='forum', renderer='templates/forum.jinja2')
def forum_view(request):
    forum_categories = Session.query(ForumCategoryModel).all()
    return {'forum_categories': forum_categories}

@view_config(route_name='forum_category', renderer='templates/forum_category.jinja2')
def forum_category_view(request):
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
            form_category = ForumCategoryModel()
            form.populate_obj(form_category)
            Session.add(form_category)
        raise HTTPFound(location=request.route_path('forum'))
    else:
      return {'form': form}