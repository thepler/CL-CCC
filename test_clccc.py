def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

from clccc import Employee, Department

def test_simple():
    d = Employee('Developer', 'John Doe', 1000)
    assert d.name == 'John Doe'
    assert d.etype == 'Developer'
    assert d.allocation == 1000
    assert d.sum_allocation() == 1000
    m = Employee('Manager', 'John Doe2', 300, [d])
    assert m.name == 'John Doe2'
    assert m.etype == 'Manager'
    assert m.allocation == 300
    assert m.sum_allocation() == 1300
    d = Department('Yipee', [m])
    assert d.name == 'Yipee'
    assert d.sum_allocation() == 1300

def test_example():
    allocation = {'Developer':1000, 'QA Tester':500, 'Manager':300}
    employees = [
        ['Manager', 'Manager A'],
        ['Manager', 'Manager B'],
        ['Developer', 'Developer A'],
        ['QA Tester', 'QA Tester A'],
    ]
    d = Department('Cloudy Coders')
    for e in employees:
        d.add_staff([Employee(e[0], e[1], allocation[e[0]], [])])

