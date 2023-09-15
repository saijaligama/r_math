import sympy as sp


def calculate_integration(data):
    expr_str = data[0]
    var_str = data[1]
    lower_limit = data[2]
    upper_limit = data[3]

    var = sp.symbols(var_str)
    expr = sp.sympify(expr_str)
    result = sp.integrate(expr, (var, lower_limit, upper_limit))
    return str(result)
