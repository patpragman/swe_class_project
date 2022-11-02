import json
import boto3
from aws_config import STORAGE_BUCKET_NAME, REGION_NAME
from retrieve import get_all_cards_as_list


def delete_item_by_id(type_of_item, id) -> dict:

    if type_of_item == "flashcard":

        card_list = get_all_cards_as_list()

        try:
            match = False
            for (i, card) in enumerate(card_list):
                if int(card['id']) == id:
                    match = True
                    card_list.pop(i)
            if not match:
                raise IndexError
        except IndexError('card id not found'):
            return {'success': False, \
            "message": 'card id does not exist in user card list', \
                'objects': card_list}

        # now we write card_list back to s3
        s3_client = boto3.resource("s3", region_name=REGION_NAME)
        s3_client.Bucket(STORAGE_BUCKET_NAME).put_object(Body=json.dumps(card_list), Key='card_list.json',
                                                    ContentType='json')
        # return success code
        return {'success': True, \
            'message': f"card {id} successfully updated", \
                'objects': card_list}


    # branch for user deletion
    return {"success": False,
            "return_payload": {
                "message": f"unable to fetch card id",
                "object": []
            }
            }
