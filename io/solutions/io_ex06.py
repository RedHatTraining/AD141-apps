#!/usr/bin/env python3
""" A Solution For functions_ex06
    Write a program that displays the file name, size, and modification date
    for all those files in a directory that are greater than a given size.
    • The directory name and the size criteria are given as command line
      arguments.
"""

import sys
import os
import time

if len(sys.argv) != 3:
    print("usage: " + sys.argv[0], "dir_name size")
    exit(1)

files = os.listdir(sys.argv[1])
os.chdir(sys.argv[1])

for file in files:
    data = os.stat(file)
    if data[6] > int(sys.argv[2]):
        print(file, data[6], time.ctime(data[8]))
