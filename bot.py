import os
from time import sleep
from selenium import webdriver

firefox_browser = webdriver.Firefox()

firefox_browser.get("https://www.instagram.com/")




# Put Username and PassWord in their field
sleep(2)
username_input = firefox_browser.find_element_by_name("username")
password_input = firefox_browser.find_element_by_name("password")
USERNAME = os.environ.get("INSTA_USER")
PASSWORD = os.environ.get("INSTA_PASS")

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)


# Hit the Login button

login_button = firefox_browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()


sleep(5)
firefox_browser.close()

