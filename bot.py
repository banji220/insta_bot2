from time import sleep
from selenium import webdriver

firefox_browser = webdriver.Firefox()

firefox_browser.get("https://www.instagram.com/")
sleep(5)
firefox_browser.close()