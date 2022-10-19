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
        {"username": "patrick",
         "password": "pass_test",
         "object": json.dumps(obj)
         }
}
post_request = requests.post(url, json=save_card_test_json)
print(post_request)
print(post_request.text)
assert post_request.status_code == 200

# now create 10 test cards
for i in range(0, 10):
    owner = 'patrick' if i % 2 == 0 else "not"
    test_card = FlashCard(
        owner=owner,
        folder="testing",
        front_text=f"test_card_front_{i}",
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
            {"username": "patrick",
             "password": "pass_test",
             "object": json.dumps(obj)
             }
    }
    post_request = requests.post(url, json=save_card_test_json)
    assert post_request.status_code == 200

get_cards_test_json = {
    "operation": "get_cards",
    "payload":{
        "username": "patrick",
        "password": "pass_test",
    }
}

post_request = requests.post(url, json=get_cards_test_json)
assert post_request.status_code == 200
response = post_request.json()
return_payload = response['return_payload']
for obj in return_payload['objects']:
    print(obj)