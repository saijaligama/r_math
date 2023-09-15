from sympy import symbols, limit, sympify


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
        data = {'eqn':inp[0],'var':inp[1],'point':inp[2],'dir':inp[3]}
        x = symbols(data['var'])
        expr = sympify(data['eqn'])
        limit_value = limit(expr, x, data['point'],
                            data['dir'])  # Providing a default direction if 'dir' isn't in the dictionary

        return f"The limit of {data['eqn']} as {data['var']} approaches {data['point']} is {limit_value}"
