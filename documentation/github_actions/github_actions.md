# Github Actions

## WTF is a Github Action (gha)?

A Github action (henceforth gha) is a cool tool github provides to allow you to automate portions of
the development process.  A gha can do things like, run scripts on command, do linting or unit testing,
or automate your workflows.

## How do they work?

There's a folder in the repository called ".github/workflows" - the ghas live in there and are 'yaml'
scripts that are defined by github's easy to read and copious documentation.  Basically, they can be
set up to run when triggered or when certain events occur with your repository.

## Ok, so what do ours do?

In this repository, we have several ghas presently, the important ones are documented below.

### deploy.yml

deploy.yml deploys code on the master branch to production.  This script is triggered automatically
under two conditions.

if someone "pushes" to master (which shouldn't happen) or on a "pull request to master."

## deploy_to_test.yml

deploy_to_test.yml deploys code on the develop branch to the test environment.  This script is NOT
triggered automatically and must be run manually as a git hub action.

## discord_merge_to_master.yml

discord_merge_to_master.yml sends an alert whenever a pull request is initiated to the master branch.

## discord_push_to_dev_alert.yml

discord_push_to_dev_alert.yml sends an alert to the discord channel when someone pushes to dev or someone
initiates a pull request into the dev branch.

## push_to_dev.yml

push_to_dev.yml runs automatically when initiating a push to dev or a PR into dev.  It is the heart of
our deployment pipeline.  It takes newly commited code and makes sure it passes all of the tests
before deploying it into the develop enrvironment.  If "bad code" is getting into the master branc because of
poor testing this is where we stop it.  In the future we could add linting or style checking, but for
now this is the best we're going to do.

It performs the
following tasks:

1. it executes the python script test/integration_tests.py
2. it executes the python script test/unit_tests.py
3. it runs the script that deploys the work from the develop branch to the develop environment