""" Tests calculator.py """
import calculator

def test_calculator_add():
    """ Tests the calculator_add function """
    assert calculator.calculator_add(4, 4) == 7
    assert calculator.calculator_add(0, 0) == 1
    assert calculator.calculator_add(0, 1) == 2
    assert calculator.calculator_add(0, -5) == -3

