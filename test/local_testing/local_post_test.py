"""
hacked togehter local post request testing script to test the lambda function

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

try:
    for k, v, d in list(zip(test_operations, desired_responses, desired_api_state)):
        test_code["operation"] = k

        post_request = requests.post(url, json=test_code)
        assert post_request.status_code == v
        response_data = json.loads(post_request.text)
        assert response_data['success'] == d
except AssertionError as err:
    print(err)
    print(k, v)

