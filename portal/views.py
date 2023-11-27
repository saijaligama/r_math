import gc
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_file, make_response, \
    Response, jsonify
# from portal.application.sequence import sequence_type, generat_arithmetic_sequence, generat_geometric_sequence
from portal.application.matrix_operations import matrix_arithmetic, matrix_arithmetic_operations, get_matrix, \
    get_ones_zeros_eye, get_transpose_inv_det, get_Diagonal_Trace_Size, get_inverse
# from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
# import numpy as np
from portal.application.complex_numbers import evaluate_complex_expression
from portal.application.equations_inequalities import evaluate_expression, find_variables, calculate_logarithm, \
    quad_equation_solution
import cmath
import random
from decimal import Decimal
# from PyPDF2 import PdfReader
from fraction import Fraction
import re

bp = Blueprint('view', __name__, url_prefix='/uncg_math', template_folder="./templates", static_folder="./static")


################gayatri function##############################
@bp.route('/inequalities_new', methods=['GET', 'POST'])
def inequalities_new():
    if request.method == 'GET':
        return render_template("inequality_new.html")

 #-------------------------------------------------------------
@bp.route('/equations_new', methods=['GET', 'POST'])
def equation_service():
    if request.method == "GET":
        return render_template("equations_new.html")
    else:
        data = request.json
        result = calculate_equation(data['eqn'])
        return jsonify({'result': result})

import sympy as sp

def calculate_equation(equation_or_inequality_str):
    # print(eqn)
    x = sp.symbols('x')
    if '=' in equation_or_inequality_str:
        sides = equation_or_inequality_str.split('=')
        left_side = sp.sympify(sides[0].strip())
        right_side = sp.sympify(sides[1].strip())
        equation = sp.Eq(left_side, right_side)
        solutions = sp.solve(equation, x)
    else:
        inequality = sp.sympify(equation_or_inequality_str)
        solutions = sp.solve_univariate_inequality(inequality, x, relational=False)

    return str(solutions)

#-------------------------------------------------------------

@bp.route('/rationals', methods=["GET", "POST"])
def rationals():
    if request.method == "GET":
        return render_template("rationals.html")
    else:
        data = request.json
        result = simplify_expression(data['eqn'])
        return jsonify({'result': result})

def simplify_expression(expression):
    try:
        # Define symbolic variables
        a = sp.symbols('a')
        b = sp.symbols('b')

        # Parse the input expression using SymPy
        parsed_expression = sp.sympify(expression)

        # Simplify the parsed expression
        simplified_expression = sp.simplify(parsed_expression)

        return str(simplified_expression)
    except sp.SympifyError:
        return "Invalid input"

#-------------------------------------------------------------
@bp.route('repeated_to_fraction', methods=["GET", "POST"])
def repeated_to_fraction():
    if request.method == "POST":
        data = request.json
        result = repeated_fraction_handler(data['fraction'])
        return jsonify({'result': result})

def repeated_fraction_handler(decimal_str):
    # Split the decimal string into integer and fractional parts
    integer_part, fractional_part = decimal_str.split('.')

    # Initialize the numerator and denominator
    numerator = 0
    denominator = 1

    # Process the integer part
    if integer_part:
        numerator = int(integer_part)

    # Process the fractional part
    if '(' in fractional_part:
        non_repeating, repeating = fractional_part.split('(')
        repeating = repeating.rstrip(')')
        non_repeating_len = len(non_repeating)
        repeating_len = len(repeating)

        numerator *= 10 ** non_repeating_len + int(non_repeating + repeating) - int(non_repeating)
        denominator *= (10 ** non_repeating_len * (10 ** repeating_len - 1))
    else:
        denominator *= 10 ** len(fractional_part)
        numerator = int(fractional_part)

    # Simplify the fraction
    common_divisor = sp.gcd(numerator, denominator)
    numerator //= common_divisor
    denominator //= common_divisor

    return "{}/{}".format(numerator, denominator)

#-------------------------------------------------------------
@bp.route('/factorization', methods=["GET", "POST"])
def factoring():
    if request.method == "GET":
        return render_template("factorization.html")
    else:
        data = request.json
        result = factor_handler(data['fraction'])
        return jsonify({'result': result})

def factor_handler(expression):
    try:
        expression = expression.replace("^", "**")
        # Parse the expression using sympy
        expr = sp.sympify(expression)

        # Factor the expression
        factored_expr = sp.factor(expr)

        return str(factored_expr)
    except sp.SympifyError:
        return "Invalid expression"
