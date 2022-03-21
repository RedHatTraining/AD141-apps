#!/usr/bin/env python3
""" A Solution For functions_ex08
    Now, create a few more files file with one name per line.
    • The program in this exercise should read all these files and print the
      number of times each line occurs over all of the files.
    • The file names should be supplied on the command line.
    • The following files are available in the starter directory for this
      chapter in the labfiles and can be used if desired:
            names_a.txt
            names_b.txt
            names_c.txt
            names_d.txt
    • Output from the program would look similar to the following:
            Alice   4
            Bart    2
            Beverly 1
            Bill    4
            Chris   2
            Dave    1
            Frank   3
            Jane    3
            John    2
            Mary    1
            Mike    4
            Peter   3
            Susan   2
"""

import sys

hash = {}

for filename in sys.argv[1:]:
    f1 = open(filename, "r")
    for line in f1:
        line = line.strip()
        if line in hash:
            hash[line] += 1
        else:
            hash[line] = 1

names = list(hash.keys())
names.sort()

for name in names:
    print(f"{name:10}{hash[name]:4}")
