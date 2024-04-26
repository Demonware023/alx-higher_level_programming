#!/usr/bin/python3
"""
A Python script that uses the requests and sys packages to send a
-request to a URL and display the value of the X-Request-Id variable found
-in the header of the response:
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = request.get(url)
    print(response.headers.get('X-Request-Id'))
