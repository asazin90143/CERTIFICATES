# Introduction to API in Python

Status: In progress
Type: Work

# **Introduction to APIs**

## **1. Introduction to APIs**

- **Definition:** API stands for **Application Programming Interface**.
- **Core Function:** A set of rules that allows two systems to communicate, exchange data, or manipulate information.
- **API vs. UI:** * **UI (User Interface):** What humans use to interact with software.
    - **API:** What systems use to interact with each other behind the scenes (e.g., clicking "send" in an email app triggers an API call to a server).

![image.png](image.png)

## **2. Web APIs and the Client-Server Model**

Web APIs facilitate communication over a network or the internet using the **HTTP protocol** (the same protocol used by web browsers).

- **The Client:** The application sending the request (e.g., your Python script).
- **The Server:** The system receiving the request and sending a response back.

![image.png](image%201.png)

## **3. Types of Web APIs**

While there are several ways to build APIs, three types are most common:

| **Type** | **Characteristics** | **Use Case** |
| --- | --- | --- |
| **SOAP** | Formal, robust, uses strict protocols. | Enterprise applications. |
| **REST** | **Most popular**; known for simplicity and scalability. | General web integrations (Focus of this course). |
| **GraphQL** | Focused on precise data retrieval; minimizes data transfer. | Performance-optimized applications. |

## **4. Working with APIs in Python**

The lesson compares two primary libraries for making API calls: `urllib` and `requests`.

### **Option A: urllib (Standard Library)**

- **Pros:** Built into Python (no installation needed); very powerful.
- **Cons:** Verbose and complex.
- **Workflow:** 1. Call `urlopen()` to send the request.
2. Use `.read()` on the response object.
3. Use `.decode()` to extract the raw data.

![image.png](image%202.png)

### **Option B: requests (Third-Party Library)**

- **Pros:** Simplifies the process significantly; handles reading and decoding automatically.
- **Cons:** Must be installed (e.g., via `pip`).
- **Workflow:**
    1. Use `requests.get()` to fetch data.
    2. Access the `.text` attribute to see the result.

![image.png](image%203.png)

> **Key Takeaway:** While `urllib` is powerful, the `requests` library is the industry standard for its ease of use and cleaner code.
> 

## **API requests with urllib**

You will be using the API for a *Music Catalog* application. This API has multiple features. You will start with the *Lyrics API*, which allows you to retrieve a quote from the *Lyric of the day*.

Before you can make your first API request, you will need to know where the API can be accessed. This location is also referred to as the **URL**, short for Uniform Resource Locator. The URL will tell Python *where* to send the API request to. The URL for the Lyrics API is as follows: `http://localhost:3000/lyrics/`.

Let's make a first request to the Lyrics API using the built-in `urllib` Python module.

Instructions

- Use the read function on the response object to read the response data from the response object.
- Use the decode function to decode the response data into a string with the right encoding.

Code:

```python
from urllib.request import urlopen

with urlopen('http://localhost:3000/lyrics/') as response:
  
  # Use the correct function to read the response data from the response object
  data = response.read()
  encoding = response.headers.get_content_charset()

  # Decode the response data so you can print it as a string later
  string = data.decode(encoding)
  
  print(string)
```

Output:

![image.png](image%204.png)

using the `urllib` module you have retrieved the 'Lyric of the day' from the Lyric API. The code is quite complex though, as we had to deal with decoding, etc. Let's see if we can make it simpler.

## **Using the requests package**

Using `urllib` to integrate APIs can result in verbose and complex code as you need to take care of a lot of additional things like encoding and decoding responses.

As an alternative to `urllib`, the `requests` Python package offers a simpler way to integrate APIs. A lot of functionality is available out of the box with `requests`, which makes your code a lot easier to write and read. Let's try the same exercise again but now with the `requests` package.

Remember, as with the previous exercise, the URL for the Lyrics API is `http://localhost:3000/lyrics`.

**Instructions**

- Import the `requests` package.
- Pass the URL `http://localhost:3000/lyrics` to the `requests.get` method.
- Print out the response text.

Code:

```python
# Import the requests package
import requests

# Pass the API URL to the get function
response = requests.get("http://localhost:3000/lyrics")

# Print out the text attribute of the response object
print(response.text)
```

Output:

![image.png](image%205.png)

using the `requests` package you have simplified the code a lot. The `requests` package even took care of decoding the response for you, how cool is that? Let's move on and see what more can be done with the requests package.

