#!/bin/bash

DIR=$(dirname "$0")
echo "$DIR"

# Specify the full paths to the Python interpreter and the pip command
PYTHON=$DIR/myenv/bin/python3
PIP=$DIR/myenv/bin/pip3

# Create the virtual environment
python3 -m venv myenv

# Activate the virtual environment and run the commands that need to be run in it
(
    source myenv/bin/activate
    $PIP install PyGithub
    $PYTHON /home/ravikishans/cicdpipeline/newcmits.py
)
