#!/usr/bin/env python3
long_names = ["January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"]
abbr_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
numdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

fmt = "{:^10} {:^10} {}"
print(fmt.format("#Days:", "Abbr Name:", "Long Name:"))
for days, abbr, lng in zip(numdays, abbr_names, long_names):
    print(fmt.format(days, abbr, lng))
