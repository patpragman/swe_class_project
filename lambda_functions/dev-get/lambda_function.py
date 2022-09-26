import json


def lambda_handler(event, context):
    #  Code to serve the front end goes here

    # a request for "home" or to initially load the app comes in, and we send back HTML files form S3 that have
    # the website in them


    return {
        'statusCode': 200,
        "headers": {'Content-Type': 'text/html'},
        'body': json.dumps('<h3>Here we go! Hello World!!! WOOO HOO! Welcome!</h3>')
    }
