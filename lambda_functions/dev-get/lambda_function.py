import json


def lambda_handler(event, context):
    #  Code to serve the front end goes here
    return {
        'statusCode': 200,
        "headers": {'Content-Type': 'text/html'},
        'body': json.dumps('<h3>Here we go! Hello World!!! WOOO HOO!</h3>')
    }
