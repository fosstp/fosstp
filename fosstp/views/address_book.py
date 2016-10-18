from pyramid.view import view_config


@view_config(route_name='address_book', renderer='templates/address_book.jinja2')
def address_book_view(request):
    return {}
