#Instructions 1/4

#Get a list of all playlists from the *playlists API*.

#Import the requests package
import requests

# Make a GET request to the playlists API
response = requests.get('http://localhost:3000/playlists')
print(response.text)

