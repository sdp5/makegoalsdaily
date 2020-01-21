from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_add_goal(self):
        # open project url in browser
        self.browser.get('http://localhost:8000')

        # Page title mention make-goals-daily
        self.assertIn('make-goals-daily', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
