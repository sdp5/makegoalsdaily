from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

TIMEOUT = 2


class NewVisitorTest(StaticLiveServerTestCase):
    fixtures = ['tests/functional/auth_dump.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_start_page(self):
        # open URL in browser
        self.browser.get(self.live_server_url)

        # Page title mention make-goals-daily
        self.assertIn('make-goals-daily', self.browser.title)

    def test_can_add_new_goal(self):
        # Login into application
        self.browser.get(self.live_server_url)
        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('administration')
        self.browser.find_element_by_xpath(
            "//button[@type='submit']").click()

        # Wait until the response is received
        WebDriverWait(self.browser, TIMEOUT).until(
            lambda driver: driver.find_element_by_tag_name('body'))

        project_name = self.browser.find_element_by_xpath(
            "//div[@class='navbar-header']/a").text
        self.assertIn('Make Goals Daily', project_name)

        # Go to Goals Tab
        self.browser.find_element_by_xpath(
            "//a[contains(@href, '/dashboard/goals/')]").click()

        # Open add goal form
        self.browser.find_element_by_xpath(
            "//a[contains(@href, '/dashboard/goals/add/')]").click()

        # Fill the entries in the new goal form
        goal_slug_input = self.browser.find_element_by_name('goal_slug')
        goal_slug_input.send_keys('Go-to-mars')
        goal_desc_input = self.browser.find_element_by_name('goal_desc')
        goal_desc_input.send_keys('Tour to mars')
        goal_target_input = self.browser.find_element_by_name('goal_target')
        goal_target_input.send_keys('01/22/2020')
        goal_category = Select(self.browser.find_element_by_name(
            'goal_category'))
        goal_category.select_by_value('Excursion')
        goal_weight = Select(self.browser.find_element_by_name('goal_weight'))
        goal_weight.select_by_value('1')

        # Save goal
        self.browser.find_element_by_xpath(
            "//input[@value='Save Details']").click()

        # Check goal section is visible
        goal_heading = self.browser.find_element_by_xpath(
            "//div[@class='container']/div[1]/h2")
        self.assertEqual(goal_heading.text, 'Excursion')

        # Assert goal added
        goal_field = self.browser.find_element_by_xpath(
            "//div[contains(@class, 'panel-body')]/h3").text
        self.assertEqual(goal_field, "Go-to-mars Tour to mars")
