""" Tests calculator.py"""

import calculator

def test_calculator_add():
    """ Tests the calculator_add function """
    assert calculator.calculator_add(4, 4) == 8
    assert calculator.calculator_add(0, 0) == 0
    assert calculator.calculator_add(0, 1) == 1
    assert calculator.calculator_add(0, -5) == -5

def test_calculator_multiply():
    """ Tests calculator_multiply function """
    assert calculator.calculator_multiply(2, 6) == 12
    assert calculator.calculator_multiply(5, 7) == 35
    assert calculator.calculator_multiply(4, 3) == 12
    assert calculator.calculator_multiply(5, 5) == 25

def test_calculator_subtract():
    """ Tests calculator_subtract function """
    assert calculator.calculator_subtract(10, 5) == 5
    assert calculator.calculator_subtract(9, 6) == 3
    assert calculator.calculator_subtract(10, -20) == 30
    assert calculator.calculator_subtract(-10, 5) == -15

def test_calculator_divide():
    """ Test calculator_divide fucntion """
    assert calculator.calculator_divide(10, 2) == 5
    assert calculator.calculator_divide(12, 6) == 2
    assert calculator.calculator_divide(100, 10) == 10
    assert calculator.calculator_divide(49, 7) == 7


