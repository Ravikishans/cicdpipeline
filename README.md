crontask.sh: A shell script that is run periodically using cron.
deploy.sh: A shell script for deploying the project.
newcmits.py: The main Python script for the project.


Setup--

Clone the repository.
Replace the placeholder GitHub token in newcmits.py with your actual GitHub token. Alternatively, you can set your GitHub token as an environment variable in your shell.
Modify the repo_name variable in newcmits.py to match the name of the repository you want to work with.
Run crontask.sh to run the script. You can also add it to your crontab using crontab -e to run it periodically.

Running the project

After setting up the project, you can run it using the crontask.sh script.
