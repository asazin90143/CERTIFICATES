#Instructions 1/2

# Create a dictionary with a key-value pair for the API key. The API expects the `access_token` URL parameter to contain your unique API key.
# Pass the dictionary to the `requests.get()` function using the correct argument to pass URL parameters.

# Import the requests package
import requests

# Create a dictionary containing the API key using the correct key-value combination
params = {'access_token': '8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'}
# Add the dictionary to the requests.get() call using the correct function argument
response = requests.get('http://localhost:3000/albums', params=params)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')

#Instructions 2/2

# Create a dictionary that includes a key-value pair for the API key, this time using the `Authorization` header.
# Pass the dictionary to the `requests.get()` function as headers.

# Import the requests package
import requests

# Create a headers dictionary containing and set the API key using the correct key and value 
headers = {'Authorization': 'Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'}
# Add the headers dictionary to the requests.get() call using the correct function argument
response = requests.get('http://localhost:3000/albums', headers=headers)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')