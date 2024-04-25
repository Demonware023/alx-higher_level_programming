#!/bin/bash
# This script takes a URL as an argument, sends a POST request to the URL, and displays the body of the response.Two variables, email and subject, are sent with specific values in the POST request
curl -sLX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
