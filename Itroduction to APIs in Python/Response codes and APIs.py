#Instructions 1/3
# Check if the server responded successfully with the `200` status code.
import requests
response = requests.get('http://localhost:3000/lyrics')

# Check the response status code
if (response.status_code == 200):
  print('The server responded succesfully!')

#Instructions 2/3
#Perform a request to the inexistent `/movies` path of the music catalog API.
# Check if the server responded with a status code indicating the resource was not found, providing the appropriate numerical status code representing this.
# Make a request to the movies endpoint of the API

response = requests.get('http://localhost:3000/movies')

if (response.status_code == 200):
  print('The server responded succesfully!')
  
# Check the response status code
elif (response.status_code == 404):
  print('Oops, that API could not be found!')

#Instructions 3/3
#Check for response codes with a `200 OK` and `404 Not found` status code using the `requests.codes` lookup object.