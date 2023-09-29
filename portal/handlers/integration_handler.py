import sympy as sp


def calculate_integration(data):
    expr_str = data[0]
    var_str = data[1]

    var = sp.symbols(var_str)
    expr = sp.sympify(expr_str)

    if len(data) == 2:
        return str(sp.integrate(expr,var))
    else:
        lower_limit = data[2]
        upper_limit = data[3]
        result = sp.integrate(expr, (var, lower_limit, upper_limit))
        return str(result)
