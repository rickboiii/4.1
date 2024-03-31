#!/usr/bin/env python3
# GitHub Lab 4: Unit Testing

# Import Modules
from main import Calculator
import random

# Global Variables
value_input = []
value_actual = []

def test_case1():
    "Case 1: Set & Validate Operand Values"
    
    # Case 1.1: Construct Object with Known Operands
    c = Calculator(1,2)
    assert c._operand1 == 1.0
    assert c.get_operand1() == 1.0
    assert c._operand2 == 2.0
    assert c.get_operand2() == 2.0

    # Case 1.2: Update with Known Operands via Setter Method
    c.set_operand1(4.5)
    c.set_operand2(9.7)
    assert c.get_operand1() == 4.5
    assert c.get_operand2() == 9.7

    # Case 1.3: Update with Unknown Operands via Setter Method
    v1 = random.randint(1,1000)
    v2 = random.uniform(1.1,1000.1)
    c.set_operand1(v1)
    c.set_operand2(v2)
    assert c.get_operand1() == v1
    assert c.get_operand2() == v2

def test_case2():
    # Case 2.1: Addition
    c = Calculator(3, 4)
    assert c.add() == 7

    # Case 2.2: Subtraction
    c.set_operand1(10)
    c.set_operand2(5)
    assert c.subtract() == 5

    # Case 2.3: Multiplication
    c.set_operand1(2.5)
    c.set_operand2(6)
    assert c.multiply() == 15

    # Case 2.4: Division
    c.set_operand1(20)
    c.set_operand2(4)
    assert c.divide() == 5
    pass

def test_case3():
    "Test Division by Zero Handling"
    # Create a Calculator object with operands 10 and 0
    c = Calculator(10, 0)
    
    # Attempt division by zero
    try:
        c.divide()
    except ZeroDivisionError:
        # If ZeroDivisionError is raised, the test passes
        pass
    else:
        # If no exception is raised, fail the test
        assert False, "Division by zero did not raise ZeroDivisionError"
    pass

def test_case4():
    "Case 4: TBD"
    pass

def test_case5():
    "Case 5: TBD"
    pass