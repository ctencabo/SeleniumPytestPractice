""" This file holds the tests for the Automation Practice Page

    it includes tests for the;
        
"""
import time
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from test_cases.configtest import setup
from page_objects.landing_page.landing_page_actions import LandingPageActions
from page_objects.authentication_page.authentication_page_actions import AuthenticationPageActions
from configurations.test_data import AuthPageTestDate

# create logger that will be used on all test cases
logger = LogGen.loggen()

class TestAutomationPractice:
    base_url = "http://automationpractice.com/index.php"

    def test_sign_up_functionality(self, setup):
        auth_page_title = ReadConfig.get_authentication_page_title()
        landing_page_actions = LandingPageActions
        auth_page_actions = AuthenticationPageActions
        test_data = AuthPageTestDate

        self.driver = setup
        self.driver.get(self.base_url)

        logger.info("*****START SIGN IN FUNCTIONALITY******")

        # NAVIGATE TO SIGN IN PAGE
        try:
            logger.info("*********CLICKING SIGN IN BUTTON************")
            landing_page_actions.click_sign_in(self)
            page_title = self.driver.title
            if page_title == auth_page_title:
                auth_page_actions.input_sign_up_email(self, test_data.new_email)
                auth_page_actions.click_create_account(self)
            else:
                # raise exception to force to go to the except field
                raise Exception("did not redirect")
        except:
            self.driver.save_screenshot("./screen_shots/test_sign_up.png")
            raise ValueError
        finally:
            self.driver.quit()
