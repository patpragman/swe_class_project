"""
script for deployment of code to production (that's stuff in the master branch)
"""
import os
import sys
"""
this horrifying call allows us to connect the "deployment" module to all the other modules we could
conceivably need - this is similar to what's in the unit_tests.py script for a reason, we want code
hiding in this directory to be able to be able to see all the other modules etc.

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

"""
code to deploy the application goes below here:
"""
print("Nothing has been set up yet!")
