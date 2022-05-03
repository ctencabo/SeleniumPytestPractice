"""This file reads the information from the config.ini file
    It includes multiple methods that are used to read and return
    specific data from the configuration file
"""
import configparser

config = configparser.RawConfigParser()
config.read("./configurations/config.ini")

class ReadConfig:
    """This class consists of methods that retrieve
    information from the configuration file"""

    @staticmethod
    def get_landing_page_title():
        "This method retrieves the landing page title from config file"
        landing_page_title = config.get(
            'Page titles', 'landing_page_title'
        )
        return landing_page_title

    @staticmethod
    def get_authentication_page_title():
        "This method retrieves the authentication page title from config file"
        auth_page_title = config.get(
            'Page titles', 'auth_page_title'
        )
        return auth_page_title
