#Instructions 1/3
# Find out the content-type of the response by printing out the response `content-type` header.
import requests
response = requests.get('http://localhost:3000/lyrics')

# Print the response content-type header
print(response.headers['content-type'])


#Instructions 2/3
# Find out what content-types the server can respond with by printing out the response `accept` header.
response = requests.get('http://localhost:3000/lyrics')

# Print the response accept header
print(response.headers['accept'])

#Instructions 3/3
# Add an `accept` header to the request so the server returns JSON formatted data, then print the response `text` attribute.
response = requests.get('http://localhost:3000/lyrics', headers={'Accept': 'application/json'})
print(response.text)