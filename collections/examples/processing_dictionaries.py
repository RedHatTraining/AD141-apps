#!/usr/bin/env python3
reward_pts = {"Bryce": 500, "Heather": 2000, "Kaylie": 750,
              "Amanda": 1350, "Casey": 2400, "Jason": 800,
              "Kaylie": 25}
rule, prefix = "-" * 75, "\n"

print("Looping through dictionary", rule, sep=prefix)
for name in reward_pts:
    print(name, reward_pts[name])

print(prefix, "Looping through keys()", rule, sep=prefix)
for name in reward_pts.keys():
    print(name, end=" ")

print(prefix, "Looping through values()", rule, sep=prefix)
for value in reward_pts.values():
    print(value, end=" ")

print(prefix, "Looping through items() as tuples", rule,
      sep=prefix)
for item in reward_pts.items():
    print(item)

fmt = "{:8}~{:>8}"
print(prefix, "Items() unpacked as keys and values", rule,
      sep=prefix)
print(fmt.format("Name", "Points"))
for name, points in reward_pts.items():
    print(fmt.format(name, points))

print(prefix, "Data types of returned views", rule,
      sep=prefix)
print("  keys()", type(reward_pts.keys()))
print("values()", type(reward_pts.values()))
print(" items()", type(reward_pts.items()))
