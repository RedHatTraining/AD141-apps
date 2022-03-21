#!/usr/bin/env python3
class Employee:
    pass


class Manager(Employee):
    pass


class Executive(Manager):
    pass


def main():
    manager = Manager()

    print(isinstance(manager, Employee))      # True
    print(isinstance(manager, Manager))       # True
    print(isinstance(manager, Executive))     # False

    print(issubclass(Executive, Executive))   # True
    print(issubclass(Executive, Manager))     # True
    print(issubclass(Executive, Employee))    # True
    print(issubclass(Executive, object))      # True


if __name__ == "__main__":
    main()
