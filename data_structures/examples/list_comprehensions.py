#!/usr/bin/env python3
def main():
    sample = [hex(x) for x in range(0, 16)]
    print(type(sample), sample, sep="\t")
    print([(x, x * x) for x in range(2, 7)])
    print([x * x for x in range(1, 16) if x % 2 == 0])


if __name__ == '__main__':
    main()
