import json
import boto3
ENV = "dev"
def lambda_handler(event, context):
    #  Code to serve the front end goes here

    # this just goes to s3, and sends the main page for now, something more complicated might come along later
    # we'll need it to process the get request and send the appropriate files from the s3 bucket

    s3_client = boto3.resource("s3", region_name="us-west-2")
    bucket_name = f"swe.class.project.{ENV}"
    selected_bucket = s3_client.Bucket(bucket_name)

    # so honestly, this just fetches one page... that's the only thing it does naturally more to come
    obj = s3_client.Object(bucket_name, "/main.html")
    content = obj.get()['Body'].read().decode('utf-8')

    return {
        'statusCode': 200,
        "headers": {'Content-Type': 'text/html'},
        'body': json.dumps(content)
    }