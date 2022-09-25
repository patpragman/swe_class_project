import json


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