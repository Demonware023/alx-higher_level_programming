#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
# Send a JSON POST request with the contents of the file as the body
curl -s "$1" -X POST -H "Content-type: application/json" -d @"$2"
