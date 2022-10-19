import boto3
import json

if __name__ == "__main__":
    s3_client = boto3.resource("s3", region_name="us-west-2")

    s3_client.Bucket("swe.class.project.storage").put_object(Body=json.dumps([]), Key="users.json",
                                                     ContentType='json')

    s3_client.Bucket("swe.class.project.storage").put_object(Body=json.dumps([]), Key="card_list.json",
                                                             ContentType='json')