## 1. The Basic Anatomy of an API Request

Fetching data from an API is a straightforward process. By using the **requests** package in Python, we can provide detailed instructions to an API to retrieve exactly what we need.

![image.png](image%206.png)

---

## 2. What are URLs?

A URL (Uniform Resource Locator) is a fundamental concept in Web APIs. It acts as a **structured address** pointing to a specific resource.

- **The Analogy:** Think of a REST API as an office building.
    - **Office Unit:** A unique resource.
    - **URL:** The address of a single unit in that building, containing all the information needed to navigate there.
    
    ![image.png](image%207.png)
    

---

## 3. Dissecting the URL

A URL consists of five main components that determine how you reach and interact with a resource:

![image.png](image%208.png)

| **Component** | **Description** | **Office Building Analogy** |
| --- | --- | --- |
| **Protocol** | Determines the "transportation" method. | Walking vs. Driving |
| **Domain** | Uniquely identifies the API server location on the internet. | The street address of the building |
| **Port** | The gateway or entrance (Common defaults: 80, 443). | Entering via the garage vs. front door |
| **Path** | The specific location of the resource on the server. | The specific office unit number |
| **Query** | Additional instructions or parameters. | Instructions like "take the elevator" |

## 4. Adding Query Parameters with `requests`

While you can append query parameters directly to a URL string, the **requests** package offers a cleaner method:

- **The `params` Argument:** Every HTTP method (like `get`) accepts a `params` argument.
- **Format:** It takes a **dictionary** of key/value pairs.
- **Benefit:** This makes the code much more readable and easier to manage than manual string concatenation.

![image.png](image%209.png)

---

## 5. HTTP Verbs

HTTP verbs define **what action to take** once you arrive at the URL destination. While there are 9 verbs in total, these 4 are the most relevant for REST APIs:

| Verb | Action | Description |
| --- | --- | --- |
| **GET** | Reads  | Check the mailbox contents |
| **POST** | Creates | Drop a new package in the mailbox |
| **PUT** | Updates | Replace all packages with a new one |
| **DELETE** | Removes | Remove all packages from the mailbox |

There are 9 HTTP verbs in total, but for simple REST APIs only these 4 are relevant

| **Verb** | **Action** | **Description** |
| --- | --- | --- |
| **PATCH** | **Modify** | Applies partial modifications to a resource. Unlike PUT, it only updates the specific fields you provide. |
| **HEAD** | **Check** | Identical to GET, but it only asks for the response headers and **no response body**. Useful for checking if a file exists or its size. |
| **OPTIONS** | **Inquire** | Describes the communication options for the target resource (e.g., "Which methods are allowed for this URL?"). |
| **CONNECT** | **Tunnel** | Establishes a tunnel to the server identified by the target resource; primarily used for proxy servers and SSL (HTTPS). |
| **TRACE** | **Echo** | Performs a message loop-back test along the path to the target resource, useful for debugging what intermediate servers are doing to the request. |

---

## 6. Sending Data via POST and PUT

The `requests` package provides specific functions for each verb (e.g., `requests.post()`, `requests.put()`, `requests.delete()`).

![image.png](image%2010.png)

- **Sending Data:** For POST and PUT, use the `data` argument to specify the information you want to create or update.
- **Syntax Example:** Similar to `params`, you pass your information through this argument to send it along with the request.
- **DELETE:** This is the simplest to implement—just call the `.delete()` function on the target URL.

### **The 4 most important HTTP Verbs**

HTTP verbs are a fundamental concept in REST APIs. There are 9 verbs in total, you got to know the four most important ones used by REST APIs: GET, POST, PUT and DELETE.

**Instructions**

Drag and drop each item into the correct HTTP Verb bucket based on the type of action that is being performed.

![image.png](image%2011.png)

## **Constructing a URL with parameters**

You can fine-tune your API requests using the path and query parameters of the URL. Let's learn how you can use HTTP verbs, URL paths, and parameters using the `requests` package.

In this exercise, you will make another API request to the *Lyrics API*, but instead of getting today's lyric, you will send a request to the *random lyrics API*. You will then further customize the API request by adding query parameters to filter on specific artists and include the track title. Below, you can find the details needed to construct the correct URL.

| Component | Value |
| --- | --- |
| Protocol | http |
| Domain | localhost |
| Port | 3000 |
| Path | /lyrics/random |
| Artist filter parameter | artist |
| Include track parameter | include_track |

