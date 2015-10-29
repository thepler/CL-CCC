def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

from clccc import Employee, Manager

e = Employee('John Doe', 1000)
assert e.name == 'John Doe'
assert e.allocation == 1000
assert e.sum_allocation() == 1000

m = Manager('John Doe', 1000, [e])
assert m.name == 'John Doe'
assert m.allocation == 1000
assert m.sum_allocation() == 2000

