from selenium.webdriver.common.by import By

from .landing_page_objects import LandingPageElements

# Instantiating Landing Page Elements
landing_page_elements = LandingPageElements

class LandingPageActions:

    # CLICK ACTIONS

    def click_sign_in(self):
        element = self.driver.find_element(By.XPATH, landing_page_elements.nav_bar_sign_in_text_xpath)
        self.driver.execute_script("arguments[0].click()", element)

    
