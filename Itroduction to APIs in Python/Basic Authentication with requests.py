#Instructions 1/2

# Check the numeric status code value on the request object for a successful response.
# Also check for a failed authentication request which has a specific status-code too.

# Import the requests package
import requests

# Perform a GET request to the lyrics API
response = requests.get('http://localhost:3000/lyrics')

# Check if the response status code is 200
if (response.status_code == 200):
  print('The server responded successfully!')
  
# Check if the response status code is 401
elif (response.status_code == 401):
  print('Authentication failed!')


#Instructions 2/2

# Create the correct `authentication` variable with your username and password.
# Then pass the `authentication` variable to the `requests.get()` method using the correct argument.

# Import the requests package
import requests

# Create the authentication tuple with the correct values for basic authentication
authentication = ('john@doe.com', 'Warp_ExtrapolationsForfeited2')

# Use the correct function argument to pass the authentication tuple to the API
response = requests.get('http://localhost:3000/albums', auth = authentication)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')