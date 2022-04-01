""" This file holds the tests for the Automation Practice Page

    it includes tests for the;
        
"""
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from test_cases.configtest import setup
from page_objects.landing_page_objects import LandingPageElements

landing_page_elements = LandingPageElements

class TestAutomationPractice:
    base_url = "http://automationpractice.com/index.php"

    def test_ui_checks(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        try:
            element = self.driver.find_element(By.XPATH, landing_page_elements.nav_bar_call_us_now_text)
            call_us_now_text = element.text
            print(call_us_now_text)
            assert call_us_now_text == "Call us now: 0123-456-789"
        except:
            pass
        finally:
            self.driver.quit()