The `requests` library is already imported for your convenience.

Instructions 1/3:

- Construct the URL to the *random lyrics API* for the `requests.get()` method using the protocol, domain, port and path components.

Note: Do not use the query parameters yet, we will add these in the next steps!

Code:

```python
# Construct the URL string and pass it to the requests.get() function
response = requests.get('http://localhost:3000/lyrics/random')

print(response.text)
```

Output:

![image.png](image%2012.png)

Instructions 2/3

Let's now add a query parameter to only get lyrics by a specific artist.

- Create a dictionary variable with one entry: the key `artist` with a value of `Deep Purple`.
- Pass this dictionary to the `requests.get()` method as the `params` argument.

Code:

```python
# Create a dictionary variable with query params
query_params = {'artist': 'Deep Purple'}

# Pass the dictionary to the get() function
response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

print(response.text)
```

Output:

![image.png](image%2013.png)

![image.png](image%2014.png)

Instructions 3/3

- Add a second item to the dictionary with the key `include_track` and the Boolean value `True`.
- Print the response's `url` attribute to see the full URL.
- Print out the lyric.

Code:

```python
# Add the `include_track` parameter
query_params = {'artist': 'Deep Purple', 'include_track' : True}

response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

# Print the response URL
print(response.url)

# Print the lyric
print(response.text)
```

Output:

![image.png](image%2015.png)

now the track title is included in the lyric! Check the URL we printed, notice how the requests library took care of properly encoding and structuring the artists query parameter for you? Cool isn't it?

## **Creating and deleting resources using an API.**

Now that you have learned how to construct a URL, you can send requests to specific API resources. Let's see what more you can do with HTTP verbs on these resources.

In this exercise, you will use the *playlists API* available via `http://localhost:3000/playlists/`. This API offers the following actions:

| Verb | Path | Description |
| --- | --- | --- |
| GET | `playlists` | get a list of all playlists |
| GET | `/playlists/{PlaylistId}` | get information on a single playlist using it's unique identifier `PlaylistId` |
| POST | `/playlists` | create a new playlist |
| DELETE | `/playlists/{PlaylistId}` | remove an existing playlist using it's unique identifier `PlaylistId` |

You will start by getting a list of all existing playlists, then you will learn how to create a new playlist and verify it's creation, and last you will learn how to remove an existing playlist.

The `requests` library is already imported for your convenience.

Instructions 1/4

• Get a list of all playlists from the *playlists API*.

Code:

```python
import requests

# Make a GET request to the playlists API
response = requests.get('http://localhost:3000/playlists')
print(response.text)
```

Output:

![image.png](image%2016.png)

Instructions 2/4

- Create a dictionary with Name set to Rock Ballads, then perform a POST request with this dictionary as the data parameter.

Code:

```python
# Create a dictionary with the playlist info
playlist_data = {'Name': 'Rock Ballads'}

# Perform a POST request to the playlists API with your dictionary as data parameter
response = requests.post('http://localhost:3000/playlists', data=playlist_data)
print(response.text)
```

Output:

![image.png](image%2017.png)

Instructions 3/4

- Perform a GET request to get information on the playlist with PlaylistId 2.

Code:

```python
# Perform a GET request to get info on playlist with PlaylistId 2
response = requests.get('http://localhost:3000/playlists/2')

print(response.text)
```

Output:

![image.png](image%2018.png)

Instructions 4/4

- Send a DELETE request to the URL for the playlist with PlaylistId 2 and get the list of existing playlists to confirm removal.

Code:

```python
# Import the requests package
import requests

# Send a DELETE request to the URL for the playlist with PlaylistId 2
response = requests.delete('http://localhost:3000/playlists/2')

# Get the list of all playlists
response = requests.get('http://localhost:3000/playlists')

# Print the response text
print(response.text)
```

Output:

![image.png](image%2019.png)

# Headers and status codes

## 1. Headers and Status Codes

While sending and processing basic requests is the first step, **headers** and **status codes** allow us to provide the server with extra instructions and verify if our requests were handled correctly.

---

## 2. Request and Response Message Anatomy

Both request and response messages share a very similar structure, which can be divided into three distinct parts.

![image.png](image%2020.png)

---

## 3. The Start-line

The first part of any HTTP message is the start-line, though its name changes based on the direction of the message:

- **Request-line (Request):** Contains the **request type** (e.g., `GET`, `POST`) and the **path** where the message should be delivered.
- **Status-line (Response):** Contains a **three-digit numerical status code** and a corresponding **status message**.

