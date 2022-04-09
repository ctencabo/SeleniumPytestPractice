""" This file holds the tests for the Automation Practice Page

    it includes tests for the;
        
"""
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from test_cases.configtest import setup
from page_objects.landing_page_objects import LandingPageElements
from data.test_data import LandingPageTestData

landing_page_elements = LandingPageElements
test_data = LandingPageTestData

class TestAutomationPractice:
    base_url = "http://automationpractice.com/index.php"

    def test_search_functionality(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        try:
            element = self.driver.find_element(By.ID, landing_page_elements.search_bar_id)
            element.send_text(test_data.search_data)
        except:
            self.driver.save_screenshot("./screen_shots/test_search_functionality.png")
        finally:
            self.driver.quit()