#-------------------------------------------------------------
import shunting_yard as sy
import math

def convert_to_mixed_fraction(decimal):
    # Convert the decimal to a fraction
    fraction = Fraction(decimal).limit_denominator()

    # Extract the whole number and the fractional part
    whole_number = fraction.numerator // fraction.denominator
    fractional_part = fraction - whole_number

    return f"{whole_number} {fractional_part.numerator}/{fraction.denominator}"



@bp.route('/arithmetic_new', methods=["GET", "POST"])
def arithmetic_new():
    if request.method == "GET":
        return render_template("arithmetic_new.html")
    if request.method == "POST":
        data = request.json
        # result = eval(data['eqn'])
        result = sy.compute(data['eqn'])
        if data['radioValue'] == "integer":
            result = convert_to_mixed_fraction(result)
        return jsonify({'result': result})

#-------------------------------------------------------------

#-------------------------------------------------------------
from sympy import symbols, expand, sympify
def simplify_step_by_step(data):
    # var = symbols(data[1])
    equations = data[0]

    if len(data) > 1:
        var_str = data[1]
        var = symbols(var_str)
    else:
        var = symbols("x")

    if not isinstance(equations, list):
        equations = [equations]

    simplified_equation = None

    for eq_index, equation in enumerate(equations, 1):
        results = []
        # Convert string equation to sympy expression
        equation = sympify(equation)

        print(f"\n--- Simplifying equation {eq_index} ---")

        args = equation.args

        if not args:
            print(f"Equation is a single term: {equation}")

            continue

        print("Step 1: Identify the terms.")
        results.append("Step 1: Identify the terms.")
        for i, term in enumerate(args, 1):
            print(f"Term {i}: {term}")
            results.append(f"Term {i}: {term}")

        print("\nStep 2: Combine the terms.")
        combined_equation = expand(equation)
        print(f"Combined result: {combined_equation}")
        results.append(f"Combined result: {combined_equation}")

        print("\nStep 3: Combine like terms (if any).")
        simplified_equation = expand(combined_equation)
        results.append(f"Simplified equation: {simplified_equation}")
    # return f"Simplified equation: {simplified_equation}"
    return results

@bp.route('/polynomials', methods=["GET", "POST"])
def polynomial_simplification():
    if request.method == 'GET':
        return render_template('polynomial.html')
    elif request.method == 'POST':
        data = request.json
        inp = data['eqn'].split(',')
        result = simplify_step_by_step(inp)
        return jsonify({'result': result})

#-------------------------------------------------------------
import inflect
from word2number import w2n

def number_to_words(num):
    p = inflect.engine()
    whole, decimal = str(num).split('.') if '.' in str(num) else (str(num), None)

    word_representation = p.number_to_words(whole)

    if decimal:
        word_representation += " point " + " ".join(p.number_to_words(int(digit)) for digit in decimal)

    return word_representation


# print(number_to_words(921.31))
def round_to_nearest_10th(num):
    return round(num, -1)

def extract_places(data):
    num = float(data['decimal_to_convert'])
    place = data['show_digit_num']
    num_str = str(num)
    if '.' in num_str:
        whole, decimal = num_str.split('.')
    else:
        whole, decimal = num_str, '0'

    # Dynamically generate place names
    place_names = {
        0: '1st',
        1: '10th',
        2: '100th',
        3: '1000th',  # This can be extended further if needed
    }
    for i in range(4, len(whole)):
        place_names[i] = f'{10**i}th'

    places_dict = {}
    for i, digit in enumerate(reversed(whole)):
        places_dict[f'{place_names[i]}'] = int(digit)

    places_dict['decimal_place'] = int(decimal)

    return places_dict[place]


def text_to_decimal(text):
    try:
        decimal_value = w2n.word_to_num(text)
        return decimal_value
    except ValueError:
        return None

