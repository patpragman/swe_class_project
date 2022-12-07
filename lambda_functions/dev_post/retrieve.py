import json
import boto3
from aws_config import STORAGE_BUCKET_NAME, REGION_NAME

def get_max_id(operation: str) -> int:
    # retrieve information about the largest id for various objects
    print('operation:', operation)
    if operation == "user":
        print('getting maximum user id')
        users = get_all_users_as_list()
        print(users)
        if users:
            return max(int(user['id']) for user in users)
        else:
            return 0
    elif operation == "flashcard":
        cards = get_all_cards_as_list()

        if cards:
            return max(int(card['id']) for card in cards)
        else:
            return 0


def get_all_users_as_list() -> list:
    """
    connect to s3 and get the big list of json that contains all the user objects
    :return: big list of user objects as json
    """
    s3_client = boto3.resource("s3", region_name=REGION_NAME)
    response = s3_client.Object(STORAGE_BUCKET_NAME, "users.json").get()
    users = json.loads(response['Body'].read())
    return users

def get_all_cards_as_list() -> list:
    s3_client = boto3.resource("s3", region_name=REGION_NAME)
    response = s3_client.Object(STORAGE_BUCKET_NAME, "card_list.json").get()
    return json.loads(response['Body'].read())

def get_all_cards_by_user_as_list(username) -> list:
    return [card for card in get_all_cards_as_list() if card["owner"] == username]


def get_all_user_cards(payload) -> dict:
    username = payload['username']
    print('getting all cards for', username)

    cards = {"success": True,
             "return_payload": {
                 "message": f"fetched the following cards for {username}",
                 "objects": get_all_cards_by_user_as_list(username)
             }
             }
    return cards
