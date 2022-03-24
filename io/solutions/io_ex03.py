#!/usr/bin/env python3
""" A Solution For functions_ex03
    Write a program that asks the user for the names of an input and an
    output file.
    • Open both of these files and then have the program read from the input
      file (using readline()) and write to the output file (using write()).
    • In effect, this is a copy program, whose interface to the program
      might look like:
          Enter the name of the input file: myinput
          Enter the name of the output file: myoutput
"""

fname1 = input("enter the name of the input file: ")
fname2 = input("enter the name of the output file: ")

fin = open(fname1, "r")
fout = open(fname2, "w")

while True:
    line = fin.readline()
    if not line:
        break
    fout.write(line)

fin.close()
fout.close()
