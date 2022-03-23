#!/usr/bin/env python3
""" A Solution For data_structures_ex04
    Suppose there is a file of three values per line.
    • The values are whitespace separated as follows.
        ▶ OwnerName ComputerType ComputerValue
    • Read the lines and make a dictionary of dictionaries so the keys are the
      owner and the values are a dictionary consisting of the computer type as
      the key and the computer value as the value.
    • Finally, print the dictionary.
    • The dataset might look as follows.

            Joe Desktop 500
            Joe Laptop 200
            Joe Desktop 400
            Mary Desktop 200
            Mary Laptop 800
            Beth Laptop 500
            Beth Tablet 250
            Joe Tablet 250
    • The output might look as follows.
            {
            'Mary': {'Desktop': 200, 'Laptop': 800},
            'Beth': {'Tablet': 250, 'Laptop': 500},
            'Joe': {'Desktop': 900, 'Tablet': 250, 'Laptop': 200}
            }
"""

import sys
file = open("DATA", "r")

lines = file.readlines()
file.close()

map = {}

for line in lines:
    name, typ, amount = line.split()
    ctm = map.get(name)
    if ctm:
        value = ctm.get(typ)
        if value:
            ctm[typ] += int(amount)
        else:
            ctm[typ] = int(amount)
    else:
        map[name] = {typ: int(amount)}

print(map)
