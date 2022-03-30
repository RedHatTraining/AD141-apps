#!/usr/bin/env python3
import decimal
import json
import requests

# get the current location of the ISS
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.content.decode())
    with open("api_data.json", "w") as r:
        json.dump(data, r, skipkeys=True,
                  separators=seps, indent=2)
else:
    print("response status:", response.status_code)

print("Done")
