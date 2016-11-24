from pyramid.view import view_config
from pyramid_sqlalchemy import Session
from ..models.news import NewsModel
from ..models.forum import ForumTopicModel
from ..models.link import LinkModel


@view_config(route_name='home', renderer='templates/home.jinja2')
def home_view(request):
    news_list = Session.query(NewsModel).order_by(NewsModel.id.desc())[:10]
    forum_topic_list = Session.query(ForumTopicModel).order_by(ForumTopicModel.id.desc())[:10]
    link_list = Session.query(LinkModel).all()
    return {'news_list': news_list, 'forum_topic_list': forum_topic_list, 'link_list': link_list}
