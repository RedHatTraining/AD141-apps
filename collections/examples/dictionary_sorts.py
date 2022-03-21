#!/usr/bin/env python3
def get_value(akey):
    return states[akey]


states = {'New Hampshire': 'NH', 'Maryland': 'MD',
          'Nevada': 'NV', 'Maine': 'ME'}

# Sorted by Values
long_names = list(states.keys())
long_names.sort(key=get_value)
for name in long_names:
    print(name, states[name])
print()

# Sorted again by value without the need for custom function
long_names = list(states.keys())
long_names.sort(key=states.get)
for name in long_names:
    print(name, states[name])
print()
