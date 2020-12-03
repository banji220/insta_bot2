import os
from instapy import InstaPy
from instapy import smart_run
from selenium import webdriver
import time
from datetime import datetime
import schedule
import traceback
import requests

# My Instagram Username and Password
insta_user = os.environ.get('INSTA_USER')
insta_pass = os.environ.get('INST_PASS')
def start_session():
    config_setting = InstaPy(username=insta_user, password=insta_pass, headless_browser=False, nogui=True, multi_logs=False)
    return config_setting