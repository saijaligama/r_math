from flask import Blueprint, render_template, request, jsonify
from fraction import Fraction
import random

fraction_bp = Blueprint('fraction_bp', __name__, url_prefix='/uncg_math',
                        template_folder="./templates", static_folder="./static")


def generate_number(base, num_digits, den_digits):
    whole_number = ''.join(str(random.randint(0, 9)) for _ in range(base))
    numerator = [random.randint(0, 9) for _ in range(num_digits)]
    denominator = [random.randint(1, 9) for _ in range(den_digits)]

    if numerator[0] > denominator[0]:
        numerator[0], denominator[0] = denominator[0], numerator[0]

    numerator = ''.join(str(numerator[0]))
    denominator = ''.join(str(denominator[0]))
    return f'{whole_number} {numerator}/{denominator}'


@fraction_bp.route('/fraction', methods=["GET", "POST"])
def fractions():
    if request.method == "GET":
        return render_template('fraction.html')
    if request.method == 'POST':
        data = request.get_json()
        num_of_questions = int(data['numOfQues'])
        first_format = data['fNumberFormat']
        second_format = data['sNumberFormat']

        first_digits = [d for d in first_format.split()]
        second_digits = [d for d in second_format.split()]

        first_numerator = int(first_digits[1].split("/")[0])
        second_numerator = int(second_digits[1].split("/")[0])

        first_denominator = int(first_digits[1].split("/")[1])
        second_denominator = int(second_digits[1].split("/")[1])

        op = data['ASMD']

        result = {'questions': [], 'answers': []}
        for i in range(num_of_questions):
            f_num_res = generate_number(int(first_digits[0]), first_numerator, first_denominator)
            whole_num1, frac1 = f_num_res.split()

            fraction = Fraction(frac1)
            # f_num = str(round(float(whole_num1) + fraction.numerator / fraction.denominator, 5))

            # s_num_res = generate_number(int(second_digits[0]), second_numerator, second_denominator)
            # whole_num2, frac2 = s_num_res.split()

            # fraction_2 = Fraction(frac2)
            # s_num = str(round(float(whole_num2) + fraction_2.numerator / fraction_2.denominator, 5))

            f_num = str(float(whole_num1) + fraction.numerator / fraction.denominator)

            s_num_res = generate_number(int(second_digits[0]), second_numerator, second_denominator)
            whole_num2, frac2 = s_num_res.split()

            fraction_2 = Fraction(frac2)
            s_num = str(float(whole_num2) + fraction_2.numerator / fraction_2.denominator)

            print(f_num)
            print(s_num)

            if op == '+':
                res = float(f_num) + float(s_num)
            elif op == '-':
                res = float(f_num) - float(s_num)
            elif op == '*':
                res = float(f_num) * float(s_num)
            elif op == '/':
                res = float(f_num) / float(s_num)
            else:
                res = 0
            # res_1 = decimal_to_fraction(res)
            res_1 = round(res, 5)
            # res_1 = res

            result['questions'].append(f'{f_num_res} {op} {s_num_res}')
            # result['answers'].append(res_1)
            result['answers'].append(str(res_1))

        return jsonify(result)
