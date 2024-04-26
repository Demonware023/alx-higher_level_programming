#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package requests
You are not allow to import packages other than requests
The body of the response must be display like the following example (tabulation before -)
"""
import requests

if __name__ == "__main__":
    # Specify the URL to fetch
    url = "https://alx-intranet.hbtn.io/status"

    # Send a GET request to the URL
    response = requests.get(url)

    # Print the body of the response
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
