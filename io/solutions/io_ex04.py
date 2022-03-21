#!/usr/bin/env python3
""" A Solution For functions_ex04
    Rewrite Exercise 3 such that the file names are obtained from the command
    line if two arguments are supplied.
    • If the number of arguments is not two, then is should fall back on
      prompting the user for the filenames.
    • The interface might look like.
            python3 your_program_name.py inputfile outputfile
"""

import sys

if len(sys.argv) != 3:
    print("usage: inputfile outputfile")
    exit(1)

fin = open(sys.argv[1], "r")
fout = open(sys.argv[2], "w")

while True:
    line = fin.readline()
    if not line:
        break
    fout.write(line)

fin.close()
fout.close()
