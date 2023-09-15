import sympy as sp


def calculate_differentiation(data):
    expr_str = data[0]
    var_str = data[1]
    var = sp.symbols(var_str)

    # Parse the expression
    expr = sp.sympify(expr_str)

    # Differentiate
    diff_expr = sp.diff(expr, var)
    # print(diff_expr)

    return str(diff_expr)
