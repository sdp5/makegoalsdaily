from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 2


class NewVisitorTest(StaticLiveServerTestCase):
    import os
    print(os.getcwd())
    fixtures = ['functional_tests/auth_dump.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_start_page(self):
        # open URL in browser
        self.browser.get(self.live_server_url)

        # Page title mention make-goals-daily
        self.assertIn('make-goals-daily', self.browser.title)

    def test_login(self):
        # Login into application
        self.browser.get(self.live_server_url)
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('administration')
        self.browser.find_element_by_xpath(
            '/html/body/div[1]/form/button').click()

        # Wait until the response is received
        WebDriverWait(self.browser, TIMEOUT).until(
            lambda driver: driver.find_element_by_tag_name('body'))

        project_name = self.browser.find_element_by_xpath(
            '/html/body/nav/div/div/a').text
        self.assertIn('make-goals-daily', project_name)

    def test_add_goal(self):
        pass
