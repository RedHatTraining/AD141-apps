#!/usr/bin/env python3
""" A Solution For debugging_ex03
    Debug a program of your choosing again by assigning several breakpoints
    within the debugger using the b command.


    • Use the continue command to have the debugger stop at the breakpoints and
    then use the p command to print out the values of the various variable
    available within the context of the current line.
"""

# Below is the text of an interactive python shell that debugs the
# generate_dates.py program

"""
$ python3
>>> import pdb
>>> import generate_dates
>>> pdb.run('generate_dates.main()')
> <string>(1)<module>()
(Pdb) step
--Call--
> generate_dates.py(11)main()
-> def main():
(Pdb) b 13
Breakpoint 1 at generate_dates.py:13
(Pdb) b  7
Breakpoint 2 at generate_dates.py:7
(Pdb) continue
Code was run on: 2021-04-16
> generate_dates.py(13)main()
-> print("Next 7 days are:")
(Pdb) continue
Next 7 days are:
> generate_dates.py(7)following_days()
-> for i in range(1, howmany + 1):
(Pdb) p howmany, now
(7, datetime.date(2021, 4, 16))
(Pdb) continue
2021-04-17
> generate_dates.py(7)following_days()
-> for i in range(1, howmany + 1):
(Pdb) clear
Clear all breaks? Yes
Deleted breakpoint 1 at generate_dates.py:13
Deleted breakpoint 2 at generate_dates.py:7
(Pdb) continue
2021-04-18
2021-04-19
2021-04-20
2021-04-21
2021-04-22
2021-04-23
>>>
"""
