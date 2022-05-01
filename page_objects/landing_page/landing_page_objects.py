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

    hover_price_xpath = "//div[@class='left-block']" \
        "//div[@class='content_price']"
    unhovered_price_xpath = "//div[@class='right-block']" \
        "//div[@class='content_price']"

    # Buttons
    women_btn_xpath = ".//a[@title='Women']"
    dresses_btn_xpath = ".//ul[@class='sf-menu clearfix menu-content" \
        " sf-js-enabled sf-arrows']/li/a[@title='Dresses']"
    tshirt_btn_xpath = ".//ul[@class='sf-menu clearfix menu-content" \
        " sf-js-enabled sf-arrows']/li/a[@title='T-shirts']"

    quickview_btn_xpath = "//li[contains(@class,'hovered')]" \
        "//a[@class='quick-view']"

    hover_add_to_cart_btn_xpath = "//li[contains(@class,'hovered')]" \
        "//a[@title='Add to cart']"
    hover_more_btn_xpath = "//li[contains(@class,'hovered')]//a[@title='View']"

    # Search Bars
    search_bar_id = "search_query_top"

    # Images
    logo_xpath = ".//img[@class='logo img-responsive']"
    popular_first_img_xpath = "{popular}//img".format(popular=popular_first)
    bestseller_first_img_xpath = "{bestseller}//img".format(
        bestseller=bestseller_first)


class QuickViewElements:
    """Elements found inside the quick view modal"""

    # Texts/Labels

    price_id = "our_price_display"
    product_name_xpath = "//h1[@itemprop='name']"
    product_ref_id = "product_reference"
    product_condition_id = "product_condition"
    product_description_id = "short_description_content"
    quantity_label_xpath = "//p[@id='quantity_wanted_p']/label"
    size_label_xpath = "//label[@class='attribute_label']" \
        "[contains(text(),'Size')]"
    color_label_xpath = "//label[@class='attribute_label']" \
        "[contains(text(),'Color')]"

    # Buttons

    close_btn_xpath = "//a[@title='Close']"
    minus_btn_xpath = "//a[contains(@class,'product_quantity_down')]"
    plus_btn_xpath = "//a[contains(@class,'product_quantity_up')]"
    color_selected_xpath = "//ul[@id='color_to_pick_list']" \
        "/li[@class='selected']"
    color_unselected_xpath = "//ul[@id='color_to_pick_list']" \
        "/li[@class='selected']/following-sibling::li[position()=1]"
    add_to_cart_btn_xpath = "//button[@name='Submit'][@class='exclusive']"
    add_to_wishlist_id = "wishlist_button"

    next_btn_id = "view_scroll_right"
    prev_btn_id = "view_scroll_left"

    # Input Fields

    quantity_input_field_id = "quantity_wanted"

    # Dropdown

    size_dropdown_id = "group_1"

    # Images

    img_preview_id = "bigpic"
    img_list_id = "thumbs_list_frame"

