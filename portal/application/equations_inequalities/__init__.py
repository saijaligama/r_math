# def evaluate_expression(expression, **values):
#     for key, value in values.items():
#         expression = expression.replace(key, str(value))
#     return eval(expression)


# result1 = evaluate_expression('3*s-t', s=2, t=0)
#
# print(result1)
#
# result1 = evaluate_expression('x + y', x=2, y=3)
# print(result1)
from sympy import symbols, solve, sympify, Eq
import sympy

import numpy as np
def evaluate_expression(expression, **values):
    try:
        result=''
        for key, value in values.items():
            print("__init__",key,value)
            if str(value).__contains__('='):
                len_ = str(value).split('=')
                if len(len_)>=2:
                    expression = expression.replace(len_[0], str(len_[1]))
                else:
                    message = 'Invalid equation'
                    result = 'na.'
                    return result, message
                    break
            else:
                message = 'Invalid 2'
                result = 'na.'
                return result, message
                break
        try:
            result = eval(expression)
            message = 'Data extracted successfully'
            return result, message
        except ValueError:
            message = 'try string'
        except Exception as e:
            message = f'Error: Could not calculate the equation ({e})'
        return message, result
    except Exception as e:
        message = f'Error: Could not calculate the equation ({e})'
        result='na'
    return result, message


def find_variables(eq1, eq2, var1, var2):
    message=''
    result=''
    try:
        try:
            lhs1, rhs1 = eq1.split('=')
            lhs2, rhs2 = eq2.split('=')
        except ValueError:
            message = 'Invalid equation'
            result = 'na'
            return result, message
        except Exception as e:
            message = f'Error: Could not calculate the equation ({e})'
            result = 'na'
            return result, message
        eq1 = Eq(sympify(lhs1.replace(var1, 'a').replace(var2, 'b')),
                 sympify(rhs1.replace(var1, 'a').replace(var2, 'b')))
        eq2 = Eq(sympify(lhs2.replace(var1, 'a').replace(var2, 'b')),
                 sympify(rhs2.replace(var1, 'a').replace(var2, 'b')))
        a, b = symbols('a b')
        message = 'Data extracted successfully'
        result = solve((eq1, eq2), (a, b))
        print('result',result)
    except Exception as e:
        message = f'Error: Could not calculate the equation ({e})'
        result='na'
    return str(result).replace('a',"Value 1").replace('b',"Value 2"), message


def calculate_logarithm(equation_str: str):
    try:
        try:
            equation_str_lhs, equation_str_rhs = equation_str.split("=")
            print(equation_str_lhs,equation_str_rhs)
            if "(" not in equation_str_lhs or ")" not in equation_str_lhs:
                message =  "Syntax error"
                result = 'na'
                return result, message
        except ValueError:
            message = 'Invalid equation'
            result = 'na'
            return result, message
        except Exception as e:
            message = f'Error: Could not calculate the equation ({e})'
            result = 'na'
            return result, message
        equation_lhs = sympy.parse_expr(equation_str_lhs, local_dict={"log": lambda x: sympy.log(x, 10),"ln": lambda x: sympy.log(x, np.exp(1)),"lg": lambda x: sympy.log(x, 2)})
        equation_rhs = sympy.parse_expr(equation_str_rhs)
        equation = sympy.Eq(equation_lhs, equation_rhs)
        result = sympy.solve(equation)
        print(result)
        for r_1 in result:
            try:
                result=float(r_1)
                break
            except:
                continue

        message = 'Data extracted successfully'
        return result, message
    except Exception as e:
        message = f'Error: Could not calculate the equation ({e})'
        result='na'

    return result, message

def quad_equation_solution(equation_str: str):
    try:
        try:
            equation_str_lhs, equation_str_rhs = equation_str.split("=")
            print(equation_str_lhs)

        except ValueError:
            message = 'Invalid equation'
            result = 'na'
            return result, message
        except Exception as e:
            message = f'Error: Could not calculate the equation ({e})'
            result = 'na'
            return result, message
        equation_lhs = sympy.parse_expr(equation_str_lhs) #, local_dict={"log": lambda x: sympy.log(x, 10),"ln": lambda x: sympy.log(x, np.exp(1)),"lg": lambda x: sympy.log(x, 2)})
        equation_rhs = sympy.parse_expr(equation_str_rhs)
        equation = sympy.Eq(equation_lhs, equation_rhs)
        print(equation)
        result = sympy.solve(equation)
        try:
            result_list  = [round(float(result[0]),5),round(float(result[1]),5)]
        except:
            result_list  = [str(result[0]),str(result[1])]
        print(result_list)
        message = 'Data extracted successfully'
        return result_list, message
    except Exception as e:
        message = f'Error: Could not calculate the equation ({e})'
        result='na'

    return result, message

def calculate_exponential(equ: str):
    try:
        try:
            equation_str_lhs, equation_str_rhs = equ.split("=")
            print("Equation spits",equation_str_lhs,equation_str_rhs)
            if "(" not in equation_str_lhs or ")" not in equation_str_lhs:
                message =  "Syntax error"
                result = 'na'
                return result, message
        except ValueError:
            message = 'Invalid equation'
            result = 'na'
            return result, message
        except Exception as e:
            message = f'Error: Could not calculate the equation ({e})'
            result = 'na'
            return result, message
        equation_lhs = sympy.parse_expr(equation_str_lhs, local_dict={"log": lambda x: sympy.log(x, 10),"ln": lambda x: sympy.log(x, np.exp(1)),"lg": lambda x: sympy.log(x, 2)})
        equation_rhs = sympy.parse_expr(equation_str_rhs)
        equation = sympy.Eq(equation_lhs, equation_rhs)
        result = sympy.solve(equation)
        result=float(result[0])
        message = 'Data extracted successfully'
        return result, message
    except Exception as e:
        message = f'Error: Could not calculate the equation ({e})'
        result='na'

    return result, message
