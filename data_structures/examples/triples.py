#!/usr/bin/env python3
def main():
    alist = [2, 4, 6]
    print([3 * x for x in alist])
    print([3 * x for x in [1, 2, 3, 4, 5]])
    print([3 * x for x in range(1, 5)])
    print([[x, 3 * x] for x in range(1, 5)])


if __name__ == "__main__":
    main()
