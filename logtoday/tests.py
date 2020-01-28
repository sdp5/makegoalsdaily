from django.test import TestCase
from django.urls import resolve


class HomePageTest(TestCase):

    def test_root_url_resolves_to_index_page_view(self):
        found = resolve("/")
        self.assertEqual(found.view_name, "index")

    def test_uses_login_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'login.html')
