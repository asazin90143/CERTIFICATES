#Instructions 1/3:

# Construct the URL to the *random lyrics API* for the `requests.get()` method using the protocol, domain, port and path components.

#Note: Do not use the query parameters yet, we will add these in the next steps!

# Import the requests package
import requests

# Construct the URL string and pass it to the requests.get() function
response = requests.get('http://localhost:3000/lyrics/random')

# Print the response text
print(response.text)

#Instructions 2/3

#Let's now add a query parameter to only get lyrics by a specific artist.

#Create a dictionary variable with one entry: the key `artist` with a value of `Deep Purple`.
#Pass this dictionary to the `requests.get()` method as the `params` argument.

# Import the requests package
import requests

# Create a dictionary variable with query params
query_params = {'artist': 'Deep Purple'}

# Pass the dictionary to the get() function
response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

# Print the response text
print(response.text)