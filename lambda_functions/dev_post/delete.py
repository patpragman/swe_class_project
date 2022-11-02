import json
import boto3
from aws_config import STORAGE_BUCKET_NAME, REGION_NAME
from retrieve import get_all_cards_as_list, get_all_users_as_list


def delete_flashcard(payload) -> dict:

    # read card id from payload
    id = int(payload['id'])

    # check card list for matching id and pop
    card_list = get_all_cards_as_list()
    try:
        match = False
        for (i, card) in enumerate(card_list):
            if card['id'] == id:
                match = True
                card_list.pop(i)
        if not match:
            raise IndexError
    except IndexError('card id not found'):
        return {'success': False, \
        "message": f"unable to find card with matching id {id}", \
            'objects': card_list}

    # write card_list back to s3
    s3_client = boto3.resource("s3", region_name=REGION_NAME)
    s3_client.Bucket(STORAGE_BUCKET_NAME).put_object(Body=json.dumps(card_list), Key='card_list.json',
                                                ContentType='json')
    # return success code
    return {'success': True, \
        'message': f"card {id} successfully deleted", \
            'objects': card_list}


def delete_user(payload):

    # get username from payload
    username = payload['username']

    # double check user exists
    user_list = get_all_users_as_list()
    user_idx = 0
    exists = False
    for (i, user) in enumerate(user_list):
        if user['username'] == username:
            exists = True
            user_idx = i

    if not exists:
        raise Exception('no user with matching id found')

    # if user exists, delete all that user's cards
    original_card_list = get_all_cards_as_list()
    new_card_list = []
    while original_card_list:
        card = original_card_list.pop()
        if card['owner'] == username:
            continue
        else:
            new_card_list.append(card)

    # write the new_card_list back to s3
    s3_client = boto3.resource("s3", region_name=REGION_NAME)
    s3_client.Bucket(STORAGE_BUCKET_NAME).put_object(Body=json.dumps(new_card_list), Key='card_list.json',
                                                    ContentType='json')

    # delete user
    user_list.pop(user_idx)

    # write user_list back to s3
    s3_client = boto3.resource("s3", region_name=REGION_NAME)
    s3_client.Bucket(STORAGE_BUCKET_NAME).put_object(Body=json.dumps(user_list), Key='user_list.json',
                                                ContentType='json')
    # return success code
    return {'success': True, \
        'message': f"user {username} successfully deleted. {cards_deleted} cards were removed.", \
            'objects': user_list}

    

        



        
            



