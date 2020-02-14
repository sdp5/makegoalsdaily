from django.test import TestCase
from django.urls import resolve
from logtoday.models import GoalsCategory


class HomePageTest(TestCase):
    fixtures = ['tests/functional/auth_dump.json']

    def test_root_url_resolves_to_index_page_view(self):
        found = resolve("/")
        self.assertEqual(found.view_name, "index")

    def test_uses_login_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'login.html')

    def test_redirects_login_and_logout(self):
        response = self.client.post('/login/', {'username': 'admin',
                                                'password': 'administration'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/dashboard/')

        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')

    def test_uses_dashboard_landing_page(self):
        # login is required to access /dashboard url.
        self.client.post('/login/', {'username': 'admin',
                                     'password': 'administration'})
        response = self.client.get('/dashboard', follow=True)
        self.assertTemplateUsed(response, 'dashboard/landing_page.html')


class ModelTest(TestCase):

    def test_adding_and_removing_goal_categories(self):
        goal_first = GoalsCategory()
        goal_first.category_value = "reading"
        goal_first.category_name = "Read - Activities"
        goal_first.save()

        goal_second = GoalsCategory()
        goal_second.category_value = "sketching"
        goal_second.category_name = "sketch - Activities"
        goal_second.save()

        saved_categories = GoalsCategory.objects.all()
        self.assertEqual(saved_categories.count(), 2)

        first_saved_goal = saved_categories[0]
        self.assertEqual(first_saved_goal.category_value, "reading")

        goal_first.delete()
        saved_categories = GoalsCategory.objects.all()
        self.assertEqual(saved_categories.count(), 1)