@bp.route('/decimal_conversion', methods=["GET", "POST"])
def decimal_conversion():
    if request.method == 'GET':
        return render_template('decimal_conversion.html')

    if request.method == 'POST':
        data = request.json

        if data['type'] == 'text_dec_dec_text':
            result = ""
            dec_to_convert = data.get("decimal")
            text_to_convert = data.get("text")

            if dec_to_convert:
                result = number_to_words(dec_to_convert)
                return {'decimal':dec_to_convert,'text':result}
            elif text_to_convert:
                result = text_to_decimal(text_to_convert)
                return jsonify({'decimal':result,'text':text_to_convert})
        else:

            if data['operation'] == 'round_to':
                # Implement the 'round_to_nearest_10th()' function for rounding
                result = round_to_nearest_10th(float(data['decimal_to_convert']))
            else:
                # Implement the 'extract_places()' function for specific extraction
                result = extract_places(data)
            return jsonify({'result':result})
#-------------------------------------------------------------


#-------------------------------------------------------------


#-------------------------------------------------------------

################gayatri_function_ends########################



# @bp.route('/', methods=["GET", "POST"])
# def login():
#     if request.method == "GET":
#         return render_template("index.html")

# @bp.route('/calculus', methods=["GET", "POST"])
# def calculus():
#     if request.method == "GET":
#         return render_template("calculus.html")


# @bp.route('/trigonometry', methods=["GET", "POST"])
# def trigonometry():
#     if request.method == "GET":
#         return render_template("trigonometry.html")


# @bp.route('/differentiation', methods=["GET", "POST"])
# def differentiation():
#     if request.method == "GET":
#         return render_template("differentiation.html")


# @bp.route('/integration', methods=["GET", "POST"])
# def integration():
#     if request.method == "GET":
#         return render_template("integration.html")


# @bp.route('/', methods=["GET", "POST"])
# def home():
#     if request.method == "GET":
#         return render_template("home.html")


# @bp.route('/', methods=["GET", "POST"])
# def home():
#    if request.method == "GET":
#        return render_template("home.html")


# @bp.route('/decimal_conversion', methods=["GET", "POST"])
# def decimal_conversion():
#     if request.method == "GET":
#         return render_template("decimal_conversion.html")
#
#
# @bp.route('/fraction_conversion', methods=["GET", "POST"])
# def fraction_conversion():
#     if request.method == "GET":
#         return render_template("fraction_conversion.html")
#
#
# @bp.route('/patterns', methods=["GET", "POST"])
# def patterns():
#     if request.method == "GET":
#         return render_template("patterns.html")
#
#
# @bp.route('/arithmetic_expressions', methods=["GET", "POST"])
# def arithmetic_expressions():
#     if request.method == "GET":
#         return render_template("arithmetic_expressions.html")


@bp.route('/geometry', methods=["GET", "POST"])
def geometry():
    if request.method == "GET":
        return render_template("geometry.html")


# @bp.route('/algebra', methods=["GET", "POST"])
# def Algebra():
#     if request.method == "GET":
#         return render_template("algebra.html")


# @bp.route('/sequences', methods=["GET", "POST"])
# def sequences():
#     if request.method == "GET":
#         return render_template("sequences.html")
#     if request.method == "POST":
#         data = request.json
#         type = data["type"]
#         if type == 'a_or_g_output':
#             arith_or_geo = data["arith_or_geo_input"]
#             a_n_term = data["a_n_term"]
#             finl_out = sequence_type(arith_or_geo, a_n_term, a_n_term)
#             print(finl_out)
#             return finl_out
#         elif type == 'Arithmetic Sequence':
#             print('Geometric', data)
#             print("hi")
#             final_output_ = generat_arithmetic_sequence(data)
#             print('final_output_', final_output_)
#             return final_output_
#         elif type == 'Geometric Sequence':
#             final_output_ = generat_geometric_sequence(data)
#             return final_output_
#         Status = {"status": 'as,mna,sn,s'}
#         return jsonify(Status)


