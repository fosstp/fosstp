from pyramid.view import view_config
from pyramid_sqlalchemy import Session
from ..models.planet import PlanetContentModel


@view_config(route_name='planet', renderer='templates/planet.jinja2')
def planet_view(request):
    planet_contents = Session.query(PlanetContentModel).all()
    return {'planet_contents': planet_contents}