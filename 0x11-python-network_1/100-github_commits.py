#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""
import requests
import sys

# Extract the repository name and owner name from command-line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Construct the URL for the GitHub API endpoint to list commits
url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

# Send a GET request to the GitHub API endpoint
response = requests.get(url)

# Parse the JSON response
commits = response.json()

# Iterate over the 10 most recent commits and print SHA and author name
for commit in commits[:10]:
    sha = commit['sha']
    author_name = commit['commit']['author']['name']
    print(f"{sha}: {author_name}")
