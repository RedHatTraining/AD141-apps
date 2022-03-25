#!/usr/bin/env python3
""" A Solution For debugging_ex01
    Debug an example from previous chapters by starting the debugger from
    within the interactive Python shell.

    • Step through the code using a combination of the step and next commands
      to get used to their behavior.
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
(Pdb) step
> generate_dates.py(12)main()
-> print("Code was run on:", datetime.date.today())
(Pdb) step
Code was run on: 2021-04-16
> generate_dates.py(13)main()
-> print("Next 7 days are:")
(Pdb) step
Next 7 days are:
> generate_dates.py(14)main()
-> for adate in following_days(7):
(Pdb) s
--Call--
> generate_dates.py(5)following_days()
-> def following_days(howmany):
(Pdb) s
> generate_dates.py(6)following_days()
-> now = datetime.date.today()
(Pdb) s
> generate_dates.py(7)following_days()
-> for i in range(1, howmany + 1):
(Pdb) s
> generate_dates.py(8)following_days()
-> yield now + datetime.timedelta(days=i)
(Pdb) s
--Return--
> generate_dates.py(8)following_days()->datetime.date(2021, 4, 17)
-> yield now + datetime.timedelta(days=i)
(Pdb) s
> generate_dates.py(15)main()
-> print(adate)
(Pdb) s
2021-04-17
> generate_dates.py(14)main()
-> for adate in following_days(7):
(Pdb) next
> generate_dates.py(15)main()
-> print(adate)
(Pdb) next
2021-04-18
> generate_dates.py(14)main()
-> for adate in following_days(7):
(Pdb) next
> generate_dates.py(15)main()
-> print(adate)
(Pdb) continue
2021-04-19
2021-04-20
2021-04-21
2021-04-22
2021-04-23
>>>

"""
