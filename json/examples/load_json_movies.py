#!/usr/bin/env python3
import decimal
import json

with open("movies.json", "r") as m:
    j = json.load(m, parse_float=decimal.Decimal)

print(type(j))
print(type(j["movies"]))
print(j["movies"][0]["title"])
liked = j["movies"][0]["liked_it"]
print(type(liked), liked)
rating = j["movies"][1]["rating"]
print(type(rating), rating)

print()

for movie in j["movies"]:
    if movie["liked_it"] > 0.9:
        print(movie["title"])