# @bp.route('/matrix_operation', methods=["GET", "POST"])
# def matrix_operation():
#     if request.method == "GET":
#         return render_template("matrix_operation.html")
#     if request.method == "POST":
#         data = request.json
#         match = re.search(r"(?<=})(.*?)(?={)", data['matrix_expression_1_input'])
#         if isinstance(match, type(None)):
#             return {'error_msg': "Syntax error", 'status': "Failed", 'result_': '-----'}
#         operation_ = match.group(1).strip()
#         if len(operation_) != 1:
#             return {'result_': '-----', 'status': "Failed", 'error_msg': "Syntax error"}
#         print(match, data['matrix_expression_1_input'])
#         ixx = match.group(1).index(operation_)
#         ix = match.span()
#         tmp_a = data['matrix_expression_1_input'][:ix[0] + ixx]
#         tmp_b = data['matrix_expression_1_input'][ix[1] - ixx:]
#         if tmp_a.count("{") != tmp_a.count("}") or tmp_a.count("{") == 0 or tmp_a.count("}") == 0:
#             return {'result_': '-----', 'status': "Failed", 'error_msg': "Syntax error"}
#         if tmp_b.count("{") != tmp_b.count("}") or tmp_b.count("{") == 0 or tmp_b.count("}") == 0:
#             return {'error_msg': "Syntax error", 'status': "Failed", 'result_': '-----'}
#         temp_matrix_a = tmp_a.replace('{', '').replace('}', '').strip().split(';')
#         temp_matrix_b = tmp_b.replace('{', '').replace('}', '').strip().split(';')
#
#         print('matrix_expression_1_input', temp_matrix_a)
#         print('matrix_expression_2_input', temp_matrix_b)
#         print('Matrix_Action', operation_)
#         # exit()
#         matrix_a = get_matrix(temp_matrix_a)
#         matrix_b = get_matrix(temp_matrix_b)
#         print('matrix_a', matrix_a)
#         print('matrix_b', matrix_b)
#
#         check_list_ = matrix_arithmetic(matrix_a, matrix_b)
#         print('check_list_', check_list_)
#         if check_list_['OutPut'] == 'Successful':
#             result_ = matrix_arithmetic_operations(matrix_a, matrix_b, operation_)
#             print("Result", result_, type(result_))
#             if isinstance(result_, type(None)):
#                 return {'result_': '-----', 'status': "Failed", 'error_msg': "Syntax Error"}
#
#             if isinstance(result_, str):
#                 return {'result_': '-----', 'status': "Failed", 'error_msg': result_}
#
#             str_final_ = get_final_out_1(result_)
#             # str_final_ = str_final_ + '}'
#             return {'result_': str_final_, 'status': str(check_list_['OutPut']), 'error_msg': '-----'}
#         else:
#             return {'result_': '-----', 'status': str(check_list_['OutPut']), 'error_msg': str(result_)}
#
#
# def get_final_out_1(res):
#     k = list(res)
#     string = ''
#     for z in k:
#         for z2 in str(z).replace('[', '').replace(']', '').split():
#             string += str(float(z2)) + ','
#         string = string[:-1] + ';'
#     return '{' + string[:-1] + '}'


# def get_final_out(result_, action):
#     print('result_',result_)
#     len_ = 0
#     str_final_ = ''
#     if action == 'matrix_matlab_operation':
#         result_ = result_.astype(int)
#     print('result_',result_)
#     if  type(result_) != type(np.int64()):
#         for i in result_.tolist():
#             temp_ = str(i).replace('[', '').replace(']', "")
#             if len_ == 0:
#                 str_final_ = '{' + str(temp_)
#             else:
#                 str_final_ = str(str_final_) + ';' + str(temp_)
#             len_ += 1
#     else:
#         str_final_='{'+str(result_)
#     return str_final_


