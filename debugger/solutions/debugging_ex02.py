#!/usr/bin/env python3
""" A Solution For debugging_ex02
    Use the list command with no arguments at some point when debugging the
    above code again to list the code around the currently executing line.

    • Repeat the process by passing a range large enough to the list command to
      list the entire file on the screen.

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
(Pdb) list
  7  	    for i in range(1, howmany + 1):
  8  	        yield now + datetime.timedelta(days=i)
  9
 10
 11  	def main():
 12  ->	    print("Code was run on:", datetime.date.today())
 13  	    print("Next 7 days are:")
 14  	    for adate in following_days(7):
 15  	        print(adate)
 16
 17
(Pdb) list 1, 20
  1  	#!/usr/bin/env python3
  2  	import datetime
  3
  4
  5  	def following_days(howmany):
  6  	    now = datetime.date.today()
  7  	    for i in range(1, howmany + 1):
  8  	        yield now + datetime.timedelta(days=i)
  9
 10
 11  	def main():
 12  ->	    print("Code was run on:", datetime.date.today())
 13  	    print("Next 7 days are:")
 14  	    for adate in following_days(7):
 15  	        print(adate)
 16
 17
 18  	if __name__ == "__main__":
 19  	    main()
[EOF]
(Pdb) continue
Code was run on: 2021-04-16
Next 7 days are:
2021-04-17
2021-04-18
2021-04-19
2021-04-20
2021-04-21
2021-04-22
2021-04-23
>>>

"""
