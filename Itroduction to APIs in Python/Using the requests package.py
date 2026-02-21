#Instructions

#Import the requests package.
#Pass the URL http://localhost:3000/lyrics to the requests.get method.
#Print out the response text.

# Import the requests package
import requests

# Pass the API URL to the get function
response = requests.get("http://localhost:3000/lyrics")

# Print out the text attribute of the response object
print(response.text)