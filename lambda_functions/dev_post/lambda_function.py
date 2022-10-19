import json
from create import create_flashcard, create_user


def authenticate(payload: dict) -> bool:
    """
    authenticate the payload and return true or false if the username and password match
    """



    return True # for now just return true


def validate_login(username: str, password) -> bool:

    pass



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
            lambda payload: create_flashcard(payload),  # creates a flashcard and sends back confirmation
        'create_user':
            lambda payload: create_user(payload)
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
