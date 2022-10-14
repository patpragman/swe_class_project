import json
import requests
from os import environ

url = environ['AWS_URL_ENDPOINT']
print(url)
test_code = {"key1": "value1",
             "key2": "value2",
             "key3": "value3",
             "operation": "sayhello",
             "payload": "patpatpatpatpat!"
             }

x = requests.post(url, json=test_code)

print(x, x.text)
