from time import sleep
from selenium import webdriver

firefox_browser = webdriver.Firefox()

firefox_browser.get("https://www.instagram.com/")

# Login
login_link = firefox_browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
login_link.click()

sleep(5)
firefox_browser.close()