![image.png](image%2021.png)

---

## 4. Status Codes

There are over 70 status codes, grouped into five major categories. Understanding the "hundreds" digit helps identify the type of response:

| **Category** | **Type** | **Common Examples** |
| --- | --- | --- |
| **2xx** | **Success** | `200 OK`: Request processed correctly. |
| **4xx** | **Client Error** | `404 Not Found`: The resource doesn't exist. |
| **5xx** | **Server Error** | `500 Internal Server Error`: An error occurred on the server side. |

![image.png](image%2022.png)

---

## 5. Headers

Headers describe the message or the data being exchanged (e.g., content type or last modified date).

- **Format:** Always formatted as **key-value pairs** separated by a colon.
- **Case-Insensitivity:** Header keys are case-insensitive.
- **Example:** `Content-Type: application/json`

![image.png](image%2023.png)

---

## 6. Content Negotiation

Clients and servers use headers to "negotiate" the language or format of the data exchange.

- **Accept Header:** Sent by the **client** to tell the server what format it can handle (e.g., JSON).
- **Content-Type Header:** Sent by the **server** to inform the client of the format actually used in the response.

![image.png](image%2024.png)

---

## 7. Headers with `requests`

The Python `requests` package makes it easy to both send and read these headers.

- **Sending Headers:** Use the `headers` parameter in methods like `requests.get()`. It accepts a **dictionary** of key-value pairs.
- **Reading Headers:** The response object has a `.headers` attribute (also a dictionary).
    - Access via square brackets: `response.headers['Content-Type']`
    - Access via `.get()`: `response.headers.get('Content-Type')`

![image.png](image%2025.png)

---

## 8. Status Codes with `requests`

Checking the outcome of your request is simplified through two main tools:

1. **`.status_code` attribute:** Every response object contains the numeric value of the code (e.g., `200`).
2. **`requests.codes` lookup:** Instead of memorizing numbers, you can use built-in aliases.
    - *Example:* `requests.codes.ok` returns `200`.
    - *Example:* `requests.codes.not_found` returns `404`.

![image.png](image%2026.png)

## Response codes and APIs

When a client sends a request to a server, the server response includes a numeric status code, which is used to tell the client how the server responded to the request.

In this exercise you will learn about the most important status codes you should know. We will send requests to valid and invalid paths and learn how we can access the status code to determine if our request was successful or not.

The `requests` package comes with a built-in status code lookup object `requests.codes` you can use when you don't remember the exact numerical values.

The `requests` package has been imported for you.

Instructions 1/3

• Check if the server responded successfully with the `200` status code.

Code:

```python
response = requests.get('http://localhost:3000/lyrics')

# Check the response status code
if (response.status_code  == 200):
  print('The server responded succesfully!')
```

Output:

![image.png](image%2027.png)

Instructions 2/3

- Perform a request to the inexistent `/movies` path of the music catalog API.
- Check if the server responded with a status code indicating the resource was not found, providing the appropriate numerical status code representing this.

Code:

```python
# Make a request to the movies endpoint of the API
response = requests.get('http://localhost:3000/movies')

if (response.status_code == 200):
  print('The server responded succesfully!')
  
# Check the response status code
elif (response.status_code == 404):
  print('Oops, that API could not be found!')
```

Output:

![image.png](image%2028.png)

Instructions 3/3

• Check for response codes with a `200 OK` and `404 Not found` status code using the `requests.codes` lookup object.

Code:

```python
response = requests.get('http://localhost:3000/movies')

# Check if the response.status_code is equal to the requests.codes value for "200 OK"
if (response.status_code == requests.codes.ok):
  print('The server responded succesfully!')
  
# Or if the request was not successful because the API did not exist
elif (response.status_code == requests.codes.not_found):
  print('Oops, that API could not be found!')
```

Output:

![image.png](image%2029.png)

Using the requests package, working with status-codes becomes a breeze. And it even becomes easier using the `requests.codes` lookup object! Now let's move on to headers.

## **Using request and response headers**

Headers contain additional information about your API calls, including the desired or used response format. Using `accept` and `content-type` headers, client and server can negotiate what response format to use.

In this exercise, you'll use headers to inspect response formats after making a request and make a new request specifying the desired format via the `accept` header.

The `requests` package has been imported for your convenience.

Instructions 1/3

- Find out the content-type of the response by printing out the response `content-type` header.

Code:

