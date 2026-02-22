#Instructions

# Start by running the exercise without making changes to the code, you'll notice that the console outputs a `429 Client Error` indicating we are sending too many requests to the server in a short amount of time.
# Fix the script by adding a **3 second pause** at the end of the while-loop using the `sleep` method from the `time` package.

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