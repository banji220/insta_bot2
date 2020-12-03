import os
from typing import Counter
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

# Set my configuration and setting and authentication
def config_setting():
    session = InstaPy(username=insta_user, password=insta_pass, headless_browser=False, nogui=True, multi_logs=False)
    return session

# Follow Users
def follow():
    session = config_setting()
    
    with smart_run(session):
        counter = 0 
        while counter < 5:
            counter += 1
            
            try:
                # Setting 
                # potency_ratio == (followers count / following count)| eg. 5000(followers)/4000(following) == 1.25
                session.set_relationship_bounds(enabled=True, potency_ratio=1.25)