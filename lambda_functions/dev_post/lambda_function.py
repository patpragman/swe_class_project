import json
import boto3
import botocore

def authenticate(payload: dict) -> bool:
    """
    authenticate the payload and return true or false if the username and password match
    """
    return True # for now just return true


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
    bucket_name = f"swe.class.project.storage"

    # first try and load the master flashcard list
    try:
        card_list = s3_client.Object(bucket_name, "card_list.json").load()
    except botocore.exceptions.ClientError as e:
        print(e)
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
    card = json.loads(payload['object'])
    card_list.append(card)

    # now try to save the card
    try:
        # put an object
        s3_client.Bucket(bucket_name).put_object(Body=json.dumps(card_list), Key='card_list.json', ContentType='json')

        return {"success": True,
                "return_payload": {
                    "message": "card saved!"
                    }
                }

    except botocore.exceptions.ClientError:
        return {"success": False,
                "return_payload": {
                    "message": "we received your card, but there was an error and it did not save."
                    }
                }


def lambda_handler(event, context):
    '''
    Provide an event that contains the following keys:
      - operation: one of the operations in the operations dict below
      - payload: a parameter to pass to the operation being performed
    '''

    response = {
        "statusCode": 500,  # start with the assumption that we broke something
        "body": {
            "success": False,
            "return_payload": {
                "message": "unexplained server error"
            }
        },
    }

    # this code is the wiring between the json sent as post request and the functions we have in our app that does stuff
    operations = {
        'echo': lambda x: {"success": True,
                           "return_payload": {"message": x}
                           },  # echos back literally all data you send
        'create_flashcard':
            lambda payload: create_flashcard(payload)  # creates a flashcard and sends back confirmation
    }

    try:
        # we wrap all of this in a try/except block to catch any and all errors - no matter what we want to control
        # the output of the lambda function
        event = json.loads(event['body'])
        operation = event['operation']

        # first, authenticate the payload
        if authenticate(event.get("payload")):
            # check if this operation is supported, then run the operation
            if operation in operations:
                # a simple "200" request, but suffice it to say the operation worked.
                response['statusCode'] = 200

                # get the result, stick that in "body"
                result = operations[operation](event.get('payload'))
                response['body'] = result
            else:
                response['statusCode'] = 400
                response['body']['return_payload']['message'] = f"the api operation: {operation} is not recognized"
        else:
            response['statusCode'] = 404
            response['body']['return_payload']['message'] = 'unrecognized username or password'
    except Exception as err:
        """
        if any sort of error happened while doing this, let's send back a response that indicates that there was an
        internal server error
        """
        response['statusCode'] = 500
        response['body']['return_payload']['message'] = f"received the following error during operations: \n {str(err)}"

    return response
