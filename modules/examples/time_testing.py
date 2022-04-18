#!/usr/bin/env python3
import time


def counters():
    return(time.perf_counter(), time.process_time())


def main():
    starts = counters()
    print("time.time():", time.time())
    print("time.ctime():", time.ctime())
    print()
    now = time.localtime()
    f = "{0}/{1}/{2}"
    # struct_time values by property
    print("struct_time values by property and index")
    print(f.format(now.tm_mon, now.tm_mday, now.tm_year))

    # struct_time values by tuple index
    print(f.format(now[1], now[2], now[0]))
    print()
    # Formatting of struct_time objects
    print("time.strftime() examples:")
    print("Format: %m/%d/%Y\tResult: ",
          time.strftime("%m/%d/%Y", now))
    print("Format: %A %B %d\tResult: ",
          time.strftime("%A %B %d", now))
    print()
    time.sleep(5)
    ends = counters()
    print()
    print("Performance:", ends[0] - starts[0], "seconds")
    print("Process:", ends[1] - starts[1], "seconds")


if __name__ == "__main__":
    main()