```python
response = requests.get('http://localhost:3000/lyrics')

# Print the response accept header
print(response.headers['accept'])
```

Output:

![image.png](image%2030.png)

Instructions 2/3

- Find out what content-types the server can respond with by printing out the response `accept` header.

Code:

```python
response = requests.get('http://localhost:3000/lyrics')

# Print the response accept header
print(response.headers.get('accpet'))
```

Output:

![image.png](image%2031.png)

Instructions 3/3

- Add an `accept` header to the request so the server returns JSON formatted data, then print the response `text` attribute.

Code:

```python
# Set the content type to application/json
headers = {'accept': 'application/json'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Print the response's text
print(response.text)
```

Output:

![image.png](image%2032.png)

You now know how to retrieve a lyric using the JSON format!

## **Handling content-types errors**

What happens when you ask for a response in a specific format but the server cannot satisfy that request? Say you want to receive the response in XML rather than JSON. If the server can not respond in XML, it will respond with a specific status-code indicating that it can't reply in the requested format. The status code used in this case is `406 Not Acceptable` or `406` in short. The response from the server also frequently contains an `accept` header which includes a list of all response formats it *can* respond with. Use this to learn what content types the API can respond with.

Instructions

- Add an `accept` header to request a response in the `application/xml` content-type from the server.
- Check if the server did not accept the request using the relevant status code.
- Print out a list of accepted content types from the server response.

Code:

```python
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
```

Output:

![image.png](image%2033.png)

Headers can be used for a lot of things, content negotiation is just the start! 

# **API Authentication**

## 1. API Authentication

Many APIs handle private or sensitive data. To protect this information, APIs require **authentication** to verify the identity of the client before granting access.

---

## 2. Accessing Sensitive Data

If you attempt to access a protected resource without identifying yourself, the server will reject the request.

- **401 Unauthorized:** The standard HTTP status code indicating that the request lacks valid authentication credentials.

![image.png](image%2034.png)

- **200 OK:** The status code returned once proper identification is provided and the server verifies your identity.

![image.png](image%2035.png)

---

## 3. Authentication Methods

There are several ways to identify yourself to an API, ranging from simple to highly secure:

| **Method** | **Description** | **Security Level** |
| --- | --- | --- |
| **Basic Authentication** | Uses a username and password. | **Low** (Sent as easily decodable Base64). |
| **API Key / Token** | A unique string (key) attached to every request. | **Medium** (Risk if the key is intercepted). |
| **JWT (JSON Web Token)** | Encrypted tokens with a limited lifespan. | **High** (Contains encrypted metadata). |
| **OAuth 2.0** | A complex framework for fine-grained access. | **Very High** (Does not share actual credentials). |

![image.png](image%2036.png)

---

## 4. Implementing Basic Authentication

Basic Authentication requires an `Authorization` header containing a **Base64-encoded** username and password.

> **Note:** Base64 is **not encryption**; it is a two-way encoding that can be easily reversed by anyone.
> 

**Using the `requests` package:**
You do not need to manually encode your credentials. Simply use the `auth` argument:

- Pass a **tuple** containing `('username', 'password')`.
- The library automatically handles the encoding and adds the necessary header for you.

![image.png](image%2037.png)

---

## 5. API Key / Token Authentication

There are two primary ways to send an API key using the `requests` package:

### Option A: Query Parameters

The key is appended directly to the URL.

- **How:** Use the `params` argument (e.g., `params={'access_token': 'your_key'}`).
- **Security:** Less secure as keys may show up in server logs or browser history.

### Option B: Authorization Header (Preferred)

The key is placed inside the message headers.

- **How:** Use the `headers` argument (e.g., `headers={'Authorization': 'Bearer your_token'}`).
- **Note:** Unlike Basic Auth, `requests` does not have a built-in shortcut for this; you must define the header dictionary yourself.

![image.png](image%2038.png)

## **Basic Authentication with requests**

Basic Authentication is the simplest authentication method for web APIs. It works like logging into a website. To gain access, you need to send your personal username and password along with every request. Using this username and password, the API can identify you and grant you access to the requested data.

Let's first learn how a server responds when authentication fails, and then let's fix it by using *Basic Authentication*.

Good to know:

1. The `requests` package has already been imported.
2. You can use the username `john@doe.com` and the password `Warp_ExtrapolationsForfeited2` to authenticate.

Instructions 1/2

- Check the numeric status code value on the request object for a successful response.
- Also check for a failed authentication request which has a specific status-code too.

