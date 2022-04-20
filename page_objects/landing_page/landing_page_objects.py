""" This file is a collection of all the page elements and the action methods 
    of the landing page.

    The elements are identified using;
        -- xpath (Relative xpath recommended)
        -- id
        -- css-selectors and many others
"""
class LandingPageElements:

    # Common Xpaths

    popular_first = ".//ul[@id='homefeatured']/li[position()=1]"
    bestseller_first = ".//ul[@id='blockbestsellers']/li[position()=1]"

    # Labels/Texts
    nav_bar_sign_in_text_xpath = ".//a[@class='login']"

    popular_tab_xpath = ".//a[@class='homefeatured']"
    bestsellters_tab_xpath = ".//a[@class='blockbestsellers']"

    hover_price_xpath = "//div[@class='left-block']//div[@class='content_price']"
    unhovered_price_xpath = "//div[@class='right-block']//div[@class='content_price']"

    # Buttons
    women_btn_xpath = ".//a[@title='Women']"
    dresses_btn_xpath = ".//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li/a[@title='Dresses']"
    tshirt_btn_xpath = ".//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li/a[@title='T-shirts']"

    quickview_btn_xpath = "//a[@class='quick-view']"

    hover_add_to_cart_btn_xpath = "//a[@title='Add to cart']"
    hover_more_btn_xpath = "//a[@title='View']"

    # Search Bars
    search_bar_id = "search_query_top"

    # Images
    logo_xpath = ".//img[@class='logo img-responsive']"
    popular_first_img_xpath = "{popular}//img".format(popular=popular_first)
    bestseller_first_img_xpath = "{bestseller}//img".format(bestseller=bestseller_first)
