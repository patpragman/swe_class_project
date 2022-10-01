"""
script for deployment of code to production (that's stuff in the master branch)
"""
import os
import sys
import argparse
import boto3
from upload import update_api, update_web_content
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
parser = argparse.ArgumentParser()
parser.add_argument("--to_env", type=str, default="develop")
parser.add_argument("--from_branch", type=str, default="develop")




if __name__ == "__main__":
    args = parser.parse_args()
    from_branch = args.from_branch
    target_env = args.to_env

    print(f"Attempting to deploy code from the {from_branch} branch to the {target_env} environment.")

    """
    this is where we package the code to deploy to the various AWS services we're using
    """

    if target_env == "develop":
        # if you're deploying to the dev facing environment
        update_api(env="dev")
        update_web_content(env="dev")
    else:
        print('deployment to test and prod not set up yet')
