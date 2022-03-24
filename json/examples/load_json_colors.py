#!/usr/bin/env python3
import decimal
import json

with open("colors.json", "r") as m:
    j = json.load(m, parse_float=decimal.Decimal)

print(type(j))
print(type(j["colors"]))
print(j["colors"][0]["name"])
value = j["colors"][0]["value"]
print(type(value), value)

print()

for color in j["colors"]:
    if "e" in color["name"]:
        print(color["name"])
