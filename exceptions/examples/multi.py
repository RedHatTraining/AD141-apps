#!/usr/bin/env python3
def main():
    names = ['Mike', 'John',  'Jane',  'Alice']
    themap = {'Mike': 15, 'Chris': 10, 'Dave': 25}

    while True:
        try:
            value = input("Enter an integer: ")
            if value == "end":
                break
            value = int(value)
            print("Name is: " + names[value])
            name = input("Enter a name: ")
            print(name, " => ", themap[name])
        except ValueError:
            print("Value Error: non numeric data")
        except (KeyError, IndexError) as err:
            # Above could be written as:
            #      except LookupError as err:
            print("Illegal value:", err)
        except Exception:
            print("Unknown Exception: ")


if __name__ == "__main__":
    main()
