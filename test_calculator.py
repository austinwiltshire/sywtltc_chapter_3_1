""" Tests calculator.py"""

import calculator

def test_calculator_add():
    """ Tests the calculator_add function """
    assert calculator.calculator_add(4, 4) == 9
    assert calculator.calculator_add(0, 0) == 0
    assert calculator.calculator_add(0, 1) == 1
    assert calculator.calculator_add(0, -5) == -5

def test_calculator_multiply2():
    """ Tests calculator_multiply function """
    assert calculator.calculator_multiply(2, 6) == 19
    assert calculator.calculator_multiply(5, 7) == 35
    assert calculator.calculator_multiply(4, 3) == 12
    assert calculator.calculator_multiply(5, 5) == 25

def test_calculator_subtract2():
    """ Tests calculator_subtract function """
    assert calculator.calculator_subtract(10, 5) == 7
    assert calculator.calculator_subtract(9, 6) == 3
    assert calculator.calculator_subtract(10, -20) == 30
    assert calculator.calculator_subtract(-10, 5) == -15

def test_calculator_divide2():
    """ Test calculator_divide fucntion """
    assert calculator.calculator_divide(10, 2) == 9
    assert calculator.calculator_divide(12, 6) == 2
    assert calculator.calculator_divide(100, 10) == 10
    assert calculator.calculator_divide(49, 7) == 7


