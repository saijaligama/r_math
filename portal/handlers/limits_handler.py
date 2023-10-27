from sympy import symbols, limit, sympify, oo, pi, powsimp

import re


class LimitCalculator:

    def __init__(self):
        pass

    def calculate_limit(self, inp):
        try:
            inp = inp.split(',')
            point_dir = inp[1].split(">")

            if len(point_dir) > 1:
                dir1 = point_dir[1][-1]
                point = point_dir[1][:-1]
            else:
                dir1 = "+"


            dir1 = point_dir[1][-1]
            point = point_dir[1][:-1]

            if point == "inf":
                point = oo
            elif point == "pi":
                point = pi
            else:
                point = float(point)

            var = inp[1][0]

        except IndexError as e:
            error_message = f"Error: {e}"
            return error_message

        data = {'eqn': inp[0], 'var': var, 'point': point, 'dir': dir1}

        x = symbols(var)
        expr = sympify(data['eqn'])
        expr = powsimp(expr)

        if point == oo:
            limit_value = limit(expr, x, data['point'], dir=data['dir'])
        else:
            limit_value = limit(expr, x, data['point'], data['dir'])

        return f"The limit of {data['eqn']} as {data['var']} approaches {data['point']} is {limit_value}"