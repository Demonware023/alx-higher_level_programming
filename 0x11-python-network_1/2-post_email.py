#!/usr/bin/python3
"""
A Python script that uses the urllib and sys packages to send
a POST request to a URL with an email as a parameter,
and display the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

# Extract the URL and email from command-line arguments
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
