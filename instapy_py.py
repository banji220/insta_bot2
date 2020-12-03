import os
from typing import Counter
from instapy import InstaPy
from instapy import smart_run
import traceback


# My Instagram Username and Password
insta_user = os.environ.get('INSTA_USER')
insta_pass = os.environ.get('INSTA_PASS')

# Set my configuration and setting and authentication
def config_setting():
    session = InstaPy(username=insta_user, password=insta_pass, headless_browser=False, multi_logs=False,).login()
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
                session.set_relationship_bounds(enabled=True,
                                                potency_ratio=1.25,
                                                max_followers=2000,
                                                min_followers=1000,
                                                min_following=500)
                
                # Activity
                session.follow_by_tags(tags=["بورس"], amount=5)
                
            except Exception as e:
                print("Error")
follow()