#Instructions

# Add the correct header to request JSON from the API.
# Decode the JSON response into an album object.
# Print the album `Title` property.

# Import the requests package
import requests

headers = {
    'Authorization': 'Bearer ' + API_TOKEN,
    # Add a header to request JSON formatted data
    'accept': 'application/json'
}
response = requests.get('http://localhost:3000/albums/1/', headers=headers)

# Get the JSON data as a Python object from the response object
album = response.json()

# Print the album title
print(album['Title'])