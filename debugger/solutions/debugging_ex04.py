#!/usr/bin/env python3
""" A Solution For debugging_ex04
    Repeat Exercise 3, but start the debugger from the command line using
    Python’s -m option.
"""

# Below is the text of an interactive python shell that debugs the
# generate_dates.py program

"""
$ python3 -m pdb generate_dates.py
> generate_dates.py(2)<module>()
-> import datetime
(Pdb) next
> generate_dates.py(5)<module>()
-> def following_days(howmany):
(Pdb) next
> generate_dates.py(11)<module>()
-> def main():
(Pdb) next
> generate_dates.py(18)<module>()
-> if __name__ == "__main__":
(Pdb) next
> generate_dates.py(19)<module>()
-> main()
(Pdb) b 7
Breakpoint 1 at generate_dates.py:7
(Pdb) break 13
Breakpoint 2 at generate_dates.py:13
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
(Pdb) p howmany, now
(7, datetime.date(2021, 4, 16))
(Pdb) clear
Clear all breaks? yes
Deleted breakpoint 1 at generate_dates.py:7
Deleted breakpoint 2 at generate_dates.py:13
(Pdb) continue
2021-04-18
2021-04-19
2021-04-20
2021-04-21
2021-04-22
2021-04-23
The program finished and will be restarted
> generate_dates.py(2)<module>()
-> import datetime
(Pdb) q
"""
