import time

from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By


class RecipeHomePageFunctionalTest(StaticLiveServerTestCase):
    def sleep(self, seconds=5):
        time.sleep(seconds)

    def test_the_test(self):
        browser = make_chrome_browser()
        try:
            browser.get(self.live_server_url)
            time.sleep(5)  # Pause to visually confirm the page load during testing
        finally:
            body = browser.find_element(by=By.TAG_NAME, value='body')
            self.assertIn('No Recipe Found Here', body.text)
            browser.quit()

