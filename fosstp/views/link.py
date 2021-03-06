from pyramid.view import view_config
from pyramid_sqlalchemy import Session
import transaction
from ..models.link import LinkModel


@view_config(route_name='link', renderer='templates/link.jinja2')
def link_view(request):
    links = Session.query(LinkModel).all()
    return {'links': links}
