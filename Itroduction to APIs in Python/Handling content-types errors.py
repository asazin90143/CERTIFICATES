#Instructions

# Add an `accept` header to request a response in the `application/xml` content-type from the server.
# Check if the server did not accept the request using the relevant status code.
# Print out a list of accepted content types from the server response.

# Add a header to use in the request
headers = {'accept': 'application/xml'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Check if the server did not accept the request
if (response.status_code == 406):
  print('The server can not respond in XML')
  
  # Print the accepted content types
  print('These are the content types the server accepts: ' + response.headers['accept'])
else:
  print(response.text)