#!/usr/bin/python3
"""
A Python script that takes a URL as input, sends a request to the URL,
-and displays the value of the X-Request-Id variable found in the
-header of the response:
"""
import urllib.request
import sys

# Extract the URL from command-line arguments
if __name__ == "__main__":
    url = sys.argv[1]

    # Send a GET request to the URL
    # (using with so resources are properly closed.)
    with urllib.request.urlopen(url) as response:
        # Get the value from X-Request-Id
        # Display the value of the X-Request-Id header
        print(response.getheader('X-Request-Id'))
