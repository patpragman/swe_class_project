import json



def create_flashcard(payload: dict) -> dict:
    """
    This function creates a new flashcard object by parsing a dictionary and saving it to s3

    :param payload: a dictionary containing the json from the client side
    :return: a dictionary with the following keys:
            {"success": True or false depending on if it worked or not,
            "return_payload": the data the server is going to send back
            }
    """

    return {"success": False,
            "return_payload": {}  # empty dictionary for now
            }  # just returning false until we actually write the code to do this


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
    except Exception as err:
        """
        if any sort of error happened while doing this, let's send back a response that indicates that there was an
        internal server error
        """
        response['statusCode'] = 500
        response['body']['return_payload']['message'] = f"received the following error during operations: \n {str(err)}"

    return response
