#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials (username and
-password) and uses the GitHub API to display your id

You must use Basic Authentication with a personal access token as password
-to access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal
-access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
import requests
import sys

# Extract username and personal access token from command-line arguments
username = sys.argv[1]
password = sys.argv[2]

# Construct the URL for the GitHub API endpoint to get user information
url = f"https://api.github.com/user"

# Send a GET request to the GitHub API endpoint with Basic Authentication
response = requests.get(url, auth=(username, password))

# Check if the request was successful and the response contains
# -user information
if response.status_code == 200:
    # Parse the JSON response
    user_info = response.json()
    # Display the user ID
    print(user_info['id'])
else:
    print("None")
