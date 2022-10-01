#!/bin/bash
# Package for Deployment!
# Generate a Zip File of the post lambda functions

mkdir "deployment_package"

# copy all the lambda functions into the deployment package
cp -r lambda_functions/dev_post/* "deployment_package"
# build a venv of all the tools we need
cd deployment_package
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

# zip up the packages you'll need for the lambda
cd venv/lib/python3.10/site-packages
zip -r ../../../../../deployment_package_post.zip .
cd ../../../../  # cd back to the working directory
# now remove the venv - we don't need to package that up
rm -rf venv

# now package everything in the dev_post folder by zipping it up
zip -g ../deployment_package_post.zip *
cd ..
rm -rf deployment_package

