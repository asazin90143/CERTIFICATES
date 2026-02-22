#Instructions 1/2
# Import the exception class used to detect connection errors from the requests package, then use the imported class to intercept the error raised by the API request.

import requests
# Import the correct exception class
from requests.exceptions import ConnectionError, HTTPError

url ="http://wronghost:3000/albums"
try: 
    r = requests.get(url) 
    print(r.status_code)
# Use the imported class to intercept the connection error
except ConnectionError as conn_err: 
    print(f'Connection Error! {conn_err}.')

    
#Instructions 2/2
# Import the exception class used to detect errors returned via the response status code, then enable the setting on the response object which will automatically raise an error when an unsuccessful status code value is received. Finally, intercept the imported exception to print an error.

# Import the correct exception class
from requests.exceptions import HTTPError

url ="http://localhost:3000/albums/"
try: 
    r = requests.get(url) 
	# Enable raising errors for all error status_codes
    r.raise_for_status()
    print(r.status_code)
# Intercept the error 
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')