#!/bin/bash

source ./scripts/helpers.sh

if [ ! -f "requirements.txt" ]; then
  generate_requirements
fi

docker build -t $DOCKER_IMAGE:latest .
