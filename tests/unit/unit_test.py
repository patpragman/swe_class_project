"""
unit tests for all the appropriate classes in the app go here
"""
import sys
import os

print("Running Unit Tests!")
print('running from:')
print(os.getcwd())
# check that the app module imports at all
import app
assert "app" in sys.modules