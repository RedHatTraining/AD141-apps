#!/usr/bin/env python3
names = """Smith Johnson Williams Brown Jones Miller Lee
Garcia Rodriguez Wilson Martinez Anderson Taylor
Thomas Hernandez Moore Martin Jackson Thompson
White Lopez Davis"""
names = names.split()
# Primary sort by name ("Alphabetically)
names.sort()
# Secondary sort by length
names.sort(key=len)
print(names)
