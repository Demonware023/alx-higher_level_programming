#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.

# Check if the filename argument is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Check if the file exists
if [ ! -f "$2" ]; then
    echo "File $2 does not exist."
    exit 1
fi

# Check if the file contains valid JSON
if ! jq . "$2" > /dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send a JSON POST request with the contents of the file as the body
curl -sX POST -H "Content-type: application/json" -d @"$2" "$1"
