from collections.abc import Callable
from create import create_flashcard, create_user
from retrieve import get_all_user_cards
from update import update_card_by_id


def retrieve_operation(operation: str):
    """
    takes an operation, finds the appropriate function for that operation, then returns
    :param operation: a str that tells this method what function to retrieve
    :return: the function to execute
    """

    unrecognized_payload = lambda x: {
        "success": False,
        "return_payload": {"message": f"the api operation '{operation}' unrecognized"}
    }
    # the wiring between operations and payloads lives in the "gross" list of if then statments below
    # I'd prefer a hash table, but this is probably more reasonable -pp
    print(f'getting result for operation \'{operation}\'')
    if operation == "get_cards":
        return lambda payload: get_all_user_cards(payload)
    elif operation == "create_flashcard":
        return lambda payload: create_flashcard(payload)  # return the create flashcard function
    elif operation == "create_user":
        return lambda payload: create_user(payload)
    elif operation == "update_card":
        return lambda payload: update_card_by_id(payload)
    elif operation == "echo":
        # this was the first thing we got AWS to do, let's leave it in here for the time being
        return lambda x: {"success": True, "return_payload": {"message": x} }

    else:
        return unrecognized_payload