# @bp.route('/matrix_matlab_operation', methods=["GET", "POST"])
# def matrix_matlab_operation():
#     if request.method == "POST":
#         data = request.json
#         result_ = ''
#         print(data['type'])
#         if data['type'] == "Zeros" or data['type'] == "Ones":
#             if str(data['matrix_matlab_Expression']).__contains__(','):
#                 temp_matrix_a = str(data['matrix_matlab_Expression']).replace('(', '').replace(')', '').split(',')
#                 final_ = []
#                 for num in temp_matrix_a:
#                     if num.isdigit() and int(num) == 0:
#                         return {'result_': "Size cannot be zero.", 'status': "Failed"}
#                     elif num.isdigit():
#                         final_.append(int(num))
#                     else:
#                         return {'result_': "Size cannot be string.", 'status': "Failed"}
#                 result_ = get_ones_zeros_eye(tuple(final_), data['type'])
#             else:
#                 return {'result_': "Please check entered expression", 'status': "Failed"}
#         elif data['type'] == "Eyes":
#             temp_matrix_a = str(data['matrix_matlab_Expression']).replace('(', '').replace(')', '').strip()
#             if temp_matrix_a.isdigit() and int(temp_matrix_a) == 0:
#                 return {'result_': "Size cannot be zero.", 'status': "Failed"}
#             elif temp_matrix_a.isdigit():
#                 temp_matrix_a = int(temp_matrix_a)
#             else:
#                 return {'result_': "Size cannot be string.", 'status': "Failed"}
#             result_ = get_ones_zeros_eye(temp_matrix_a, data['type'])
#         elif data['type'] == "Det" or data['type'] == "Inverse" or data['type'] == "Transpose":
#             if str(data['matrix_matlab_Expression']):
#                 temp_matrix_a = str(data['matrix_matlab_Expression']).replace('{', '').replace('}', '').split(';')
#                 matrix_a = get_matrix(temp_matrix_a)
#                 result_ = get_transpose_inv_det(matrix_a, data['type'])
#                 print("Inverse", result_)
#                 if data['type'] == "Det" and not isinstance(result_, str):
#                     return {'result_': float(result_), 'status': "Successful"}
#             else:
#                 return {'result_': "Please check entered expression", 'status': "Failed"}
#         elif data['type'] == "Diagonal" or data['type'] == "Size" or data['type'] == "Trace":
#             if str(data['matrix_matlab_Expression']):
#                 temp_matrix_a = str(data['matrix_matlab_Expression']).replace('{', '').replace('}', '').split(';')
#                 print("size of matrix:", temp_matrix_a)
#                 matrix_a = get_matrix(temp_matrix_a)
#                 result_ = get_Diagonal_Trace_Size(matrix_a, data['type'])
#                 print("Result", result_)
#                 if data['type'] == "Size" and not isinstance(result_, str):
#                     return {'result_': tuple(result_), 'status': "Successful"}
#                 elif data['type'] == "Trace" and not isinstance(result_, str):
#                     return {'result_': float(result_), 'status': "Successful"}
#                 elif data['type'] == 'Diagonal' and not isinstance(result_, str):
#                     return {'result_': get_final_out_1(result_), 'status': "Successful"}
#                 else:
#                     return {'result_': "Please check matrix expression", 'status': "Failed"}
#         else:
#             return {'result_': "Operation not understood", 'status': "Failed"}
#
#         if isinstance(result_, str):
#             if result_ == 'The matrix is singular':
#                 return {'result_': "The matrix is singular", 'status': "Failed"}
#             elif result_ == 'The matrix is not square':
#                 return {'result_': "The matrix is not square", 'status': "Failed"}
#             elif result_ == 'Please check matrix expression':
#                 return {'result_': "Please check matrix expression", 'status': "Failed"}
#
#         if data['type'] == "Zeros" or data['type'] == "Ones" or data['type'] == "Eyes":
#             str_final_ = get_final_out_1(result_)
#         else:
#             str_final_ = get_final_out_1(result_)
#         if str_final_:
#             str_final_ = str_final_
#             return {'result_': str_final_, 'status': "Successful"}
#         else:
#             return {'result_': "Please check entered expression", 'status': "Failed"}
#

# @bp.route('/complexnumbers', methods=["GET", "POST"])
# def complexnumbers():
#     if request.method == "GET":
#         return render_template("complex_numbers.html")
#     if request.method == "POST":
#         data = request.json
#         type = data["type"]
#         complex_expression_ = data["complex_expression_"]
#         try:
#             message, result = evaluate_complex_expression(complex_expression_)
#         except Exception as e:
#             message = f'Error: Could not calculate the expression ({e})'
#             if type == 'Complex Expressions':
#                 return jsonify(
#                     {"message": message, "result_real": "na.", "result_imagery": "na."})
#             else:
#                 return jsonify(
#                     {"message": message, "result": "na."})
#         if type == 'Complex Expressions':
#             return jsonify({"message": message, "result_real": str(result.real), "result_imagery": str(result.imag)})
#         elif type == 'Absolute':
#             return jsonify({"message": message, "result": str(abs(result))})
#         elif type == 'Angle':
#             return jsonify({"message": message, "result": str(cmath.phase(result))})
#         elif type == 'Conjugate':
#             return jsonify({"message": message, "result": str(result.conjugate())})
#         elif type == 'Real':
#             return jsonify({"message": message, "result": str(result.real)})
#         elif type == 'imagery':
#             return jsonify({"message": message, "result": str(result.imag)})
#         Status = {"status": 'as,mna,sn,s'}
#         return jsonify(Status)


