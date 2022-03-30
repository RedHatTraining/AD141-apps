#!/usr/bin/env python3
import decimal
import json

data = '{"x": 0.1, "y": 0.2}'
j = json.loads(data)
j_x = j["x"]
j_y = j["y"]
print(type(j), type(j_x), j_x, sep=", ")
print(j_x + j_y)

j = json.loads(data, parse_float=decimal.Decimal)
j_x = j["x"]
j_y = j["y"]
print(type(j), type(j_x), j_x, sep=", ")
print(j_x + j_y)

data = '{"name": "Jill", "age": 33, "state": "MD"}'
j = json.loads(data, parse_int=str)
print(type(j["age"]), j["age"], sep=", ")
