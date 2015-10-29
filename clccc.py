

class Person(object):
    """A person in a department at CenturyLink

    Attributes:
        name: A string representing the person's name.
        allocation: warranted allocation for this person
    """

    def __init__(self, name="", allocation=0):
        self.name = name
        self.allocation = allocation

