

class Employee(object):
    """An employee in a department at CenturyLink

    Attributes:
        name: A string representing the person's name.
        allocation: warranted allocation for this employee
    """

    # XXX use a set instead of a list to make sure no duplicates?

    def __init__(self, etype="", name="", allocation=0, staff=[]):
        self.name = name
        self.allocation = allocation
        self.staff = staff
        self.etype = etype

    def add_staff(self, more=[]):
        self.staff.extend(more)

    def sum_allocation(self):
        return self.allocation + sum(map(lambda e: e.sum_allocation(), self.staff))


class Department(object):
    """A department at CenturyLink

    Attributes:
        name: name of this department
        staff: list of employees in this department
    """
    def __init__(self, name="", staff=[]):
        self.name = name
        self.staff = staff

    def add_staff(self, more=[]):
        self.staff.extend(more)

    def sum_allocation(self):
        return sum(map(lambda e: e.sum_allocation(), self.staff))

