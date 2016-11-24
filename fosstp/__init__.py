from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    from pyramid.settings import asbool

    # auth settings
    if asbool(settings['auth_mode']):
        from pyramid.security import Allow, Everyone, Authenticated, DENY_ALL, ALL_PERMISSIONS
        from pyramid.authentication import AuthTktAuthenticationPolicy
        from pyramid.authorization import ACLAuthorizationPolicy

        def get_user(request):
            from pyramid.security import unauthenticated_userid
            return unauthenticated_userid(request)

        def get_group(request):
            from pyramid_sqlalchemy import Session
            from .models.user import UserModel

            user = request.user
            if user:
                result = Session.query(UserModel).filter_by(name=user).one()
                return result.group

        def group_finder(userid, request):
            from pyramid_sqlalchemy import Session
            from .models.user import UserModel

            result = Session.query(UserModel).filter_by(name=userid).one_or_none()
            if result:
                return result.group.split(',')


        class RootFactory:
            __acl__ = [
                (Allow, Authenticated, 'edit'),
                (Allow, 'admin', ALL_PERMISSIONS),
            ]

            def __init__(self, request):
                pass

        authn_policy = AuthTktAuthenticationPolicy(settings['sessions.secret'],
                                                   timeout=86400, # cookie will expire after 1 day
                                                   callback=group_finder)
        authz_policy = ACLAuthorizationPolicy()

        config = Configurator(settings=settings,
                              root_factory=RootFactory,
                              authentication_policy=authn_policy,
                              authorization_policy=authz_policy)

        config.add_request_method(get_user, 'user', reify=True)
        config.add_request_method(get_group, 'group', reify=True)
    else:
        config = Configurator(settings=settings)

    # using jinja2 as default template engine
    config.include('pyramid_jinja2')

    # session settings
    if asbool(settings['production_mode']):
        # using pyramid_redis_sessions
        config.include('pyramid_redis_sessions')
    else:
        # using builtin session mechanism
        from pyramid.session import SignedCookieSessionFactory
        sessions_secret = settings['sessions.secret']
        session_factory = SignedCookieSessionFactory(sessions_secret)
        config.set_session_factory(session_factory)

    # transaction manager settings, used by pyramid_sqlalchemy and
    # pyramid_mailer
    config.include('pyramid_tm')

    # database settings
    config.include('pyramid_sqlalchemy')

    # mailer settings
    config.include('pyramid_mailer')

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('news', '/news')
    config.add_route('workshop', '/workshop')
    config.add_route('workshop_edit', '/workshop/edit')
    config.add_route('planet', '/planet')
    config.add_route('forum', '/forum')
    config.add_route('forum_category', '/forum_category/{id:\d+}')
    config.add_route('forum_category_add', '/forum_category/add')
    config.add_route('forum_topic', '/forum_topic/{id:\d+}')
    config.add_route('forum_topic_edit', '/forum_topic/{id:\d+}/edit')
    config.add_route('forum_topic_add', '/forum_category/{id:\d+}/topic_add')
    config.add_route('forum_reply_edit', '/forum_reply/{id:\d+}/edit')
    config.add_route('about', '/about')
    config.add_route('about_edit', '/about/edit')
    config.add_route('download', '/download')
    config.add_route('link', '/link')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('signup', '/signup')
    config.add_route('settings', '/settings')


    config.scan()
    return config.make_wsgi_app()
