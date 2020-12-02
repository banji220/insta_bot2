import os 
from time import sleep
from selenium import webdriver

firefox_browser = webdriver.Firefox()

class Login:
    def __init__(self, firefox_browser):
        self.firefox_browser = firefox_browser
        self.firefox_browser.get("https://www.instagra.com")
        
            
    def login_me(self, username, password):
        username_input = self.firefox_browser.find_element_by_name("username")
        password_input = self.firefox_browser.find_element_by_name("password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.firefox_browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)
    
    
    

username = os.environ.get("INSTA_USER")
password = os.environ.get("INSTA_PASS")
login = Login(firefox_browser)
login.login_me(username, password)