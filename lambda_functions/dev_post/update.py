import json
import boto3
from aws_config import STORAGE_BUCKET_NAME, REGION_NAME
from retrieve import get_all_cards_by_user_as_list


def update_card_by_id(payload: dict) -> dict:
    username = payload['username']
    card_id = payload['id']

    """Retrieves user's card_list, updates the card with matching id,
    
    and writes new card_list back to s3. Returns json containing the 
    updated card_list"""

    updated_card = payload['object']

    card_list = get_all_cards_by_user_as_list(username)

    try:
        match = False
        for (i, card) in enumerate(card_list):
            if int(card['id']) == card_id:
                match = True
                updated_card['id'] == card_id
                card_list[i] = updated_card
        if not match:
            raise IndexError
    except IndexError:

        return {'success': False,
                "return_payload": {
                    "message": 'card id does not exist in user card list', \
                    'objects': card_list}}

    # now we write card_list back to s3
    s3_client = boto3.resource("s3", region_name=REGION_NAME)
    s3_client.Bucket(STORAGE_BUCKET_NAME).put_object(Body=json.dumps(card_list), Key='card_list.json',
                                                     ContentType='json')

    return {'success': True,

            "return_payload":{
                'message': f"card {card_id} successfully updated", \
                'objects': card_list
                }
            }
