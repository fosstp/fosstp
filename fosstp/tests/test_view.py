import unittest

from pyramid import testing

class ViewTests(unittest.TestCase):

    def setUp(self):
        self.request = testing.DummyRequest()
        self.config = testing.setUp(request=self.request)

    def tearDown(self):
        testing.tearDown()

    def test_home_view(self):
        from pyramid.httpexceptions import HTTPFound
        from ..views.home import home_view

        with self.assertRaises(HTTPFound):
            self.config.add_route('news', '/news')
            home_view(self.request)

    def test_news_view(self):
        from ..views.news import news_view
        info = news_view(self.request)
        self.assertEqual(info, {})

    def test_about_this_site_view(self):
        from ..views.about_this_site import about_this_site_view
        info = about_this_site_view(self.request)
        self.assertEqual(info, {})

    def test_workshop_view(self):
        from ..views.workshop import workshop_view
        info = workshop_view(self.request)
        self.assertEqual(info, {})

    def test_planet_view(self):
        from ..views.planet import planet_view
        info = planet_view(self.request)
        self.assertEqual(info, {})

    def test_forum_view(self):
        from ..views.forum import forum_view
        info = forum_view(self.request)
        self.assertEqual(info, {})

    def test_download_view(self):
        from ..views.download import download_view
        info = download_view(self.request)
        self.assertEqual(info, {})

    def test_link_view(self):
        from ..views.link import link_view
        info = link_view(self.request)
        self.assertEqual(info, {})

    def test_address_book_view(self):
        from ..views.address_book import address_book_view
        info = address_book_view(self.request)
        self.assertEqual(info, {})

    def test_login_view(self):
        from ..views.login import login_view
        info = login_view(self.request)
        self.assertEqual(info, {})

