import json
import boto3
from aws_config import STORAGE_BUCKET_NAME, REGION_NAME
from retrieve import get_all_cards_as_list


def delete_item_by_id(type_of_item, id) -> dict:
    if type_of_item == "flashcard":
        cards = get_all_cards_as_list()

        while cards:
            card = cards.pop()
            if int(card['id']) == int(id):
                return {"success": True,
                        "return_payload": {
                            "message": f"deleted the following_card",
                            "object": card
                        }
                        }

        return {"success": False,
                "return_payload": {
                    "message": f"unable to fetch card id",
                    "object": []
                }
                }
