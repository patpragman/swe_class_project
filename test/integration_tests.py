"""
hacked togehter testing of post requests
"""

import json
import requests
from os import environ

url = environ['AWS_URL_ENDPOINT']

import os
import sys

"""
this horrifying call allows us to connect the "test" module to the App module.

The test module is in a different folder - specifically it's one up from where we normally run the application

os.path.abspath(__file__) gets the current file path
    os.path.dirname( moves up a directory
        then we do it again
            finally, we add this to the python path with sys.path.append

this is necessary if we want to keep our testing scripts separate from the scripts we use to run the code
"""
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))))

from lambda_functions.dev_post.model import FlashCard, User
from datetime import timedelta, datetime

# create a test user
test_user = User(
    username="patrick",
    password="pass_test"
)
obj = test_user.dict()
test_user_json = {"operation": "create_user",
                  "payload":
                      {"username": "test user",
                       "password": "Test",
                       "object": json.dumps(obj)
                       }
                  }
post_request = requests.post(url, json=test_user_json)
print(post_request)
print(post_request.text)
assert post_request.status_code == 200

test_card = FlashCard(
    owner="patrick",
    folder="test / not import",
    front_text="test_card_front",
    back_text="test_card_back",
    streak=0,
    create_date=datetime.utcnow() - timedelta(days=6),
    last_study_date=datetime.utcnow() - timedelta(days=5),
    next_study_due=datetime.utcnow() - timedelta(days=1)
)

obj = test_card.dict()
save_card_test_json = {
    "operation": "create_flashcard",
    "payload":
        {"username": "username",
         "password": "pass_test",
         "object": json.dumps(obj)
         }
}
post_request = requests.post(url, json=save_card_test_json)
print(post_request)
print(post_request.text)
assert post_request.status_code == 200
