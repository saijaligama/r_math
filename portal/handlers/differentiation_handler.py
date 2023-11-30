import sympy as sp


def calculate_differentiation(data):
    print(data[0])
    expr_str = data[0]



    if len(data) > 1:
        var_str = data[1]
        var = sp.symbols(var_str)
    else:
        var = sp.symbols("x")
    # var_str = data[1]
    # var = sp.symbols(var_str)

    expr_str = expr_str.replace('cosec', '1/sin')

    # Parse the expression
    expr = sp.sympify(expr_str)



    # Differentiate
    diff_expr = sp.diff(expr, var)
    # print(diff_expr)

    return str(diff_expr)
