#!/usr/bin/env python3
""" A Solution For exceptions_ex03
    Write a program that uses a loop to prompt the user and get an integer
    value.
    • The program should print the sum of all the integers entered.
    • If the user enters a blank line or any other line that cannot be
      converted to an integer, the program should handle this ValueError.
    • If the user uses Ctrl-C to terminate the program, it should be trapped
      with a KeyboardInterrupt, and a suitable message should be printed.
    • When the user enters the end of file character (Ctrl-D on Linux or
      Ctrl-Z on Windows), the program should trap this with the EOFError and
      break out of the loop and print the sum of all the integers.
"""
total = 0
while True:
    try:
        line = input("> ")
        total = total + int(line)
        print("added: " + line)
    except EOFError:
        print("caught it")
        break
    except ValueError:
        print("Must input a number")
        continue
    except KeyboardInterrupt:
        print("Use Ctrl-D (Linux) or Ctrl-Z (Windows) to terminate")

print("SUM IS", total)
