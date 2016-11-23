from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid_sqlalchemy import Session
from ..models.about import AboutModel
from ..forms.about import AboutEditForm


@view_config(route_name='about', renderer='templates/about.jinja2')
def about_view(request):
    about = Session.query(AboutModel).one_or_none()
    return {'about': about}

@view_config(route_name='about_edit', renderer='templates/about_edit.jinja2', request_method='GET', permission='admin')
def about_edit_view_get(request):
    about = Session.query(AboutModel).one_or_none()
    form = AboutEditForm(obj=about) if about else AboutEditForm()
    return {'form': form}

@view_config(route_name='about_edit', renderer='templates/about_edit.jinja2', request_method='POST', permission='admin')
def about_edit_view_post(request):
    import transaction

    form = AboutEditForm(request.POST)
    if form.validate():
        # transaction 遇到 exception 會 abort，因此手工處理
        with transaction.manager:
            about = Session.query(AboutModel).one_or_none()
            if about:
                # 設定已存在，更新
                form.populate_obj(about)
            else:
                # 設定不存在，新增
                about = AboutModel()
                form.populate_obj(about)
            Session.add(about)
        raise HTTPFound(location=request.route_path('about'))
    else:
        return {'form': form}