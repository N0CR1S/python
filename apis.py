import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit(1)

response = requests.get("https://itunes.apple.com/us/search?entity=song&limit=100&term=" + sys.argv[1])

output = response.json()
for result in output['results']:
    print(result['trackName'])
#    print(result['artistName'])
#    print(result['collectionName'])
#    print(result['releaseDate'])
#    print(result['primaryGenreName'])
