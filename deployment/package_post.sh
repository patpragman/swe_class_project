#!/bin/bash
# Package for Deployment!
# Generate a Zip File of the post lambda functions

mkdir "deployment_package"

# copy all the lambda functions into the deployment package
cp lambda_functions/dev-post/* "deployment_package"
# build a venv of all the tools we need
cd deployment_package
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

# zip up the packages you'll need for the lambda
cd venv/lib/python3.10/site-packages
zip -r ../../../../../deployment_package_post.zip .
cd ../../../../
zip -g ../deployment_package_post.zip lambda_function.py
cd ..
rm -rf deployment_package

