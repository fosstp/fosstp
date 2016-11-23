from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid_sqlalchemy import Session
from ..models.workshop import WorkshopModel
from ..forms.workshop import WorkshopEditForm


@view_config(route_name='workshop', renderer='templates/workshop.jinja2')
def workshop_view(request):
    workshop = Session.query(WorkshopModel).one_or_none()
    return {'workshop': workshop}

@view_config(route_name='workshop_edit', renderer='templates/workshop_edit.jinja2', request_method='GET', permission='admin')
def workshop_edit_view_get(request):
    workshop = Session.query(WorkshopModel).one_or_none()
    form = WorkshopEditForm(obj=workshop) if workshop else WorkshopEditForm()
    return {'form': form}

@view_config(route_name='workshop_edit', renderer='templates/workshop_edit.jinja2', request_method='POST', permission='admin')
def workshop_edit_view_post(request):
    import transaction

    form = WorkshopEditForm(request.POST)
    if form.validate():
        with transaction.manager:
            workshop = Session.query(WorkshopModel).one_or_none()
            if workshop:
                # 設定已存在，更新
                form.populate_obj(workshop)
            else:
                # 設定不存在，新增
                workshop = WorkshopModel()
                form.populate_obj(workshop)
            Session.add(workshop)
        raise HTTPFound(location=request.route_path('workshop'))
    else:
        return {'form': form}