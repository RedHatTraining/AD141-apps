#!/usr/bin/env python3
'''
json_ex4.py

The following API endpoint will return JSON data that contains a random fact
about a number sent to it:
  http://numbersapi.com/a_number/?json&notfound=floor
Write a program that makes an HTTP request to the API.
The program should display the fact that was returned in the JSON data.
'''

import json
import requests
from random import randint


def main():
    url = f"http://localhost:5000/numbers?number={randint(1, 10)}"
    print(f"sending request {url} ...")
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode())
        print(data["data"])
    else:
        print("response status:", response.status_code)


if __name__ == "__main__":
    main()
