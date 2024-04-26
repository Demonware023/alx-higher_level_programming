#!/usr/bin/python3
"""
A Python script that fetches the specified URL using the urllib package and displays the body of the response as required:
"""
from urllib.request import urlopen

# The URL to open
url = "https://alx-intranet.hbtn.io/status"

with urlopen(url) as response:
    # Read the body of the response
    body_content = response.read()

    # Decode the byte content into a string using UTF-8 encoding
    decoded_content = body_content.decode("utf-8")

    # Display the body of the response
    print("Body response:")
    print("\t- type:", type(body_content))
    print("\t- content:", body_content)
    print("\t- utf8 content:", decoded_content)
