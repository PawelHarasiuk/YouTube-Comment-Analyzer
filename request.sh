#!/bin/bash
URL=$1
curl -sX POST \
  -H "Content-Type: application/json" \
  -d "{ \"url\": \"$URL\"}" \
  https://1le09i20al.execute-api.eu-central-1.amazonaws.com/development \
  | jq '.' > my_file.json

