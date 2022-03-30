#!/usr/bin/env python3
import json

data = '{"name": "Jill", "age": 33, "state": "MD"}'
j = json.loads(data)
print(type(j), j["state"])
print(type(j["age"]))

d = {"name": "Joe", "age": 57, "state": "PA"}
j = json.dumps(d)
print(type(j), j)
