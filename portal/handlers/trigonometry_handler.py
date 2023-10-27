# import math
# import re
from fractions import Fraction

import sympy as sp
#
#
# class TrigonometricCalculator:
#     def __init(self, unit="radians"):
#         self.unit = unit
#
#     def calculate_expression(self, expression):
#         try:
#             # Ensure the input expression is lowercase for case-insensitivity
#             expression = expression.lower()
#
#             # Replace common trig function names with their math module equivalents
#             expression = expression.replace("sin", "math.sin")
#             expression = expression.replace("cos", "math.cos")
#             expression = expression.replace("tan", "math.tan")
#
#             if self.unit == "radians":
#                 expression = expression.replace("pi", "math.pi")
#                 result = eval(expression)
#             else:
#                 temp = re.findall(r'\((.*?)\)', expression)[0]
#                 temp = float(temp)
#                 func = expression.split('(')[0]
#                 result = eval(f'{func}(math.radians({temp}))')
#
#             # Convert the result to a fraction
#             result_fraction = Fraction(result).limit_denominator()
#
#             return result_fraction
#         except Exception as e:
#             return f"Error: {str(e)}"

import math
import re
import sympy

class TrigonometricCalculator:
    def __init__(self, unit="radians"):
        self.unit = unit

    def calculate_trig_value(self, trig_input):
        trig_function, angle_str = trig_input[:3], trig_input[3:]
        angle = int(angle_str)

        angle_rad = sp.rad(angle)

        if trig_function == 'sin':
            trig_value = sp.sin(angle_rad)
        elif trig_function == 'cos':
            trig_value = sp.cos(angle_rad)
        elif trig_function == 'tan':
            trig_value = sp.tan(angle_rad)
        elif trig_function == 'cot':
            trig_value = 1 / sp.tan(angle_rad)
        elif trig_function == 'sec':
            trig_value = 1 / sp.cos(angle_rad)
        elif trig_function == 'csc':
            trig_value = 1 / sp.sin(angle_rad)
        else:
            raise ValueError("Invalid trigonometric function")

        return str(trig_value)
    def trig_fractions(self,trig_func):

        sin_vals = {
            0: '0',
            15: '1/4',
            30: '1/2',
            45: 'sqrt(2)/2',
            60: 'sqrt(3)/2',
            75: 'sqrt(2)/2',
            90: '1',
            105: 'sqrt(2)/2',
            120: 'sqrt(3)/2',
            135: 'sqrt(2)/2',
            150: '1/2',
            165: '1/4',
            180: '0',
            195: '-1/4',
            210: '-1/2',
            225: '-sqrt(2)/2',
            240: '-sqrt(3)/2',
            255: '-sqrt(2)/2',
            270: '-1',
            285: '-sqrt(2)/2',
            300: '-sqrt(3)/2',
            315: '-sqrt(2)/2',
            330: '-1/2',
            345: '-1/4',
            360: '0'
        }

        cos_vals = {
            0: '1',
            15: 'sqrt(3)/4',
            30: 'sqrt(3)/2',
            45: 'sqrt(2)/2',
            60: '1/2',
            75: '1/2',
            90: '0',
            105: '-1/2',
            120: '-1/2',
            135: '-sqrt(2)/2',
            150: '-sqrt(3)/2',
            165: '-sqrt(3)/4',
            180: '-1',
            195: '-sqrt(3)/4',
            210: '-sqrt(3)/2',
            225: '-sqrt(2)/2',
            240: '-1/2',
            255: '-1/2',
            270: '0',
            285: '1/2',
            300: '1/2',
            315: 'sqrt(2)/2',
            330: 'sqrt(3)/2',
            345: 'sqrt(3)/4',
            360: '1'
        }

        tan_vals = {
            0: 'undefined',
            15: '1/sqrt(3)',
            30: 'sqrt(3)/3',
            45: '1',
            60: 'sqrt(3)',
            75: 'sqrt(2)',
            90: 'undefined',
            105: '-sqrt(2)',
            120: '-sqrt(3)',
            135: '-1',
            150: '-1/sqrt(3)',
            165: '-1/sqrt(3)',
            180: '0',
            195: '1/sqrt(3)',
            210: 'sqrt(3)/3',
            225: '1',
            240: 'sqrt(3)',
            255: 'sqrt(2)',
            270: 'undefined',
            285: '-sqrt(2)',
            300: '-sqrt(3)',
            315: '-1',
            330: '-1/sqrt(3)',
            345: '-1/sqrt(3)',
            360: 'undefined'
        }

        # Manually defined dictionaries for cot, sec, and csc values in strings
        cot_vals = {
            0: 'undefined',
            15: '1/sqrt(3)',
            30: 'sqrt(3)/3',
            45: '1',
            60: 'sqrt(3)',
            75: 'sqrt(2)',
            90: 'undefined',
            105: '-sqrt(2)',
            120: '-sqrt(3)',
            135: '-1',
            150: '-1/sqrt(3)',
            165: '-1/sqrt(3)',
            180: '0',
            195: '1/sqrt(3)',
            210: 'sqrt(3)/3',
            225: '1',
            240: 'sqrt(3)',
            255: 'sqrt(2)',
            270: 'undefined',
            285: '-sqrt(2)',
            300: '-sqrt(3)',
            315: '-1',
            330: '-1/sqrt(3)',
            345: '-1/sqrt(3)',
            360: 'undefined'
        }

        sec_vals = {
            0: '1',
            15: '2',
            30: 'sqrt(3)',
            45: 'sqrt(2)',
            60: 'sqrt(3)/3',
            75: '1',
            90: 'undefined',
            105: '-1',
            120: '-sqrt(3)/3',
            135: '-sqrt(2)',
            150: '-sqrt(3)',
            165: '-2',
            180: 'undefined',
            195: '2',
            210: 'sqrt(3)',
            225: 'sqrt(2)',
            240: 'sqrt(3)/3',
            255: '1',
            270: '1',
            285: '1',
            300: '1',
            315: '1',
            330: '2',
            345: 'undefined',
            360: '1'
        }

        csc_vals = {
            0: 'undefined',
            15: '2',
            30: '2*sqrt(3)',
            45: '2*sqrt(2)',
            60: '2',
            75: '2/sqrt(2)',
            90: 'undefined',
            105: '-2/sqrt(2)',
            120: '-2',
            135: '-2*sqrt(2)',
            150: '-2*sqrt(3)',
            165: '-2*sqrt(3)',
            180: 'undefined',
            195: '2*sqrt(3)',
            210: '2',
            225: '2/sqrt(2)',
            240: '2',
            255: '2*sqrt(2)',
            270: '2*sqrt(3)',
            285: '2*sqrt(3)',
            300: '2*sqrt(3)',
            315: '2*sqrt(3)',
            330: '2*sqrt(3)',
            345: '2*sqrt(2)',
            360: 'undefined'
        }

        angle_str = trig_func.split("(")[1].split(")")[0]
        if "pi" in angle_str:
            angle = eval(angle_str.replace("pi","180"))
        else:
            angle = angle_str

        print(angle_str)
        print("hi")

        angle = int(angle)
        angle = angle % 360

        if trig_func.startswith('sin'):
            return sin_vals[angle]
        elif trig_func.startswith('cos'):
            return cos_vals[angle]
        elif trig_func.startswith('tan'):
            return tan_vals[angle]
        elif trig_func.startswith('cot'):
            return cot_vals[angle]
        elif trig_func.startswith('sec'):
            return sec_vals[angle]
        elif trig_func.startswith('cosec'):
            return csc_vals[angle]
        else:
            return "Invalid function"




