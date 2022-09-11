"""
unit test for all the appropriate classes in the app go here
"""
import os
import sys
"""
this horrifying call allows us to connect the "test" module to the App module.

The test module is in a different folder - specifically it's one up from where we normally run the application

os.path.abspath(__file__) gets the current file path
    os.path.dirname( moves up a directory
        then we do it again
            finally, we add this to the python path with sys.path.append

this is necessary if we want to keep our testing scripts separate from the scripts we use to run the code
"""
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__))))


print("starting unit tests...")
if __name__ == "__main__":
    """
    check that the classes we want to use import at all... if they don't import there's a decent chance
    things are broken...
    """
    from App.controller import Controller
    from App.view import View
    from App.model import Model

    desired_imports = ['App.model', 'App.view', 'App.controller']  # terrible...
    for module_name in desired_imports:
        assert module_name in sys.modules


    # let's import Flashcard class and test it
    from App.model import FlashCard
    from datetime import datetime, timedelta

    test_card = FlashCard(
        folder="test / not import",
        front_text="test_card_front",
        back_text="test_card_back",
        streak=0,
        create_date=datetime.utcnow() - timedelta(days=6),
        last_study_date=datetime.utcnow() - timedelta(days=5),
        next_study_due=datetime.utcnow() - timedelta(days=1)
    )
    assert test_card.unit_test()
    # now delete the object
    del test_card

    print("unit tests complete - pass!")
