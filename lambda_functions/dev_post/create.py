"""
This file contains the code that can create any objects that get stored on S3

"""

import json
import boto3
import botocore
import hashlib

STORAGE_BUCKET_NAME = f"swe.class.project.storage"
REGION_NAME = 'us-west-2'


"""
this is a mapping used in this script to map operation types to a filename in S3
"""
FILE_MAPPING = {
    "user": 'users.json',
    'flashcard': 'card_list.json'
}


VALIDATION_MAPPING = {
    "user": lambda payload: encrypt_password(payload),
    "flashcard": lambda payload: validate_flashcard(payload)
}

def encrypt_password(payload: dict) -> dict:
    # we need to encrypt the user password so we're not storing anything in our database in plain text

    # the payload has a 'password' key - before we put it into the dictionary, we should hash it so we're
    # not storing passwords in plain text
    print(payload)
    payload['password'] = hashlib.sha1(bytes(payload['password'], 'utf-8')).hexdigest()
    return payload

def validate_flashcard(obj: dict) -> dict:
    # we need to make sure the data coming at least has the keys in the data model
    try:

        # not implemented
        return obj
    except Exception as err:
        print(err)
        raise Exception('Data improperly formatted')



def create(payload: dict, operation: str) -> dict:

    s3_client = boto3.resource("s3", region_name=REGION_NAME)
    try:
        response = s3_client.Object(STORAGE_BUCKET_NAME, FILE_MAPPING[operation]).get()
        object_list = json.loads(response['Body'].read())

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            # the object doesn't exist, we'll make an empty card list
            object_list = []
        else:
            # Something else unpredictable has happened...
            print(e)
            raise Exception(str(e))
    finally:
        # The card_list does exist, so let's go ahead and append a card to it.

        # get an object from the payload, then append it to the card list
        obj = json.loads(payload['object'])  # right now this is just raw json, we may want to consider validation here
        obj = VALIDATION_MAPPING[operation](obj)  # validation of objects happens here
        object_list.append(obj)

        # now try to save the object
        try:
            # you can drop the object into the s3 bucket with the following function

            s3_client.Bucket(STORAGE_BUCKET_NAME).put_object(Body=json.dumps(object_list), Key=FILE_MAPPING[operation],
                                                    ContentType='json')

            return {"success": True,
                    "return_payload": {
                        "message": f"{operation} saved!"
                    }
                    }

        except botocore.exceptions.ClientError:
            # if we got a client error, send that back with the appropriate return payload, etc.
            return {"success": False,
                    "return_payload": {
                        "message": f"we received your {operation}, but there was an error and it did not save."
                    }
                    }


def create_user(payload: dict) -> dict:
    return create(payload=payload, operation="user")

def create_flashcard(payload: dict) -> dict:
    return create(payload=payload, operation="flashcard")


def create_folder(payload: dict) -> dict:
    pass

