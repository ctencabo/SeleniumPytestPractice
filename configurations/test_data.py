class AuthPageTestData:
    # Register Data
    new_email = "test_test{random_number}@test.com"
    first_name = "Test"
    last_name = "Test"
    password = "Test123"
    address = "Test Address"
    city = "Test City"
    state = "Hawaii"
    postcode = "12345"
    country = "United States"
    mobile_number = "12312312312312"
    alias_address = "Test Alias"

    # Existing Data
    existing_email = "test_test@test.com"
    wrong_password = "testtest"

    # Error Message
    error_message = "An account using this email address has already been registered. " \
        "Please enter a valid password or request a new one."
    error_message_2 = "Invalid email address."

    log_in_error_message = "There is 1 error"
    log_in_error_message_wrong_creds = "Authentication failed."
    log_in_error_message_no_email = "An email address required."
    log_in_error_message_no_password = "Password is required."