Code:

```python
response = requests.get('http://localhost:3000/albums')

# Check if the status code on the response object matches a successful response
if(response.status_code == 200):
    print("Success!")
# Check if the status code indicates a failed authentication attempt
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')
```

Output:

![image.png](image%2039.png)

Instructions 2/2

- Create the correct `authentication` variable with your username and password.
- Then pass the `authentication` variable to the `requests.get()` method using the correct argument.

Code:

```python
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
```

Output:

![image.png](image%2040.png)

You have now used a username and password to authenticate and were able to retrieve the list of albums! Now let's learn how you can use API key based authentication!

## **API key authentication with requests**

API key-based authentication functions similarly to Basic Authentication, but you must include a unique API key using either a request header or a URL parameter for authenticated requests. Let's explore both approaches.

Good to know:

1. The `requests` package has already been imported.
2. Use the API key/token `8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3` to authenticate.

Instructions 1/2

- Create a dictionary with a key-value pair for the API key. The API expects the `access_token` URL parameter to contain your unique API key.
- Pass the dictionary to the `requests.get()` function using the correct argument to pass URL parameters.

Code:

```python
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
```

Output:

![image.png](image%2041.png)

Instructions 2/2

- Create a dictionary that includes a key-value pair for the API key, this time using the `Authorization` header.
- Pass the dictionary to the `requests.get()` function as headers.

Code:

Output:

![image.png](image%2042.png)

Now you know how to authenticate using API keys using URL parameters and headers!

# Working with structured data

## 1. Working with Structured Data

While simple requests can return plain text (like song lyrics), real-world API interactions often involve **complex data structures**. To exchange information effectively, we need a way to organize multiple properties like IDs, titles, and lists.

---

## 2. Complex Data Structures: JSON

To handle structured data, APIs use specific formats. The most common is **JSON** (JavaScript Object Notation).

- **Characteristics:** Lightweight, natively supported by most languages, and easily readable by both humans and machines.
- **Terminology:** JSON is a **Content-Type** (also known as a MIME-type or Media-type).
- **Other Formats:** You may also encounter XML, CSV, or YAML.

![image.png](image%2043.png)

---

## 3. From Python to JSON and Back

Data must be converted into a string format to be transmitted over the internet. This process is handled by the built-in `json` package in Python:

- **Encoding (Serialization):** Converting a Python object into a JSON string using `json.dumps()`.
- **Decoding (Deserialization):** Converting a JSON string back into a Python object using `json.loads()`.

![image.png](image%2044.png)

---

## 4. Requesting JSON Data

When using the `requests` package, you can specifically ask the server for structured data:

1. **Content Negotiation:** Add an `Accept` header with the value `application/json` to inform the server you want JSON.
2. **Accessing Text:** `response.text` shows the raw JSON string.
3. **The `.json()` Method:** This is a built-in shortcut in `requests` that automatically decodes the JSON text into a Python dictionary or list, allowing you to access attributes easily (e.g., `data['artist']`).

![image.png](image%2045.png)

---

## 5. Sending JSON Data

Sending data is even simpler because `requests` automates the technical steps:

- **The `json` Argument:** Instead of using the `data` argument (which sends form data), use the `json` argument (e.g., `requests.post(url, json=my_dict)`).
- **Automatic Headers:** When you use the `json` argument, the library automatically:
    1. Encodes your Python object into a JSON string.
    2. Sets the `Content-Type` header to `application/json`.

![image.png](image%2046.png)

## Receiving JSON with the requests package

When requesting JSON data from an API, the requests library makes it really easy to decode the JSON string you received from the API back into a Python object. In this exercise you'll first need to request data in the JSON format from the API, then decode the response into a Python object to retrieve and print the album `Title` property.

Note: The requests package has been imported for you, and because the albums API is protected by authentication, the correct header has already been added.

Instructions

• Add the correct header to request JSON from the API.
• Decode the JSON response into an album object.
• Print the album `Title` property.

Code:

```python
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
```

Output:

![image.png](image%2047.png)

Great job getting the title from that album using JSON.

## **Sending JSON with the requests package**

Similar to how you can receive JSON text from an API response, you can also send JSON text to an API with POST or PUT requests. If you use the `json` argument for the `request.post()` and `request.put()` methods, the `requests` library will take care of adding all the necessary headers and encoding for you. Neat!