# @bp.route('/equationsandinequalities', methods=["GET", "POST"])
# def equationsandinequalities():
#     if request.method == "GET":
#         return render_template("equations_and_inequalities.html")
#     if request.method == "POST":
#         message = 'na.'
#         result = 'na.'
#         data = request.json
#         type_ = data["type"]
#         print("From views:,", data)
#         if type_ == 'get_equations':
#
#             Equation = data["Equations"]
#             Equation = Equation.split(',')
#             print(Equation)
#             Equations = Equation[0]
#             Value_1 = Equation[1]
#             Value_2 = Equation[2]
#             try:
#                 Value_3 = Equation[3]
#                 print('Value_3', Value_3)
#             except:
#                 Value_3 = 'z=0'
#                 pass
#
#             print('Equations', Equations)
#             print('Value_1', Value_1)
#             print('Value_2', Value_2)
#
#             result, message = evaluate_expression(Equations, x=str(Value_1), y=str(Value_2), z=str(Value_3))
#             return jsonify({"message": message, "result": str(result)})
#
#         elif type_ == '2nd_type_equations':
#
#             Equation = data["Equations1"]
#             Equation = Equation.split(',')
#             print(Equation)
#             Equations1 = Equation[0]
#             Equations2 = Equation[1]
#             Value_1 = Equation[2]
#             Value_2 = Equation[3]
#
#             # Equations1 = data["Equations1"]
#             # Equations2 = data["Equations2"]
#             # Value_1 = data["Value_1"]
#             # Value_2 = data["Value_2"]
#             result, message = find_variables(Equations1, Equations2, Value_1, Value_2)
#             return jsonify({"message": message, "result": str(result)})
#
#         elif type_ == 'Logarithm and Exponential':
#             Equations1 = data["Equations"]
#             result, message = calculate_logarithm(Equations1)
#             return jsonify({"message": message, "result": str(result)})
#
#         elif type_ == 'quad_equations':
#             Equations1 = data["Equations1"]
#             print("From init", Equations1)
#             result, message = quad_equation_solution(Equations1)
#             print("From result", result)
#             return jsonify({"message": message, "result": str(result[0]), "result2": str(result[1])})
#
#         return jsonify({"message": message, "result": str(result)})


# @bp.route('/integer', methods=["GET", "POST"])
# def integer():
#     if request.method == "GET":
#         return render_template("integer.html")
#     if request.method == "POST":
#         data = request.json
#         num_of_questions = int(data['numOfQues'])
#         f_num_digits = int(data['fnumDigits'])
#         s_num_digits = int(data['sNumDigits'])
#         operation = data['ASMD']
#
#         result = {'questions': [], 'answers': []}
#         for i in range(0, num_of_questions):
#             first_num = random.randint(10 ** (f_num_digits - 1), 10 ** f_num_digits - 1)
#             second_num = random.randint(10 ** (s_num_digits - 1), 10 ** s_num_digits - 1)
#
#             if operation == '+':
#                 res = first_num + second_num
#             elif operation == '-':
#                 res = first_num - second_num
#             elif operation == '*':
#                 res = first_num * second_num
#             elif operation == '/':
#                 if second_num == 0:
#                     second_num = random.randint(10 ** (s_num_digits - 1), 10 ** s_num_digits - 1)
#                     res = round(first_num // second_num, 2)
#                 else:
#                     res = round(first_num // second_num, 2)
#             else:
#                 return jsonify({'error': 'Invalid Operation'})
#
#             question = str(first_num) + ' ' + operation + ' ' + str(second_num)
#             result['questions'].append(question)
#             res = round(res, 5)
#             result['answers'].append(str(res))
#
#     return jsonify(result)
    # return {1:'1234'}


@bp.route('/integercheck', methods=["GET", "POST"])
def integercheck():
    data = request.json
    return jsonify(data)


