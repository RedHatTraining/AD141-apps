#!/usr/bin/env python3
originals = [[3, 1, -10, 54, 75, 29],
             ("Cheese", "Pepperoni", "Bacon", "Mushrooms"),
             {"AL", "NY", "MD", "VA", "PA", "KY", "VT"},
             {'New Hampshire': 'NH', 'Maryland': 'MD',
              'Nevada': 'NV', 'Maine': 'ME'}]

print("Original Collections")
for collection in originals:
    print(collection)
print()
for collection in originals:
    sorted_list = sorted(collection)
    print(type(collection).__name__, "sorted:", sorted_list)
print()
print("Original Collections")
for collection in originals:
    print(collection)
