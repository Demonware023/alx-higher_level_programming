#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).

You have to manage urllib.error.HTTPError exceptions and
-print: Error code: followed by the HTTP status code
You must use the packages urllib and sys
You are not allowed to import other packages than urllib and sys
You don’t need to check arguments passed to the script (number or type)
You must use the with statement
"""
import sys
import urllib.request
import urllib.error

# This line checks if the script is being run directly. If it is, the code
# within this block will be executed. If the script is being imported
# as a module in another script, this code block will not be executed.
if __name__ == "__main__":
    # Extract the URL from command-line arguments
    url = sys.argv[1]

    try:
        # Send a GET request to the URL
        with urlopen(url) as response:
            # Read and decode the body of the response
            decoded_content = response.read().decode("utf-8")
        
            # Display the body of the response
            print(decoded_content)

    except HTTPError as e:
        # Print the error code if an HTTPError occurs
        print("Error code:", e.code)
