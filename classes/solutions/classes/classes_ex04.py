""" A Solution For classes_ex04
    Implement the following class hierarchy.
    • Define a Worker class with a name, a salary, and number of years worked.
        • Provide a method named pension that returns an amount equal to the
          years worked times 10% of the salary.
        • Implement a name() method in the Worker class and have this be a
          default method for all derived classes.
    • Derive Manager from Worker.
        • A manager's pension is defined by the number of years worked times
          20% of the salary.
    • Derive Executive from Manager.
        • An executive's pension is defined by the number of years worked times
          30% of the salary.
"""


class Worker:
    def __init__(self, name, salary, years):
        self.name = name
        self.salary = salary
        self.years = years

    def pension(self):
        return self.years * .10 * self.salary

    def getname(self):
        return self.name


class Manager(Worker):
    def __init__(self, name, salary, years):
        super().__init__(name, salary, years)

    def pension(self):
        return self.years * .20 * self.salary


class Executive(Manager):
    def __init__(self, name, salary, years):
        super().__init__(name, salary, years)

    def pension(self):
        return self.years * .30 * self.salary


def main():
    workers = [Manager("Chris", 100000, 12),
               Executive("Susan", 100000, 7),
               Worker("Michael", 100000, 10)]

    fmt = "{:3} {:15.2f} {}"
    for idx, worker in enumerate(workers):
        print(fmt.format(idx, worker.pension(), worker.getname()))


if __name__ == "__main__":
    main()
