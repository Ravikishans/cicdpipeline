# CI-CD Pipeline Tool

## Introduction

This repository provides a step-by-step guide to setting up a CI-CD pipeline tool. The tool will automate the process of checking for new commits, deploying code to an NGINX server, and ensuring changes are reflected in production.

## Task 1: Create index.html

Create the `index.html` file at the following location:
```
~/CICDPipeline-html/index.html
```

## Task 2: Install NGINX

1. Update and upgrade your package lists:
    ```sh
    sudo apt-get update
    sudo apt-get upgrade
    ```
2. Install NGINX:
    ```sh
    sudo apt-get install nginx
    ```
3. Check the status of NGINX to ensure it's running:
    ```sh
    sudo service nginx status
    ```
   The status should be `active (running)`.

## Task 3: Python Script to Check for New Commits

The `newcmits.py` script tracks new commits made in a GitHub repository using the GitHub API.

## Task 4: Bash Script to Deploy the Code

The `deploy.sh` script copies the latest `index.html` file from the GitHub repository to the NGINX server's web directory to deploy changes to production.

## Task 5: Cron Job to Run the Python Script

To run the Python script periodically, set up a cron job:

1. Open the crontab editor:
    ```sh
    crontab -e
    ```
2. Add the following line to execute `crontask.sh` every minute and log the output to `py_log.txt`:
    ```sh
    * * * * * /usr/bin/bash /home/ubuntu/cicdpipeline/crontask.sh >> /home/ubuntu/cicdpipeline/py_log.txt 2>&1
    ```

## Task 6: Push a Change to index.html

Push a change to `index.html`. This action should trigger the Python script to track the changes and deploy the updated `index.html` to the NGINX server, reflecting the changes in production.
