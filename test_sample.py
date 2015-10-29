def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

from clccc import Person

p = Person('John Doe', 1000)
assert p.name == 'John Doe'
assert p.allocation == 1000