Let's try it out! Did you know you can create multiple playlists at once using a POST request to the `/playlists` API? Just pass an array of playlists (each with a `Name` property) to the API and it will create them all at once.

Instructions

- Pass the `playlists` variable as an argument to the `requests.post()` method so that it will be automatically sent as JSON.
- Get a list of all playlists from the API.
- Inspect the response of the GET request by printing the JSON text.

Code:

```python
playlists = [{"Name":"Rock ballads"}, {"Name":"My favorite songs"}, {"Name":"Road Trip"}]

# POST the playlists array to the API using the json argument
requests.post('http://localhost:3000/playlists/', json=playlists)

# Get the list of all created playlists
response = requests.get('http://localhost:3000/playlists')

# Print the response text to inspect the JSON text
print(response.text)
```

Output:

![image.png](image%2048.png)

good job using JSON to create multiple playlists at once!

# **Error handling**

## 1. Error Handling

When communicating with a web API over the internet, issues are inevitable. Gracefully handling these errors prevents your application from crashing and helps you understand whether the problem lies with your request or the server itself.

---

## 2. Error Status Codes

REST APIs use the `status_code` to communicate the outcome of a request. Errors are divided into two main categories:

| **Category** | **Type** | **Cause** | **Typical Resolution** |
| --- | --- | --- | --- |
| **4xx** | **Client Error** | The request was incorrect (e.g., wrong header, bad authentication). | Fix the request on the client side. |
| **5xx** | **Server Error** | The server acknowledged the request but failed to process it. | Usually beyond client control; wait and retry later. |

![image.png](image%2049.png)

---

## 3. Common Error Examples

Understanding specific codes allows you to implement targeted fixes:

### 4xx Range (Client)

- **401 Unauthorized:** You need to provide valid authentication.
- **404 Not Found:** The resource/URL you are looking for doesn't exist.
- **429 Too Many Requests:** You’ve hit a rate limit. **Solution:** Implement a rate limiter to spread out requests.

### 5xx Range (Server)

- **500 Internal Server Error:** A "catch-all" for general server failures.
- **502 / 504 Gateway Errors:** Issues with the server's infrastructure or connection timeouts.

![image.png](image%2050.png)

---

## 4. How to Handle Errors

Simply checking the status code isn't enough because some errors happen **before** the request even reaches the server (e.g., no internet connection).

- **Connection Errors:** If the request fails to reach the server, the `requests` library raises a `ConnectionError`. This must be handled using a `try/except` block.
- **HTTP Errors:** If the request reaches the server but returns a 4xx or 5xx code, you need to handle the response code.

![image.png](image%2051.png)

---

## 5. Using `raise_for_status()`

The `requests` library provides a built-in shortcut to handle HTTP errors automatically.

1. **Call the Function:** Run `response.raise_for_status()` immediately after sending your request.
2. **The Result:** If the response is a 4xx or 5xx, it will automatically raise an `HTTPError`.
3. **Best Practice:** Combine this with a `try/except` block to catch both network issues and API-specific errors:

```python
import requests
# 1: Import the requests library exceptions
from requests.exceptions import ConnectionError, HTTPError

try:

r = requests.get ("http://api.music-catalog.com/albums")

# 2: Enable raising exceptions for returned error statuscodes
r.raise_for_status()

print(r.status_code)

# 3: Catch any connection errors
except ConnectionError as conn_err:
print(f'Connection Error! {conn_err}.')
```

## **Handling errors with Requests**

When the `requests` library is unable to connect to an API server, it will raise an exception. This exception allows you to detect if the API is available and act accordingly. But even when the request is successfully sent, we can still encounter errors. If we send an invalid request, a `4xx Client Error` is returned from the API, if the server encounters an error, a `5xx Server Error` is returned.

The `requests` package provides a [**set of included exceptions**](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions) that can be used to handle these errors using `try/except` statements.

*The `requests` package has already been imported for your convenience.*

Instructions 1/2

- Import the exception class used to detect *connection errors* from the `requests` package, then use the imported class to intercept the error raised by the API request.

Code:

```python
# Import the correct exception class
from requests.exceptions import ConnectionError, HTTPError

url ="http://wronghost:3000/albums"
try: 
    r = requests.get(url) 
    print(r.status_code)
# Use the imported class to intercept the connection error
except ConnectionError as conn_err: 
    print(f'Connection Error! {conn_err}.')
```

Output:

![image.png](image%2052.png)

Instructions 2/2

