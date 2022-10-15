import json
import requests
from os import environ

url = environ['AWS_URL_ENDPOINT']
print(url)
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
for k,v in zip(test_operations):
    test_code["operation"] = k
    post_request = requests.post(url, json=test_code)
    print(post_request.request)
    print(post_request.text)

