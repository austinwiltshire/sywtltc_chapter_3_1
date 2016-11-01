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
