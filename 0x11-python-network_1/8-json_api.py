#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request to
-http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display
-the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
"""
import requests
import sys

if __name__ == "__main__":
    # Extract the letter from command-line arguments
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Send a POST request to the URL with the letter as a parameter
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})

    # Parse the JSON response
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
