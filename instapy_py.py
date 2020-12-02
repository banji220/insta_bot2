import os
from instapy import InstaPy

username = os.environ.get("INSTA_USER")
password = os.environ.get("INSTA_PASS")
my_account = InstaPy(username, password)
my_account.login()
my_account.like_by_tags(["BeatBox"], amount=5)