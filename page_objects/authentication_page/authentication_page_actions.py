from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.authentication_page.authentication_page_objects import AuthenticationPageElements

# Instantiating Authentication Page Elements
authentication_page_elements = AuthenticationPageElements

class AuthenticationPageActions:

    # CHECK AND ASSERTIONS

    def check_error_message(self, error_message, error_message_2):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
                EC.visibility_of_element_located((By.ID, authentication_page_elements.error_message_id))
            )
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        message = element.text
        try:
            assert error_message == message
        except:
            assert error_message_2 == message

    # INPUT TEXT FIELDS ACTIONS

    def input_sign_up_email(self, email):
        element = self.driver.find_element(By.ID, authentication_page_elements.email_sign_up_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(email)

    def input_log_in_email(self, email):
        element = self.driver.find_element(By.ID, authentication_page_elements.email_log_in_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(email)

    def input_password(self, password):
        element = self.driver.find_element(By.ID, authentication_page_elements.password_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        element.clear()
        element.send_keys(password)

    # CLICK ACTIONS

    def click_create_account(self):
        element = self.driver.find_element(By.ID, authentication_page_elements.create_account_btn_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.driver.execute_script("arguments[0].click()", element)

    def click_log_in(self):
        element = self.driver.find_element(By.ID, authentication_page_elements.log_in_btn_id)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        self.driver.execute_script("arguments[0].click()", element)
