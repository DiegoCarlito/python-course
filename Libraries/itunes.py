# JSON: JavaScript Object Notation
# - standard text format
# - language agnostic format exchangig datas between computers

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

# get some response from a server
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])