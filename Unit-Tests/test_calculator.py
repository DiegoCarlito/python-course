# pip install pytest
# Unit Tets: way of testing the smallest piece of code that can be logically isolated in a system
# - a function, a subrotine, a method or property
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
