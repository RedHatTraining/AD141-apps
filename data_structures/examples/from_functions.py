#!/usr/bin/env python3
def main():
    names = ["Ashley", "Emma", "Jayden", "Ethan"]
    print([len(name) for name in names])
    print([[name, len(name)] for name in names])
    grades = [[88, 77, 99], [95, 98, 97], [79, 100, 95]]
    highest = [max(grade) for grade in grades]
    print(highest)


if __name__ == "__main__":
    main()
