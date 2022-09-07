"""
unit tests for all the appropriate classes in the app go here
"""
import sys
import os

print("Running Unit Tests!")
print('running from:')

# check that the app module imports at all
from app.model import Model
from app.view import View
from app.controller import Controller

for file_name in os.listdir(f"{os.getcwd()}/app"):
    module_name = f"app.{file_name.replace('.py', '')}"
    if "__" not in file_name:
        assert module_name in sys.modules
