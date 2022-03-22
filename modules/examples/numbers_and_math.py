#!/usr/bin/env python3
import math
import decimal
import random


def math_examples():
    print("Square Root of 10:", math.sqrt(10))
    print("64 to 3/2 pow:", math.pow(64, 1.5))
    print("Hypotenuse of 6 and 8:", math.hypot(6, 8))
    print("Smallest integer >= 2.5", math.ceil(2.5))
    print("Pi", math.pi)


def decimal_examples():
    print(".1 + .2 is not normally thought of as", .1 + .2)
    d1, d2 = decimal.Decimal(".1"), decimal.Decimal(".2")
    print("It is normally:", d1 + d2)


def random_examples():
    data = [9, 8, 7, 6, 5, 4, 3, 2]
    print(" float 0.0 <= x < 1.0:", random.random())
    print(" int from 0 to 9:", random.randrange(10))
    print(" choice ", data, ":", random.choice(data))
    random.shuffle(data)
    print(" shuffled", ":", data)
    print(" sample ", data, ":", random.sample(data, 4))
