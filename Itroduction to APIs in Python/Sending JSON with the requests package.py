#Instructions

# Pass the playlists variable as an argument to the requests.post() method so that it will be automatically sent as JSON.
# Get a list of all playlists from the API.
# Inspect the response of the GET request by printing the JSON text.

# Import the requests package
import requests

playlists = [{"Name":"Rock ballads"}, {"Name":"My favorite songs"}, {"Name":"Road Trip"}]

# POST the playlists array to the API using the json argument
requests.post('http://localhost:3000/playlists/', json=playlists)

# Get the list of all created playlists
response = requests.get('http://localhost:3000/playlists')

# Print the response text to inspect the JSON text
print(response.text)


