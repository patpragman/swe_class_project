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


if __name__ == "__main__":
    """
    check that the classes we want to use import at all... if they don't import there's a decent chance
    things are broken...
    """
    print("starting unit tests...")

    # let's import Flashcard class and test it
    from lambda_functions.dev_post.model import run_flashcard_tests
    from datetime import datetime, timedelta

    # put all your tests below - they'll be actuated during automated testing
    run_flashcard_tests()
    print("unit tests complete - pass!")
