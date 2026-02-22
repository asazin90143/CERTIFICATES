#Instructions 1/3:

# Construct the URL to the *random lyrics API* for the `requests.get()` method using the protocol, domain, port and path components.

#Note: Do not use the query parameters yet, we will add these in the next steps!

# Import the requests package
import requests

# Construct the URL string and pass it to the requests.get() function
response = requests.get('http://localhost:3000/lyrics/random')

# Print the response text
print(response.text)

