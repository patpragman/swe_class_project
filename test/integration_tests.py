"""
hacked togehter testing of post requests
"""

import json
import requests
from os import environ

url = environ['AWS_URL_ENDPOINT']

test_code = {"key1": "value1",
             "key2": "value2",
             "key3": "value3",
             "operation": "create_flashcard",
             "payload": "test!"
             }

# testing the response codes for various operations
test_operations = ["create_flashcard",
                   "echo",
                   "bad_payload!"]
desired_responses = [
    200, 200, 400
]
desired_api_state = [
    False,
    True,
    False
]
desired_return_msg_contains = [
    "unable to create",
    "test!",
    "not recognized"
]

try:
    for k, v, d, m in list(zip(test_operations, desired_responses, desired_api_state, desired_return_msg_contains)):
        test_code["operation"] = k

        post_request = requests.post(url, json=test_code)
        assert post_request.status_code == v
        response_data = json.loads(post_request.text)
        assert response_data['success'] == d
        assert m in str(response_data['return_payload']['message'])
except AssertionError as err:
    print(err)
    print(k, v)

# make a test flashcard
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

from lambda_functions.dev_post.model import FlashCard
from datetime import timedelta, datetime

test_card = FlashCard(
    folder="test / not import",
    front_text="test_card_front",
    back_text="test_card_back",
    streak=0,
    create_date=datetime.utcnow() - timedelta(days=6),
    last_study_date=datetime.utcnow() - timedelta(days=5),
    next_study_due=datetime.utcnow() - timedelta(days=1)
)

obj = test_card.dict()
save_card_test_json = {"operation": "create_flashcard",
                       "payload":
                           {"username": "Test",
                            "password": "Test",
                            "object": json.dumps(obj)
                            }
                       }
post_request = requests.post(url, json=save_card_test_json)
print(post_request)
print(post_request.text)
assert post_request.status_code == 200
