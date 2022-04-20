#!/usr/bin/env bash
set +e

dockerAccount='dockerjeffery'
imageName='chatbot'
PACKAGE_VERSION='test'

echo docker build -t "$imageName":"$PACKAGE_VERSION" .
docker build -t "$imageName":"$PACKAGE_VERSION" .

echo run docker container
docker run -it --rm -v "$(pwd)/config.ini:/app/config.ini"  --name test_chatbot "$imageName":"$PACKAGE_VERSION"