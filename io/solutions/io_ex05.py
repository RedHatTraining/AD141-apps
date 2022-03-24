#!/usr/bin/env python3
""" A Solution For functions_ex05
    Add exception handling to the previous exercise so that if a file open
    fails, an OSError is handled and the program is halted
"""

import sys

if len(sys.argv) != 3:
    print("usage: inputfile outptfile")
    exit(1)

try:
    fin = open(sys.argv[1], "r")
    fout = open(sys.argv[2], "w")
except IOError as ioe:
    print("File open failed: ", ioe)
    exit(2)

while True:
    line = fin.readline()
    if not line:
        break
    fout.write(line)

fin.close()
fout.close()
