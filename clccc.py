

class Employee(object):
    """An employee in a department at CenturyLink

    Attributes:
        name: A string representing the person's name.
        allocation: warranted allocation for this employee
    """

    def __init__(self, name="", allocation=0, staff=[]):
        self.name = name
        self.allocation = allocation
        self.staff = staff

    def sum_allocation(self):
        return self.allocation + sum(map(lambda e: e.sum_allocation(), self.staff))


class Manager(Employee):
    pass

