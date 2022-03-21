#!/usr/bin/env python3
results = filter(lambda x: x % 3 == 0, range(2, 51))

for value in results:
    print(value, end=' ')
print()
