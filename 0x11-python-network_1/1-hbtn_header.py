#!/usr/bin/python3
"""
A Python script that takes a URL as input, sends a request to the URL,
-and displays the value of the X-Request-Id variable found in the 
-header of the response:
"""
from urllib.request import urlopen
import sys

# Extract the URL from command-line arguments
url = sys.argv[1]

# Send a GET request to the URL 
# (using with so resources are properly closed.)
with urlopen(url) as response:
    # Get the value of the X-Request-Id header
    x_request_id = response.headers.get('X-Request-Id')

    # Display the value of the X-Request-Id header
    print(x_request_id)
