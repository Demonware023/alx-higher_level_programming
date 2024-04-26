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
    url = sys.argv[1]
    # sys.argv[1] is the first command-line argument. In this case,
    # it’s the URL that you want to send a request to.
    try:
        with urllib.request.urlopen(url) as response:
	    # The urlopen function from the urllib.request module is used to open the URL
	    # The read method is used to read the response, and decode is
	    #used to decode the response from bytes to a string using utf-8 encoding.
	    print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        # This is the except block that catches HTTPError exceptions
        # which are raised for non-200 HTTP codes. If an HTTPError is
        # caught, the script prints "Error code: " followed by the HTTP status code.
        print("Error code: {}".format(error.code))
