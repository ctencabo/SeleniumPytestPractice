""" This file is a collection of all the page elements and the action methods 
    of the authentication page.

    The elements are identified using;
        -- xpath (Relative xpath recommended)
        -- id
        -- css-selectors and many others
"""
class AuthenticationPageElements:

    # Buttons
    create_account_btn_id = "SubmitCreate"
    log_in_btn_id = "SubmitLogin"

    # Text Fields
    email_sign_up_id = "email_create"
    email_id = "email"
    password_id = "passwd"

    # Texts
    error_message_id = "create_account_error"
    log_in_error_firstline_xpath = "//div[@class='alert alert-danger']/p"
    log_in_error_secondline_xpath = "//div[@class='alert alert-danger']//li"

    """CREATE ACCOUNT ELEMENTS"""

    # Input Fields
    info_first_name_id = "customer_firstname"
    info_last_name_id = "customer_lastname"

    address_first_name_id = "firstname"
    address_last_name_id = "lastname"
    address_id = "address1"
    city_id = "city"
    state_id = "id_state"
    postcode_id = "postcode"
    country_id = "id_country"
    mobile_id = "phone_mobile"
    alias_address_id = "alias"
    
    # Button
    register_id = "submitAccount"
