import json
from create import create_flashcard, create_user, encrypt_password
from retrieve import get_all_users_as_list, get_all_user_cards
import boto3
from aws_config import REGION_NAME, STORAGE_BUCKET_NAME
from operation_router import retrieve_operation


def authenticate(payload: dict, operation) -> bool:
    """
    authenticate the payload and return true or false if the username and password match
    """
    username = payload['username']
    password = payload['password']
    operation = operation

    # we can always create a new user, go ahead and allow the script to work from there
    if operation == "create_user":
        return True
    else:
        # if you're doing anything else, verify credentials before continuing
        return verify_credentials(username, password)


def verify_credentials(username: str, password) -> bool:
    # separate function to connect to S3, pull the user file, and check to see if the username password combo matches
    s3 = boto3.resource("s3", region_name=REGION_NAME)
    print('verifying credentials')
    for user_obj in get_all_users_as_list():
        print(user_obj)
        stored_username = user_obj['username']
        stored_password = user_obj['password']

        if username == stored_username:
            if password == stored_password:
                return True

    return False


def lambda_handler(event, context):
    '''
    Provide an event that contains the following keys:
      - operation: one of the operations in the operations dict below
      - payload: a parameter to pass to the operation being performed
    '''

    response = {
        'statusCode': 500,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        "body": {
            "success": False,
            "return_payload": {}
        },
    }

    try:
        # we wrap all of this in a try/except block to catch any and all errors - no matter what we want to control
        # the output of the lambda function

        # try to build a response here

        event = json.loads(event['body'])

        operation = event['operation']
        payload = event.get('payload')
        payload = encrypt_password(payload)

        # first, authenticate the payload
        if authenticate(payload, operation):
            # check if this operation is supported, then run that operation
            print("retrieving result function")
            result_function = retrieve_operation(operation)
            response['statusCode'] = 200

            response['body'] = result_function(payload)
            if not response['body']['success']:
                # unrecognized api operation
                response['statusCode'] = 400

        else:
            response['statusCode'] = 404
            response['body']['return_payload']['message'] = 'unrecognized username or password'

        return response
    except Exception as err:
        """
        if any sort of error happened while doing this, let's send back a response that indicates that there was an
        internal server error
        """
        print(err)

        response = {"body": {
            "success": False,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            "return_payload": {
                "message": "unexplained server error"
            }
        }, 'statusCode': 500}

        response['body']['return_payload']['message'] = f"received the following error during operations: \n {str(err)}"

        return response
