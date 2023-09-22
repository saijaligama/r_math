import math
import re


class TrigonometricCalculator:
    def __init__(self, unit="radians"):
        self.unit = unit

    def calculate_expression(self, expression):
        try:
            # Ensure the input expression is lowercase for case-insensitivity
            expression = expression.lower()

            # Replace common trig function names with their math module equivalents
            expression = expression.replace("sin", "math.sin")
            expression = expression.replace("cos", "math.cos")
            expression = expression.replace("tan", "math.tan")
            result = 'Nan'
            if self.unit == "radians":
                print('In radians function')
                expression = expression.replace("pi", "math.pi")
                result = eval(expression)
            else:
                print("in degrees function")
                temp = re.findall(r'\((.*?)\)', expression)[0]
                temp = float(temp)
                func = expression.split('(')[0]
                result = eval(f'{func}(math.radians({temp}))')

            # Convert degrees to radians if necessary
            # if self.unit == "degrees":
            #     expression = expression.replace("deg(", "math.radians(")

            # Use eval to calculate the expression

            return result
        except Exception as e:
            return f"Error: {str(e)}"
