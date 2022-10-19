import json
import boto3
from create import STORAGE_BUCKET_NAME, REGION_NAME

def get_all_users_as_json() -> list:
    """
    connect to s3 and get the big list of json that contains all the user objects
    :return: big list of user objects
    """
    s3_client = boto3.resource("s3", region_name=REGION_NAME)
    response = s3_client.Object(STORAGE_BUCKET_NAME, "users.json").get()
    users = json.loads(response['Body'].read())
    return users

