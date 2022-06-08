#!/bin/bash

source ./scripts/helpers.sh

# Check if virtualenv is installed
virtualenv --version > /dev/null 2>&1
if [[ $? -ne 0 ]]
then
    printf "\nPlease install virtualenv:\n[ https://virtualenv.pypa.io/en/latest/installation.html ]\n";
fi

if [[ ! -d "venv" ]]; then
    virtualenv -p python3 venv
fi

active_env

# Check if requirements exists
if [[ ! -f "requirements.txt" ]]; then
    echo "requirements.txt file does not exist.";
    exit 1;
fi
