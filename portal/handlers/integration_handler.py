import sympy as sp


def calculate_integration(data):
    expr_str = data['eqn']
    var_str = data['var']
    lower_limit = data['lower']
    upper_limit = data['upper']

    var = sp.symbols(var_str)
    expr = sp.sympify(expr_str)
    result = sp.integrate(expr, (var, lower_limit, upper_limit))
    return str(result)
