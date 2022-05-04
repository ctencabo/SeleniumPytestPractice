""" This file holds the tests for the Automation Practice Page

    it includes tests for the;
        
"""
from msilib.schema import Error
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from test_cases.configtest import setup
from page_objects.landing_page.landing_page_actions import LandingPageActions
from page_objects.authentication_page.authentication_page_actions import AuthenticationPageActions
from configurations.test_data import AuthPageTestData

# create logger that will be used on all test cases
logger = LogGen.loggen()

class TestAutomationPractice:
    base_url = "http://automationpractice.com/index.php"

    @pytest.mark.signup
    def test_sign_up(self, setup):
        # Instantiate needed data for this test case
        auth_page_title = ReadConfig.get_authentication_page_title()
        landing_page_actions = LandingPageActions
        auth_page_actions = AuthenticationPageActions
        test_data = AuthPageTestData

        # Prepare the driver (ChromeDriver) to run with the given URL
        self.driver = setup
        self.driver.get(self.base_url)

        logger.info("*****START SIGN UP TEST CASE******")

        # NAVIGATE TO SIGN IN PAGE
        try:
            logger.info("*********CLICKING SIGN IN BUTTON************")
            landing_page_actions.click_sign_in(self)
            page_title = self.driver.title
            if page_title == auth_page_title:
                # SIGN UP WITH GIVEN CREDITS
                logger.info("*********ENTERING EMAIL****************")
                auth_page_actions.input_sign_up_email(self, test_data.new_email)
                auth_page_actions.click_create_account(self)
                # UNSUCCESSFUL FLOW
                logger.info("*********UNSUCCESSFUL SIGN UP FLOW****************")
                auth_page_actions.check_error_message(
                    self,
                    test_data.error_message,test_data.error_message_2)
            else:
                # raise exception to force to go to the except block
                raise Exception("*******USER WAS NOT REDIRECTED TO THE SIGN UP PAGE*******")
        except Exception as e:
            logger.info(e)
            self.driver.save_screenshot("./screen_shots/test_sign_up.png")
            raise ValueError
        finally:
            self.driver.quit()

    @pytest.mark.login
    def test_log_in(self, setup):
        # Instantiate needed data for this test case
        auth_page_title = ReadConfig.get_authentication_page_title()
        logged_in_page_title = ReadConfig.get_my_account_page_title()
        landing_page_actions = LandingPageActions
        auth_page_actions = AuthenticationPageActions
        test_data = AuthPageTestData

        # Prepare the driver (ChromeDriver) to run with the given URL
        self.driver = setup
        self.driver.get(self.base_url)

        logger.info("*****START LOG IN TEST CASE******")

        # NAVIGATE TO SIGN IN PAGE
        try:
            logger.info("*********CLICKING SIGN IN BUTTON************")
            landing_page_actions.click_sign_in(self)
            page_title = self.driver.title
            assert page_title == auth_page_title
        except:
            logger.info("*******USER WAS NOT REDIRECTED TO THE SIGN UP PAGE*******")
            self.driver.save_screenshot("./screen_shots/test_log_in.png")
            self.driver.quit()
            raise AssertionError

        # LOG IN WITH DIFFERENT SCENARIOS
        try:
            logger.info("*********LOG IN WITH BLANK FIELDS****************")
            auth_page_actions.click_log_in(self)
            auth_page_actions.check_log_in_error_message(
                self,test_data.log_in_error_message)
            auth_page_actions.check_log_in_error_message_second_line(
                self, test_data.log_in_error_message_no_email
            )
            logger.info("*********LOG IN WITHOUT PASSWORD****************")
            auth_page_actions.input_email(self, test_data.existing_email)
            auth_page_actions.click_log_in(self)
            auth_page_actions.check_log_in_error_message(
                self,test_data.log_in_error_message)
            auth_page_actions.check_log_in_error_message_second_line(
                self, test_data.log_in_error_message_no_password
            )
            logger.info("*********LOG IN WITH WRONG PASSWORD****************")
            auth_page_actions.input_password(self, test_data.wrong_password)
            auth_page_actions.click_log_in(self)
            auth_page_actions.check_log_in_error_message(
                self,test_data.log_in_error_message)
            auth_page_actions.check_log_in_error_message_second_line(
                self, test_data.log_in_error_message_wrong_creds
            )
            logger.info("*********LOG IN SUCCESSFULLY****************")
            auth_page_actions.input_password(self, test_data.password)
            auth_page_actions.click_log_in(self)
            time.sleep(3)
            page_title = self.driver.title
            assert page_title == logged_in_page_title
        except (NoSuchElementException) as e:
            logger.info(e)
            self.driver.save_screenshot("./screen_shots/test_log_in.png")
            raise Error
        except AssertionError:
            logger.info("*******USER WAS NOT REDIRECTED TO THE MY ACCOUNT PAGE*******")
            self.driver.save_screenshot("./screen_shots/test_log_in.png")

        finally:
            self.driver.quit()


    @pytest.mark.addtocart
    def test_add_to_cart_hover(self, setup):
        # Instantiate needed data for this test case
        landing_page_title = ReadConfig.get_landing_page_title()
        landing_page_actions = LandingPageActions

        # Prepare the driver (ChromeDriver) to run with the given URL
        self.driver = setup
        self.driver.get(self.base_url)

        logger.info("*****START ADD TO CART TEST CASE******")
        # ADD TO CART A POPULAR CLOTHING
        try:
            page_title = self.driver.title
            assert page_title == landing_page_title
            logger.info("*********HOVERING TO THE POPULAR CLOTHES************")
            landing_page_actions.hover_to_popular_first(self)
            logger.info("*********CLICKING ADD TO CART************")
            landing_page_actions.click_add_to_cart_hover_btn(self)
        except AssertionError as e:
            logger.info(e)
            self.driver.save_screenshot("./screen_shots/test_sign_up.png")
            raise AssertionError
        except Exception as e:
            pass
        finally:
            self.driver.quit()

    @pytest.mark.addtocart
    def test_add_to_cart_quickview(self, setup):
        # Instantiate needed data for this test case
        landing_page_title = ReadConfig.get_landing_page_title()
        landing_page_actions = LandingPageActions

        # Prepare the driver (ChromeDriver) to run with the given URL
        self.driver = setup
        self.driver.get(self.base_url)

        logger.info("*****START ADD TO CART TEST CASE******")
        # ADD TO CART A POPULAR CLOTHING
        try:
            page_title = self.driver.title
            assert page_title == landing_page_title
            logger.info("*********HOVERING TO THE POPULAR CLOTHES************")
            landing_page_actions.hover_to_popular_first(self)
            logger.info("*********CLICKING QUICKVIEW BUTTON************")
            landing_page_actions.click_quick_view_btn(self)
            landing_page_actions.click_add_to_cart(self)
        except AssertionError as e:
            logger.info(e)
            self.driver.save_screenshot("./screen_shots/test_sign_up.png")
            raise AssertionError
        except Exception as e:
            pass
        finally:
            self.driver.quit()