- Import the exception class used to detect errors returned via the response status code, then enable the setting on the response object which will automatically raise an error when an unsuccessful status code value is received. Finally, intercept the imported exception to print an error.

Code:

```python
# Import the correct exception class
from requests.exceptions import HTTPError

url ="http://localhost:3000/albums/"
try: 
    r = requests.get(url) 
	# Enable raising errors for all error status_codes
    r.raise_for_status()
    print(r.status_code)
# Intercept the error 
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
```

Output:

![image.png](image%2053.png)

You did a great job catching those errors! Now let's move on to the last exercise.

## **Respecting API rate limits**

Let's put what we learned about error handling to the test. In this exercise you'll encounter a *rate-limit error*, which means you're sending too many requests to the server in a short amount of time. Let's fix it by implementing a workaround to circumvent the rate limit so our script doesn't fail.

Your music library contains over 3500 music tracks, so let's try to find the longest track by checking the `Length` property of each track.

But there is an issue, the `/tracks` API has a maximum page size of 500 items and has a rate-limit of 1 request per second. The script we've written is sending too many requests to the server in a short amount of time. Let's fix it!

The `requests` and `time` packages are already imported, and we've created the following variables for you:

```
longestTrackLength = 0
longestTrackTitle = ""
headers = {'Authorization': 'Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'}
page_number = 1
```

Instructions

- Start by running the exercise without making changes to the code, you'll notice that the console outputs a `429 Client Error` indicating we are sending too many requests to the server in a short amount of time.
- Fix the script by adding a **3 second pause** at the end of the while-loop using the `sleep` method from the `time` package.

Code:

```python
while True:
    params = {'page': page_number, 'per_page': 500}
    response = requests.get('http://localhost:3000/tracks', params=params, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    
    print(f'Fetching tracks page {page_number}')

    if len(response_data['results']) == 0:
        break

    for track in response_data['results']:
        if(track['Length'] > longestTrackLength):
            longestTrackLength = track['Length']
            longestTrackTitle = track['Name']

    page_number = page_number + 1
    
    # Add your fix here
    time.sleep(3)

print('The longest track in my music library is: ' + longestTrackTitle)
```

Output:

![image.png](image%2054.png)

You've found the longest track in your collection! It's a song from the Battlestar Galactica soundtrack!

# Final Thoughts

## 1. Final Thoughts

Congratulations on completing this introductory course on working with Python APIs! You now possess the foundational skills to integrate real-world data into your applications and automate workflows using external services.

---

## 2. API Basics

This section covered the fundamental "why" and "how" of web communication:

- **Role of APIs:** Enabling data sharing and interaction between different software systems over a network.
- **REST APIs:** The most common type of Web API, characterized by its use of URLs to identify resources.
- **URL Structure:** Using **paths** to locate specific resources and **query parameters** to filter or modify requests.
- **HTTP Verbs:** The "actions" of the web:
    - **GET:** Read
    - **POST:** Create
    - **PUT:** Update
    - **DELETE:** Remove

![image.png](image%2055.png)

---

## 3. APIs with Python (The `requests` Package)

We shifted from theory to practice by using the **requests** library to manage communication:

- **Method Functions:** `requests.get()`, `requests.post()`, etc.
- **Arguments:** Using `params` for query strings and `headers` for metadata.
- **Content Negotiation:** Using headers to request specific formats like **JSON** or **XML**.
- **Status Codes:** Monitoring the `.status_code` attribute to verify if a request succeeded (`2xx`) or failed (`4xx`/`5xx`).

![image.png](image%2056.png)

---

## 4. Advanced Topics

To handle real-world scenarios, we covered security and data formatting:

- **Authentication:** * **Basic Auth:** Username/Password (via the `auth` argument).
    - **API Keys/Tokens:** Identifiers passed via query parameters or headers.
- **Structured Data (JSON):** * The primary format for complex data.
    - Using the `json` argument to automatically encode Python dictionaries and set headers.

![image.png](image%2057.png)

---

## 5. Error Handling

We concluded by ensuring our code is robust enough to handle failures:

- **Connection Errors:** Network issues occurring before the request reaches the server.
- **4xx Client Errors:** Issues with the request (e.g., 401 Unauthorized, 404 Not Found).
- **5xx Server Errors:** Issues on the server side (e.g., 500 Internal Error).
- **Best Practice:** Combining `try/except` blocks with `.raise_for_status()` to catch both network exceptions and HTTP error codes.

![image.png](image%2058.png)