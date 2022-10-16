"""
This file contains the code that can create any objects that get stored on S3

"""

import json
import boto3
import botocore


def create_user(payload: dict) -> dict:
    pass

def create_folder(payload: dict) -> dict:
    pass


def create_flashcard(payload: dict) -> dict:
    """
    This function creates a new flashcard object by parsing a dictionary and saving it to s3

    :param payload: a dictionary containing the json from the client side
    :return: a dictionary with the following keys:
            {"success": True or false depending on if it worked or not,
            "return_payload": the data the server is going to send back
            }
    """

    s3_client = boto3.resource("s3", region_name="us-west-2")
    """"
    the client is the tool that we use to talk to s3 - the region name is where our data lives presently...
    it's in portland oregon
    """
    bucket_name = f"swe.class.project.storage"  # this is the name of the folder where all our data lives

    # first try and load the master flashcard list
    try:
        response = s3_client.Object(bucket_name, "card_list.json").get()
        card_list = json.loads(response['Body'].read())

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            # the object doesn't exist, we'll make an empty card list
            card_list = []
        else:
            # Something else unpredictable has happened...
            print(e)
            raise Exception(str(e))
    else:
        # The card_list does exist, so let's go ahead and append a card to it.
        pass

    # get an object from the payload, then append it to the card list
    card = json.loads(payload['object'])  # right now this is just raw json, we may want to consider validation here
    card_list.append(card)

    # now try to save the card
    try:
        # you can drop the card_list into the s3 bucket with the following function
        s3_client.Bucket(bucket_name).put_object(Body=json.dumps(card_list), Key='card_list.json', ContentType='json')

        return {"success": True,
                "return_payload": {
                    "message": "card saved!"
                    }
                }

    except botocore.exceptions.ClientError:
        # if we got a client error, send that back with the appropriate return payload, etc.
        return {"success": False,
                "return_payload": {
                    "message": "we received your card, but there was an error and it did not save."
                    }
                }
