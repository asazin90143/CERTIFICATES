#Instructions 1/4

#Get a list of all playlists from the *playlists API*.

#Import the requests package
import requests

# Make a GET request to the playlists API
response = requests.get('http://localhost:3000/playlists')
print(response.text)

#Instructions 2/4

#Create a dictionary with Name set to Rock Ballads, then perform a POST request with this dictionary as the data parameter.

# Import the requests package
import requests

# Create a dictionary with the new playlist name
playlist_data = {'Name': 'Rock Ballads'}

# Perform a POST request to create the new playlist
response = requests.post('http://localhost:3000/playlists', data=playlist_data)

# Print the response text
print(response.text)

#Instructions 3/4

#Perform a GET request to get information on the playlist with PlaylistId 2.

# Import the requests package
import requests

# Perform a GET request to get information on the playlist with PlaylistId 2
response = requests.get('http://localhost:3000/playlists/2')

# Print the response text

print(response.text)

