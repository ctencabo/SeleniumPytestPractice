"""This is a set up method that contains all the generic requirements for all pages

    -- The ChromeDriver provides capabilities for navigating to web pages, user input,
        JavaScript execution, and more.
    -- The headless option is a boolean that enables and disables running the tests in headless mode
    -- The Implicit Wait is used to tell the web driver to wait for a certain amount of time in
    seconds before it throws a "No Such Element Exception".
    -- The maximize window is used to maximize the browser window size

    This method will run before every test method.

"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    """This method runs before every test method."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(25)
    driver.maximize_window()

    return driver
