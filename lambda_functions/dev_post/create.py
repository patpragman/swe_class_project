"""
This file contains the code that can create any objects that get stored on S3

"""

import json
import boto3
import botocore

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
    "user": lambda payload: validate_user(payload),
    "flashcard": lambda payload: validate_flashcard(payload)

}

def validate_user(payload: dict) -> dict:
    # not implemented yet

    return payload

def validate_flashcard(payload: dict) -> dict:
    # we need to make sure the data coming at least has the keys in the data model
    try:

        # not implemented
        return payload
    except Exception as err:
        print(err)
        raise Exception('Data improperly formatted')



def create(payload: dict, operation: str) -> dict:


    s3_client = boto3.resource("s3", region_name=REGION_NAME)

    # we do our data validation here:
    VALIDATION_MAPPING(operation)


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
        object_list.append(obj)

        # now try to save the object
        try:
            # you can drop the card_list into the s3 bucket with the following function
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

