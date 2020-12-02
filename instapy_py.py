import os
from instapy import InstaPy

username = os.environ.get("INSTA_USER")
password = os.environ.get("INSTA_PASS")
instagram_credentials = InstaPy(username, password).login()
