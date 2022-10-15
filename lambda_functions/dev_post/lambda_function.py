import json



def create_flashcard(payload: dict) -> bool:
    """
    This function creates a new flashcard object by parsing a dictionary and saving it to s3

    :param payload: a dictionary containing the json from the client side
    :return: true if the operation was successful, false otherwise
    """

    return False # just returning false until we actually write the code to do this

def lambda_handler(event, context):
    '''Provide an event that contains the following keys:

      - operation: one of the operations in the operations dict below
      - payload: a parameter to pass to the operation being performed
    '''
    event = json.loads(event['body'])
    operation = event['operation']

    # define more operations in here - echo is the "hello world" of this sort of thing...
    operations = {
        'echo': lambda x: x,
        'create_flashcard': lambda payload: create_flashcard(payload)
    }

    if operation in operations:
        # a simple "200" request, but suffice it to say the operation worked.
        response = {
            "statusCode": 200,
            "body": "[]",
        }

        # get the result, stick that in "body"
        result = operations[operation](event.get('payload'))
        response['body'] = result
        # and send it back!
        return response
    else:
        # we can handle "bad operations" or something later
        raise ValueError('Unrecognized operation "{}"'.format(operation))