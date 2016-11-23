from pyramid.view import view_config


@view_config(route_name='logout')
def logout(request):
    from pyramid.security import forget
    from pyramid.httpexceptions import HTTPFound

    if 'id' in request.session: del request.session['id']
    if 'group' in request.session: del request.session['group']
    request.session.flash('您已登出', 'info')
    headers = forget(request)
    raise HTTPFound(location=request.route_path('news'), headers=headers)