#!/usr/bin/env python3
import decimal
import json
import requests

with open("movies.json", "r") as m:
    j = json.load(m, parse_float=decimal.Decimal)

movies = {}
for movie in j["movies"]:
    movies[movie["title"]] = movie["rating"]

seps = (',', ':')
with open("ratings.json", "w") as r:
    json.dump(movies, r, separators=seps,
              indent=2, sort_keys=True)

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
