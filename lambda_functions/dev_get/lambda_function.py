# notes:
# https://stackoverflow.com/questions/42194162/aws-api-gateway-return-binary-file-from-base64-browser-error


import json
from collections import defaultdict
import boto3
import base64

ENV = "dev"
SUPPORTED_IMAGE_FILETYPES = ["png", "jpeg", "jpg", "gif"]

# build a dictionary of HTTP headers
header_mapping = {"html": {'Content-Type': 'text/html'}}
for image_type in SUPPORTED_IMAGE_FILETYPES:
    header_mapping[image_type] = {'Content-Type': f'image/{"jpeg" if image_type == "jpg" else image_type}',
                                  'isBase64Encoded': True}


def fetch_object_from_s3(file_type, obj):
    """convert the object from s3 to the appropriate format to send in the json response"""

    if file_type in SUPPORTED_IMAGE_FILETYPES:
        image = obj.get()['Body'].read()
        content = base64.b64encode(image).decode("utf-8")
    else:
        content = obj.get()['Body'].read().decode('utf-8')

    return content


def lambda_handler(event, context):
    #  Code to serve the front end goes here

    # this just goes to s3, and sends the main page for now, something more complicated might come along later
    # we'll need it to process the get request and send the appropriate files from the s3 bucket

    s3_client = boto3.resource("s3", region_name="us-west-2")
    bucket_name = f"swe.class.project.{ENV}"
    selected_bucket = s3_client.Bucket(bucket_name)


    # so honestly, this just fetches one page... that's the only thing it does naturally more to come

    # need to figure out how to use the AWS event coming from the api gateway to fetch specific pages...
    get_params = event["queryStringParameters"]
    api_return_datatype = get_params['type']
    api_file_path = get_params['path']
    header = header_mapping[api_return_datatype]

    try:
        # so honestly, this just fetches one page... that's the only thing it does naturally more to come
        obj = s3_client.Object(bucket_name, f"{api_file_path}")
        return {
            'statusCode': 200,
            "headers": header,
            'body': fetch_object_from_s3(api_return_datatype, obj)
        }
    except Exception as err:
        # absurdly (and overly broad) exception class...
        obj = s3_client.Object(bucket_name, f"/fnf.html")
        content = obj.get()['Body'].read().decode('utf-8')
        return {
            'statusCode': 404,
            "headers": {'Content-Type': 'text/html'},
            'body': str(err)
        }