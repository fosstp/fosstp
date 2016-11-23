from pyramid.view import view_config


@view_config(route_name='logout')
def logout(request):
    from pyramid.security import forget
    from pyramid.httpexceptions import HTTPFound

    headers = forget(request)
    if request.session['id']: del request.session['id']
    if request.session['group']: del request.session['group']
    request.session.flash('您已登出', 'info')
    raise HTTPFound(location=request.route_path('news'), headers=headers)