from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from .landing_page_objects import LandingPageElements, QuickViewElements

# Instantiating Landing Page Elements
landing_page_elements = LandingPageElements
quick_view_elements = QuickViewElements

class LandingPageActions:

    # CLICK ACTIONS

    def click_sign_in(self):
        element = self.driver.find_element(
            By.XPATH,
            landing_page_elements.nav_bar_sign_in_text_xpath)
        self.driver.execute_script("arguments[0].click()", element)

    def click_popular_tab(self):
        element = self.driver.find_element(
            By.XPATH,
            landing_page_elements.popular_tab_xpath)
        self.driver.execute_script("arguments[0].click()", element)

    def click_bestseller_tab(self):
        element = self.driver.find_element(
            By.XPATH,
            landing_page_elements.bestsellters_tab_xpath)
        self.driver.execute_script("arguments[0].click()", element)

    def click_popular_first(self):
        element = self.driver.find_element(
            By.XPATH,
            landing_page_elements.popular_first_img_xpath)
        self.driver.execute_script("arguments[0].click()", element)

    def click_bestseller_first(self):
        element = self.driver.find_element(
            By.XPATH,
            landing_page_elements.bestseller_first_img_xpath)
        self.driver.execute_script("arguments[0].click()", element)

    def click_quick_view_btn(self):
        element = self.driver.find_element(
            By.XPATH,
            landing_page_elements.quickview_btn_xpath)
        self.driver.execute_script("arguments[0].click()", element)

    def click_add_to_cart_hover_btn(self):
        element = self.driver.find_element(
            By.XPATH,
            landing_page_elements.hover_add_to_cart_btn_xpath)
        self.driver.execute_script("arguments[0].click()", element)

    ### QUICKVIEW CLICK ACTIONS

    def click_plus_quantity(self):
        element = self.driver.find_element(
            By.ID,
            quick_view_elements.plus_btn_xpath)
        self.driver.execute_script("arguments[0].click()", element)

    def click_minus_quantity(self):
        element = self.driver.find_element(
            By.ID,
            quick_view_elements.minus_btn_xpath)
        self.driver.execute_script("arguments[0].click()", element)

    def click_unselected_color(self):
        # Check if there is another color
        try:
            # Check if there is another color which is next to the selected
            element = self.driver.find_element(
                By.XPATH,
                quick_view_elements.color_unselected_next_xpath)
        except:
            # Check if there is another color which is previous to the selected
            element = self.driver.find_element(
                By.XPATH,
                quick_view_elements.color_unselected_prev_xpath)
        finally:
            # Instantiate element variable with current selected color
            element = self.driver.find_element(
                By.XPATH,
                quick_view_elements.color_selected_xpath)
            self.driver.execute_script("arguments[0].click()", element)

    def click_add_to_cart(self):
        element = self.driver.find_element(
            By.XPATH,
            quick_view_elements.add_to_cart_btn_xpath)
        self.driver.execute_script("arguments[0].click()", element)

    def click_add_to_wishlist(self):
        element = self.driver.find_element(
            By.ID,
            quick_view_elements.add_to_wishlist_id)
        self.driver.execute_script("arguments[0].click()", element)

    # HOVER ACTIONS

    def hover_to_popular_first(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(
            By.XPATH,
            landing_page_elements.popular_first_img_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        action.move_to_element(element).perform()

    def hover_to_bestseller_first(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(
            By.XPATH,
            landing_page_elements.bestseller_first_img_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView()", element)
        action.move_to_element(element).perform()

    # INPUT ACTIONS

    def input_quantity(self, quantity):
        element = self.driver.find_element(
            By.ID,
            quick_view_elements.quantity_input_field_id)
        element.send_keys(quantity)
