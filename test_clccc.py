
import sys
from clccc import Employee, Department

def test_simple():
    d = Employee('Developer', 'John Doe', 1000, [])
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

def make_department(name, employees, allocation):
    d = Department(name, [])
    for e in employees:
        x = d
        if len(e) > 2:
            # find the manager
            x = d.find_employee_by_name(e[2])

        e = Employee(e[0], e[1], allocation[e[0]], [])
        x.add_staff([e])

    return d

def test_example():
    allocation = {'Developer':1000, 'QA Tester':500, 'Manager':300}
    # optional 3rd column is the manager, which must be
    # declared before the employee
    employees = [
        ['Manager', 'Manager A'],
        ['Manager', 'Manager B', 'Manager A'],
        ['Developer', 'Developer A', 'Manager B'],
        ['QA Tester', 'QA Tester A', 'Manager B'],
    ]
    d = make_department('Cloudy Coders', employees, allocation)
    assert d.sum_allocation() == 2100
    return d

def test_deeper():
    allocation = {'Developer':1200, 'QA Tester':1500, 'Manager':1900}
    # optional 3rd column is the manager, which must be
    # declared before the employee
    departments = {
        'Cloudy Coders' : [
            ['Manager', 'Manager A'],
            ['Manager', 'Manager B', 'Manager A'],
            ['Developer', 'Developer A', 'Manager B'],
            ['QA Tester', 'QA Tester A', 'Manager B'],
        ],
        'Fluffy Typers' : [
            ['Manager', 'Big Kahuna'],
            ['Manager', 'Pointy Director'],
            ['Manager', 'NotQuiteAs Big', 'Big Kahuna'],
            ['Manager', 'Biff Biffer', 'Big Kahuna'],
            ['Developer', 'Devin Dev', 'Biff Biffer'],
            ['Manager', 'Mary Lamb', 'Pointy Director'],
            ['Manager', 'Leafy Blue', 'Pointy Director'],
            ['Developer', 'Type-y Typer', 'Mary Lamb'],
            ['Developer', 'Tappy Tapper', 'Mary Lamb'],
            ['QA Tester', 'Bam Bam', 'Mary Lamb'],
            ['QA Tester', 'Pebbles', 'Mary Lamb'],
            ['Developer', 'Sarah Desert', 'Leafy Blue'],
            ['QA Tester', 'Shiny Window', 'Leafy Blue'],
            ['Manager', 'Manny McMan', 'NotQuiteAs Big'],
            ['QA Tester', 'QQQQQ AAAAA', 'Manny McMan'],
            ['Developer', 'Imouta Names', 'Manny McMan'],
        ],
    }
    d = []
    for name, employees in departments.items():
        d.append(make_department(name, employees, allocation))

    assert d[0].sum_allocation() == 6500
    assert d[1].sum_allocation() == 25300

    return d

if __name__=="__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'example':
            d = test_example()
            print d
        elif sys.argv[1] == 'deeper':
            d = test_deeper()
            print d[0]
            print d[1]
        else :
            pass
    else:
        test_simple()
        test_example()
        test_deeper()
