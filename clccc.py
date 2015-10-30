
class Employee(object):
    """An employee in a department at CenturyLink

    Attributes:
        name: A string representing the person's name.
        allocation: warranted allocation for this employee
        etype: the employee type (Manager, Developer, etc)
        staff: list of employees that report to this employee
    """

    # XXX use a set instead of a list to make sure no duplicates?

    def __init__(self, etype, name, allocation, staff):
        self.allocation = allocation
        self.etype = etype
        self.name = name
        self.staff = staff

    def sum_allocation(self):
        return self.allocation + sum(map(lambda e: e.sum_allocation(), self.staff))

    def __str__(self):
        return "%s, %s, %i, %i, %i" % (self.etype, self.name, self.allocation, self.sum_allocation(),len(self.staff))

    def add_staff(self, more):
        self.staff.extend(more)

    def find_employee_by_name(self, name):
        if self.name == name:
            return self

        for e in self.staff:
            found = e.find_employee_by_name(name)
            if found:
                return found

class Department(object):
    """A department at CenturyLink

    Attributes:
        name: name of this department
        staff: list of top level employees in this department
    """

    def __init__(self, name, staff):
        self.name = name
        self.staff = staff

    def sum_allocation(self):
        return sum(map(lambda e: e.sum_allocation(), self.staff))

    def __str__(self):
        s = ["%s, %i" % (self.name, self.sum_allocation())]
        for e in self.staff:
            s.extend(self.__emp_str(1, e))

        return "\n".join(s)

    def __emp_str(self, level, e):
        all = ["  " * level + e.__str__()]
        for s in e.staff:
            all.extend(self.__emp_str(level + 1, s))

        return all

    def add_staff(self, more):
        self.staff.extend(more)

    def find_employee_by_name(self, name):
        if self.name == name:
            return self

        for e in self.staff:
            found = e.find_employee_by_name(name)
            if found:
                return found