# @bp.route('/fraction', methods=["GET", "POST"])
# def fractions():
#     if request.method == "GET":
#         return render_template('fraction.html')
#     if request.method == 'POST':
#         data = request.get_json()
#         num_of_questions = int(data['numOfQues'])
#         first_format = data['fNumberFormat']
#         second_format = data['sNumberFormat']
#
#         first_digits = [d for d in first_format.split()]
#         second_digits = [d for d in second_format.split()]
#
#         first_numerator = int(first_digits[1].split("/")[0])
#         second_numerator = int(second_digits[1].split("/")[0])
#
#         first_denominator = int(first_digits[1].split("/")[1])
#         second_denominator = int(second_digits[1].split("/")[1])
#
#         op = data['ASMD']
#
#         result = {'questions': [], 'answers': []}
#         for i in range(num_of_questions):
#             f_num_res = generate_number(int(first_digits[0]), first_numerator, first_denominator)
#             whole_num1, frac1 = f_num_res.split()
#
#             fraction = Fraction(frac1)
#             # f_num = str(round(float(whole_num1) + fraction.numerator / fraction.denominator, 5))
#
#             # s_num_res = generate_number(int(second_digits[0]), second_numerator, second_denominator)
#             # whole_num2, frac2 = s_num_res.split()
#
#             # fraction_2 = Fraction(frac2)
#             # s_num = str(round(float(whole_num2) + fraction_2.numerator / fraction_2.denominator, 5))
#
#             f_num = str(float(whole_num1) + fraction.numerator / fraction.denominator)
#
#             s_num_res = generate_number(int(second_digits[0]), second_numerator, second_denominator)
#             whole_num2, frac2 = s_num_res.split()
#
#             fraction_2 = Fraction(frac2)
#             s_num = str(float(whole_num2) + fraction_2.numerator / fraction_2.denominator)
#
#             print(f_num)
#             print(s_num)
#
#             if op == '+':
#                 res = float(f_num) + float(s_num)
#             elif op == '-':
#                 res = float(f_num) - float(s_num)
#             elif op == '*':
#                 res = float(f_num) * float(s_num)
#             elif op == '/':
#                 res = float(f_num) / float(s_num)
#             else:
#                 res = 0
#             # res_1 = decimal_to_fraction(res)
#             res_1 = round(res, 5)
#             # res_1 = res
#
#             result['questions'].append(f'{f_num_res} {op} {s_num_res}')
#             # result['answers'].append(res_1)
#             result['answers'].append(str(res_1))
#
#         return jsonify(result)


# def generate_number(base, num_digits, den_digits):
#     whole_number = ''.join(str(random.randint(0, 9)) for _ in range(base))
#     numerator = [random.randint(0, 9) for _ in range(num_digits)]
#     denominator = [random.randint(1, 9) for _ in range(den_digits)]
#
#     if numerator[0] > denominator[0]:
#         numerator[0], denominator[0] = denominator[0], numerator[0]
#
#     numerator = ''.join(str(numerator[0]))
#     denominator = ''.join(str(denominator[0]))
#     return f'{whole_number} {numerator}/{denominator}'


@bp.route('/decimal', methods=["GET", "POST"])
def decimal():
    if request.method == "GET":
        return render_template("decimal.html")
    if request.method == "POST":
        data = request.get_json()
        num_of_ques = int(data['numOfQues'])
        f_num_format = str(data['fNumberFormat'])
        s_num_format = str(data['sNumberFormat'])
        op = str(data['ASMD'])

        f_num_digits_left, f_num_digits_right = map(int, f_num_format.split('.'))
        s_num_digits_left, s_num_digits_right = map(int, s_num_format.split('.'))

        questions = {'questions': [], 'answers': []}

        for i in range(1, num_of_ques + 1):
            f_num = Decimal(str(random.uniform(0, 10 ** f_num_digits_left))).quantize(
                Decimal('1.' + '0' * f_num_digits_right))
            s_num = Decimal(str(random.uniform(0, 10 ** s_num_digits_left))).quantize(
                Decimal('1.' + '0' * s_num_digits_right))

            if f_num == 0:
                f_num = Decimal(str(random.uniform(0, 10 ** f_num_digits_left))).quantize(
                    Decimal('1.' + '0' * f_num_digits_right))

            elif s_num == 0:
                s_num = Decimal(str(random.uniform(0, 10 ** s_num_digits_left))).quantize(
                    Decimal('1.' + '0' * s_num_digits_right))
            else:
                x = 1;

            if op == '+':
                result = f_num + s_num
            elif op == '-':
                result = f_num - s_num
            elif op == '*':
                result = f_num * s_num
            elif op == '/':
                if s_num == 0:
                    s_num = Decimal(str(random.uniform(0, 10 ** s_num_digits_left))).quantize(
                        Decimal('1.' + '0' * s_num_digits_right))

                    result = round((f_num / s_num), 5)
                else:
                    result = round((f_num / s_num), 5)
            # questions[f"{f_num} - {s_num}"] = float(result)
            # questions[str(f_num) + " " + op + " " + str(s_num)] = float(result)

            ques = str(f_num) + " " + op + " " + str(s_num)

            result = round(result, 5)
            result1 = str(result)
            if result1[-1] == '0':
                result1 = result1.rstrip('0')

            questions['questions'].append(ques)
            questions['answers'].append(result1)
            # result1 = round(result,5)
            # questions['answers'].append(float(result1))

        print(questions)
        return jsonify(questions)


