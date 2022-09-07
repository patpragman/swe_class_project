"""
unit test for all the appropriate classes in the app go here
"""
import sys


"""
check that the classes we want to use import at all... if they don't import there's a decent chance
things are broken...
"""
from App.controller import Controller
from App.view import View
from App.model import Model

if __name__ == "__main__":

    desired_imports = ['App.model', 'App.view', 'App.controller']  # terrible...
    for module_name in desired_imports:
        assert module_name in sys.modules
