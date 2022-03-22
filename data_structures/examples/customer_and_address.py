#!/usr/bin/env python3
class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return "".join([self.street, "\n", self.city, ", ", self.state, " ",
                       self.zip])


class Customer:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __str__(self):
        return "".join([self.first_name, " ", self.last_name, "\n",
                       str(self.address)])
