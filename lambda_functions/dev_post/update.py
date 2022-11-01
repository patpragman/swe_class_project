import json
import boto3
from aws_config import STORAGE_BUCKET_NAME, REGION_NAME
from retrieve import get_all_cards_by_user_as_list


def update_card_by_id(payload: dict) -> dict:
    username = payload['username']
    card_id = payload['id']

    """
    this isn't implemented yet
    
    we need to take an id number
    update that card with the changes
    then return the all the new cards back to the client
    """

    return {"success": False,
            "return_payload": {
                "message": f"not implemented yet",
                "objects": get_all_cards_by_user_as_list(username)
            }
            }
