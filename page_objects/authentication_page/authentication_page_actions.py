from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from page_objects.authentication_page.authentication_page_objects import AuthenticationPageElements

# Instantiating Authentication Page Elements
authentication_page_elements = AuthenticationPageElements

class AuthenticationPageActions:

    # CHECK AND ASSERTIONS

    def check_error_message(self, error_message, error_message_2):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
                EC.visibility_of_element_located(
                    (By.ID, authentication_page_elements.error_message_id))
            )
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        message = element.text
        try:
            assert error_message == message
        except:
            assert error_message_2 == message

    def check_log_in_error_message(self, error_message):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
                EC.visibility_of_element_located(
                    (By.ID, authentication_page_elements.log_in_error_firstline_xpath))
            )
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        message = element.text

        assert message == error_message


    def check_log_in_error_message_second_line(self, error_message):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
                EC.visibility_of_element_located(
                    (By.ID, authentication_page_elements.log_in_error_secondline_xpath))
            )
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        message = element.text

        assert message == error_message

    # INPUT TEXT FIELDS ACTIONS

    def input_sign_up_email(self, email):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.email_sign_up_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(email)

    def input_email(self, email):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.email_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(email)

    def input_password(self, password):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.password_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(password)


    ### REGISTRATION PAGE

    def input_info_firstname(self, firstname):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.info_first_name_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(firstname)

    def input_info_lastname(self, lastname):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.info_last_name_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(lastname)

    def input_address_firstname(self, firstname):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.address_first_name_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(firstname)

    def input_address_lastname(self, lastname):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.address_last_name_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(lastname)

    def input_address(self, address):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.address_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(address)

    def input_city(self, city):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.city_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(city)

    def select_state(self, state):
        element = Select(self.driver.find_element(
            By.ID, authentication_page_elements.state_id))
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.select_by_visible_text(state)

    def input_postcode(self, postcode):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.postcode_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(postcode)

    def select_country(self, country):
        element = Select(self.driver.find_element(
            By.ID, authentication_page_elements.country_id))
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.select_by_visible_text(country)

    def input_mobile_number(self, mobile_number):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.mobile_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(mobile_number)

    def input_address_alias(self, alias):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.alias_address_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(alias)
        

    # CLICK ACTIONS

    def click_create_account(self):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.create_account_btn_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.driver.execute_script("arguments[0].click()", element)

    def click_log_in(self):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.log_in_btn_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.driver.execute_script("arguments[0].click()", element)

    def click_register(self):
        element = self.driver.find_element(
            By.ID, authentication_page_elements.register_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.driver.execute_script("arguments[0].click()", element)
