#!/usr/bin/python3
"""
A Python script that takes a URL as input, sends a request to the URL
-using the requests library, and displays the body of the response.
If the HTTP status code is greater than or equal to 400, it prints
-an error message with the status code:
"""
import requests
import sys

# Extract the URL from command-line arguments
url = sys.argv[1]

# Send a GET request to the URL
response = requests.get(url)

# Check the status code of the response
if response.status_code >= 400:
    print("Error code:", response.status_code)
else:
    # Display the body of the response
    print(response.text)