def decimal_to_fraction(decimal):
    fraction = Fraction(decimal)
    whole_number = fraction.numerator // fraction.denominator
    numerator = fraction.numerator % fraction.denominator
    denominator = fraction.denominator
    return f"{whole_number} {numerator}/{denominator}"


@bp.route('/random_tests', methods=["GET", "POST"])
def random_tests():
    if request.method == "GET":
        return render_template("random_tests.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/eogmath', methods=["GET", "POST"])
def eogMath():
    if request.method == "GET":
        return render_template("eogmath.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/kindergarden', methods=["GET", "POST"])
def kindergarten():
    if request.method == "GET":
        return render_template("kindergarden_double.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/kindergardenmain', methods=["GET", "POST"])
def kindermain():
    if request.method == "GET":
        return render_template("kindergarten.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/firstgrade', methods=["GET", "POST"])
def first():
    if request.method == "GET":
        return render_template("first_double.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/firstmain', methods=["GET", "POST"])
def firstmain():
    if request.method == "GET":
        return render_template("first.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/secondgrade', methods=["GET", "POST"])
def second():
    if request.method == "GET":
        return render_template("second_double.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/secondmain', methods=["GET", "POST"])
def secondmain():
    if request.method == "GET":
        return render_template("second.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/thirdgrade', methods=["GET", "POST"])
def third():
    if request.method == "GET":
        return render_template("third_double.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/thirdmain', methods=["GET", "POST"])
def thirdmain():
    if request.method == "GET":
        return render_template("third.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/fourthgrade', methods=["GET", "POST"])
def fourth():
    if request.method == "GET":
        return render_template("fourth_double.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/fourthmain', methods=["GET", "POST"])
def fourthmain():
    if request.method == "GET":
        return render_template("fourth.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/fifthgrade', methods=["GET", "POST"])
def fifth():
    if request.method == "GET":
        return render_template("fifth_double.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/fifthhmain', methods=["GET", "POST"])
def fifthmain():
    if request.method == "GET":
        return render_template("fifth.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/sixthgrade', methods=["GET", "POST"])
def sixth():
    if request.method == "GET":
        return render_template("sixth_double.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/sixthhmain', methods=["GET", "POST"])
def sixthmain():
    if request.method == "GET":
        return render_template("sixth.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/seventhgrade', methods=["GET", "POST"])
def seventh():
    if request.method == "GET":
        return render_template("seventh_double.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/seventhmain', methods=["GET", "POST"])
def seventhmain():
    if request.method == "GET":
        return render_template("seventh.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/eighthgrade', methods=["GET", "POST"])
def eighth():
    if request.method == "GET":
        return render_template("eight_double.html")
    if request.method == "POST":
        data = request.get_json()


@bp.route('/eighthmain', methods=["GET", "POST"])
def eighthmain():
    if request.method == "GET":
        return render_template("eighth.html")
    if request.method == "POST":
        data = request.get_json()

#
# @bp.route('/check_answers', methods=["GET", "POST"])
# def checkintdecfracanswers():
#     data = request.get_json()
#     results = {}
#     for question, values in data.items():
#         if values['Answer'] == values['Submission']:
#             results[question] = 'RIGHT'
#         else:
#             results[question] = 'WRONG'
#     return jsonify(results)
# =============================================================================
# @bp.route('/getpdf', methods=["GET", "POST"])
# =============================================================================
# def getPdf():
#     pdf_path = 'C:/Users/saija/Downloads/Mathematical_Calculation_V3/portal/templates/question/g3mathnokey.pdf'  # Replace with the actual path to your PDF file
#     with open(pdf_path, 'rb') as pdf:
#         pdf_reader = PdfReader(pdf)
#     
#         #pdf.close()
# 
#         return Response(pdf_reader.stream, content_type='application/pdf')
# =============================================================================
# =============================================================================
