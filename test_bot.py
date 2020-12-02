import os 
from time import sleep

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
    
    def login(self, username, password):
        username_input = self.firefox_browser.find_element_by_name("username")
        password_input = self.firefox_browser.find_element_by_name("password")
        USERNAME = os.environ.get("INSTA_USER")
        PASSWORD = os.environ.get("INSTA_PASS")
        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)
        