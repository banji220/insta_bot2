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

# Follow Users Based on Hashtag
def follow_hashtag_base():
    session = config_setting()
    
    with smart_run(session):
        counter = 0 
        while counter < 5:
            counter += 1
            
            try:
                # Setting 
                # potency_ratio == (followers count / following count)| eg. 5000(followers)/4000(following) == 1.25
                session.set_relationship_bounds(enabled=True,
                                                potency_ratio=None,
                                                delimit_by_numbers=True,
                                                max_followers=8000,
                                                min_followers=200,
                                                max_following=5000,
                                                min_following=100,
                                                )
                
                # Activity
                session.follow_by_tags(tags=["بورس"], amount=5)
                
            except Exception as e:
                print(traceback.format_exc())
# Unfollow Users
def unfollow():
    session = config_setting()
    
    with smart_run(session):
        try:
            # Setting
            session.set_relationship_bounds()
    
    
    
    
follow_hashtag_base()








# Document 
# `style`
# You can choose _unfollow style_ as `"FIFO"` (_First-Input-First-Output_) **OR** `"LIFO"` (_Last-Input-First-Output_) **OR** `"RANDOM"`.
# * with `"FIFO"`, it will unfollow users _in the **exact** order they are loaded_ (_`"FIFO"` is the default style unless you **change** it_);
# * with `"LIFO`" it will unfollow users _in the **reverse** order they were loaded_;
# * with `"RANDOM"` it will unfollow users _in the **shuffled** order_;