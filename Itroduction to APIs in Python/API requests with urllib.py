#Instructions
#Use the read function on the response object to read the response data from the response object.
#Use the decode function to decode the response data into a string with the right encoding.

from urllib.request import urlopen

with urlopen('http://localhost:3000/lyrics/') as response:
  
  # Use the correct function to read the response data from the response object
  data = response.read()
  encoding = response.headers.get_content_charset()

  # Decode the response data so you can print it as a string later
  string = data.decode(encoding)
  
  print(string) 