""" Tests calculator.py """
import calculator

def test_calculator_add():
    """ Tests the calculator_add function """
    assert calculator.calculator_add(4, 4) == 8
    assert calculator.calculator_add(0, 0) == 0
    assert calculator.calculator_add(0, 1) == 1
    assert calculator.calculator_add(0, -5) == -5
def test_calculator_subtract():
    """ Test subtraction function """
    assert calculator.calculator_subtract(8, 2) == 6
    assert calculator.calculator_subtract(8, 4) == 4
    assert calculator.calculator_subtract(20, 4) == 16
    assert calculator.calculator_subtract(10, 1) == 9
def test_calculator_multiply():
    """ Test multiply function """
    assert calculator.calculator_multiply(2, 2) == 4
    assert calculator.calculator_multiply(4, 4) == 16
    assert calculator.calculator_multiply(10, 10) == 100
    assert calculator.calculator_multiply(5, 5) == 25
def test_calculator_divide():
    """ Test divide function """
    assert calculator.calculator_divide(10, 2) == 5
    assert calculator.calculator_divide(4, 2) == 2
    assert calculator.calculator_divide(10, 5) == 2
    assert calculator.calculator_divide(20, 2) == 10
def test_calculator_square():
    assert calculator.calculator_square(5) == 25
