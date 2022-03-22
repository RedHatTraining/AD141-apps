#!/usr/bin/env python3
def main():
    names = ["Ashley", "Emma", "Jayden", "Ethan"]
    print({name: len(name) for name in names})


if __name__ == "__main__":
    main()   # Output: {'Jayden': 6, 'Ethan': 5, 'Ashley': 6, 'Emma': 4}
