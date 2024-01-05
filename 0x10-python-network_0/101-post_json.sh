#!/bin/bash
# Send a GET request with the custom header and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
