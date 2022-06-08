#!/bin/bash

source ./scripts/helpers.sh

if [[ "$1" == "docker" ]]; then
    docker run -it -p 8000:80 $DOCKER_IMAGE:latest;
else
    active_env
    python src/run.py
fi
