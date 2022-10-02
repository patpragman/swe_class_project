"""
This code is a series of functions to push code and content to AWS

"""

import boto3
import os
import pathlib


def file_type_mapping(suffix) -> str:
    # we need this function to map the file suffix to the appropriate HTTP response header in s3

    suffix = suffix.replace(".", "")
    if suffix == "html":
        return 'text/html'
    elif suffix == "jpg" or suffix == "jpeg":
        return "image/jpeg"
    elif suffix == "png":
        return "image/png"
    else:
        return "text/plain"


def update_api(lambda_function_endpoints=["post",], env="dev"):
    """
    This code updates the api by spooling up a lambda client, then for each end point selected
    uploading the associated zip file.

    notes.  The zip files have to have a specific format "deployment_package_<type of api action>.zip"
    we could probably make this more generalized later, refactor if necessary


    :param lambda_function_endpoints: the api endpoint names - for instance, <env>-post or somethign
    :param env: the other half of the api endpoint name
    :return: None - it just does it's work and then dies
    """
    lambda_client = boto3.client("lambda")
    for lambda_function_endpoint in lambda_function_endpoints:
        # iterate through post and get and update the lambda functions that handle posts and get requests on aws
        with open(f"deployment_package_{lambda_function_endpoint}.zip", "rb") as zipfile:
            lambda_client.update_function_code(
                FunctionName=f'{env}-{lambda_function_endpoint}',
                ZipFile=zipfile.read()
            )


def update_web_content(folderpath="web_content", env="dev"):
    """
    This code takes all the content of the web content folder, and uploads it to the applicable S3 bucket
    path and all
    :param folderpath: this is the path from the root directory in the repo where the static html is stored.
    :param path: the name of the folder or path to the folder containing the web content.
    :param env: the env referenced in the bucket, such as swe.class.project.dev or something similar
    :return: None - it does it's work then quietly dies.
    """

    s3_client = boto3.resource("s3", region_name="us-west-2")
    bucket_name = f"swe.class.project.{env}"
    selected_bucket = s3_client.Bucket(bucket_name)

    # this code modified from stack exchange, but yeah, walk through directories and create folders as required
    for path, subdirs, files in os.walk(folderpath):
        # path = path.replace("\\", "/")
        # directory_name = path.replace(path, "")
        for file in files:
            file_location = os.path.join(path, file)
            suffix = pathlib.Path(file_location).suffix
            selected_bucket.upload_file(file_location, file, ExtraArgs={'ContentType': file_type_mapping(suffix)})


if __name__ == "__main__":
    update_web_content()

