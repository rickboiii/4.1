#!/usr/bin/env python3
# GitHub Lab 4: Unit Tests

class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations
    (addition, subtraction, multiplication, division) with two operands.
    """

    def __init__(self, operand1, operand2):
        """
        Initializes the Calculator instance with two operands.

        Parameters:
        - operand1 (float): The first operand.
        - operand2 (float): The second operand.
        """
        self._operand1 = operand1
        self._operand2 = operand2

    # Getter methods
    def get_operand1(self):
        """
        Get the value of the first operand.

        Returns:
        float: The value of the first operand.
        """
        return self._operand1

    def get_operand2(self):
        """
        Get the value of the second operand.

        Returns:
        float: The value of the second operand.
        """
        return self._operand2

    # Setter methods
    def set_operand1(self, value):
        """
        Set the value of the first operand.

        Parameters:
        - value (float): The new value for the first operand.
        """
        self._operand1 = float(value)

    def set_operand2(self, value):
        """
        Set the value of the second operand.

        Parameters:
        - value (float): The new value for the second operand.
        """
        self._operand2 = float(value)

    # Arithmetic operations
    def add(self):
        """
        Perform addition of the two operands.

        Returns:
        float: The result of the addition.
        """
        return self._operand1 + self._operand2

    def subtract(self):
        """
        Perform subtraction of the second operand from the first operand.

        Returns:
        float: The result of the subtraction.
        """
        return self._operand1 - self._operand2

    def multiply(self):
        """
        Perform multiplication of the two operands.

        Returns:
        float: The result of the multiplication.
        """
        return self._operand1 * self._operand2

    def divide(self):
        """
        Perform division of the first operand by the second operand.

        Returns:
        float or str:   The result of the division or an error message if
                        attempting to divide by zero.
        """
        if self._operand2 != 0:
            return self._operand1 / self._operand2
        else:
            return "Cannot divide by zero"


# DO NOT MODIFY BELOW
if __name__ == "__main__":
    # Create Object and Use the Class
    calculator = Calculator(5, 3)

    print("Operand 1:", calculator.get_operand1())
    print("Operand 2:", calculator.get_operand2())

    print("Addition:", calculator.add())
    print("Subtraction:", calculator.subtract())
    print("Multiplication:", calculator.multiply())
    print("Division:", calculator.divide())

    # Updating operands using setter methods
    calculator.set_operand1(10)
    calculator.set_operand2(2)

    print("Updated Operand 1:", calculator.get_operand1())
    print("Updated Operand 2:", calculator.get_operand2())

    print("Addition:", calculator.add())
    print("Subtraction:", calculator.subtract())
    print("Multiplication:", calculator.multiply())
    print("Division:", calculator.divide())
