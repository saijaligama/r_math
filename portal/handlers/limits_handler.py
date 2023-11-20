from sympy import symbols, limit, sympify, oo, pi, powsimp

import re


class LimitCalculator:

    def __init__(self):
        pass

    def limit_create(self,data):
        x = symbols(data['var'])
        expr = sympify(data['eqn'])
        expr = powsimp(expr)

        if data['point'] == oo:
            limit_value = limit(expr, x, data['point'], dir=data['dir'])
        else:
            limit_value = limit(expr, x, data['point'], data['dir'])

        return f"The limit of {data['eqn']} as {data['var']} approaches {data['dir']} {data['point']} is {limit_value}"


    def calculate_limit(self, inp):
        try:
            multi_dir = False
            inp = inp.split(',')
            point_dir = inp[1].split(">")

            if point_dir[1][-1] == '+':
                dir1 = "+"
                point = point_dir[1][:-1]
            elif point_dir[1][-1] == '-':
                dir1 = "-"
                point = point_dir[1][:-1]
            else:
                multi_dir = True
                point = point_dir[1]

            # if len(point_dir) > 1:
            #     dir1 = point_dir[1][-1]
            #     point = point_dir[1][:-1]
            # else:
            #     dir1 = "+"

            # dir1 = point_dir[1][-1]
            # point = point_dir[1][:-1]

            if "in" in point:
                point = oo
            elif "p" in point:
                point = pi
            else:
                point = float(point)

            var = inp[1][0]

        except IndexError as e:
            error_message = f"Error: {e}"
            return error_message

        if multi_dir == True:
            res1 = self.limit_create({'eqn': inp[0], 'var': var, 'point': point, 'dir': '+'})
            res2 = self.limit_create({'eqn': inp[0], 'var': var, 'point': point, 'dir': '-'})

            return res1 + "  " + res2

        data = {'eqn': inp[0], 'var': var, 'point': point, 'dir': dir1}

        return self.limit_create(data)


