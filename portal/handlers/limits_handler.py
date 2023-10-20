from sympy import symbols, limit, sympify
import re

class LimitCalculator:
    def __init__(self):
        pass  # No initialization parameters for now

    def calculate_limit(self, inp):
        """Compute the limit of the expression using the provided data dictionary.

        Parameters:
        - data: A dictionary containing:
            - 'expr_str': A string representation of the function, e.g., "1/x - 2"
            - 'var_str': The variable of interest, e.g., "x"
            - 'point': The point the variable is approaching
            - 'dir': Direction of approach ("+" means from the right, "-" means from the left)

        Returns:
        - A string containing the computed limit
        """
        # dir = inp[1][-1]
        # point = inp[1][-2]
        # var = inp[1][0]

        try:
            dir = inp[1][-1]
            point = inp[1][-2]
            var = inp[1][0]
        except IndexError as e:
            # Handle the case where the list indices are out of range
            error_message = f"Error: {e}"
            # You can return an error indicator or message
            return error_message
        print(var)

        # data = {'eqn':inp[0],'var':inp[1],'point':inp[2],'dir':inp[3]}
        data = {'eqn': inp[0], 'var': var, 'point': point, 'dir': dir}
        x = symbols(var)
        expr = sympify(data['eqn'])
        limit_value = limit(expr, x, data['point'],
                            data['dir'])  # Providing a default direction if 'dir' isn't in the dictionary

        return f"The limit of {data['eqn']} as {data['var']} approaches {data['point']} is {limit_value}"

    #
    # from sympy import symbols, sympify, limit

    # def calculate_limit(self, inp):
    #     """Compute the limit of the expression using the provided data dictionary.
    #
    #     Parameters:
    #     - inp: A tuple containing:
    #         - 'expr_str': A string representation of the function, e.g., "1/x - 2"
    #         - 'var_str': The variable of interest, e.g., "x"
    #         - 'point': The point the variable is approaching
    #         - 'dir': Direction of approach ("+" means from the right, "-" means from the left)
    #
    #     Returns:
    #     - A string containing the computed limit
    #     """
    #     expr_str, var_str, point_str = inp
    #
    #     # Use regular expressions to extract variable and point
    #     # var_match = re.search(r'([a-zA-Z]+)', var_str)
    #     # point_match = re.search(r'->\s*([\w\s+-]+)', point_str)
    #
    #
    #
    #     if var_match and point_match:
    #         var = var_match.group(1)
    #         point = point_match.group(1)
    #     else:
    #         return "Invalid input format"
    #
    #     x = symbols(var)
    #     expr = sympify(expr_str)
    #     limit_value = limit(expr, x, point, direction)
    #     point = "+"
    #
    #     return f"The limit of {expr_str} as {var} approaches {point} is {limit_value}"

    # def calculate_limit(self, inp):
    #     """Compute the limit of the expression using the provided data dictionary.
    #
    #     Parameters:
    #     - data: A dictionary containing:
    #         - 'expr_str': A string representation of the function, e.g., "1/x - 2"
    #         - 'var_str': The variable of interest, e.g., "x"
    #         - 'point': The point the variable is approaching
    #         - 'dir': Direction of approach ("+" means from the right, "-" means from the left)
    #
    #     Returns:
    #     - A string containing the computed limit
    #     """
    #
    #     # data = {'eqn':inp[0],'var':inp[1],'point':inp[2],'dir':inp[3]}
    #     data = {'eqn': inp[0], 'var': inp[1], 'point': inp[2], 'dir': '+'}
    #     x = symbols(data['var'])
    #     expr = sympify(data['eqn'])
    #     limit_value = limit(expr, x, data['point'],
    #                         data['dir'])  # Providing a default direction if 'dir' isn't in the dictionary
    #
    #     return f"The limit of {data['eqn']} as {data['var']} approaches {data['point']} is {limit_value}"
