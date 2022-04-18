""" This file is a collection of all the page elements and the action methods 
    of the landing page.

    The elements are identified using;
        -- xpath (Relative xpath recommended)
        -- id
        -- css-selectors and many others
"""
class LandingPageElements:

    # Labels/Texts
    nav_bar_call_us_now_text_xpath = ".//span[@class='shop-phone']"
    nav_bar_contact_us_text_xpath = ".//a[@title='Contact Us']"
    nav_bar_sign_in_text_xpath = ".//a[@class='login']"

    homeslider_header_xpath = ".//div[@class='homeslider-description']/h2"
    homeslider_description_xpath = ".//div[@class='homeslider-description']/p"

    popular_text_xpath = ".//a[@class='homefeatured']"
    bestsellters_text_xpath = ".//a[@class='blockbestsellers']"

    # Buttons
    women_btn_xpath = ".//a[@title='Women']"
    dresses_btn_xpath = ".//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li/a[@title='Dresses']"
    tshirt_btn_xpath = ".//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li/a[@title='T-shirts']"
    next_btn_xpath = ".//a[@class='bx-next']"
    prev_btn_xpath = ".//a[@class='bx-prev']"

    shop_now_btn_xpath = ".//button[text()='Shop now !']"

    # Search Bars
    search_bar_id = "search_query_top"

    # Dropdowns

    # Images
    banner_xpath = ".//img[@class='img-responsive'"
    logo_xpath = ".//img[@class='logo img-responsive'"
