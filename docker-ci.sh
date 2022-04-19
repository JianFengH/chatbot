#!/usr/bin/env bash
set +e

dockerAccount='dockerjeffery'
imageName='chatbot'
PACKAGE_VERSION='latest'

echo docker build -t "$imageName":"$PACKAGE_VERSION" .
docker build -t "$imageName":"$PACKAGE_VERSION" .

echo docker tag "$imageName":"$PACKAGE_VERSION" "$dockerAccount"/"$imageName":"$PACKAGE_VERSION"
docker tag "$imageName":"$PACKAGE_VERSION" "$dockerAccount"/"$imageName":"$PACKAGE_VERSION"

echo docker push "$dockerAccount"/"$imageName":"$PACKAGE_VERSION"
docker push "$dockerAccount"/"$imageName":"$PACKAGE_VERSION"
