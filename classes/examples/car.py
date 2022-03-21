#!/usr/bin/env python3
class Car:

    quantity = 0  # Class variable shared by all instances

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.odometer = 0
        Car.quantity += 1

    def __del__(self):
        Car.quantity -= 1

    def drive(self, miles):
        self.odometer += miles

    def __str__(self):
        data = [self.make, self.model, " ~ Odometer:", str(self.odometer)]
        return " ".join(data)
