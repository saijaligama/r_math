import sympy as sp


# def calculate_integration(data):
#     expr_str = data[0]
#     if len(data) > 1:
#         var_str = data[1]
#         var = sp.symbols(var_str)
#     else:
#         var = sp.symbols("x")
#
#     # var_str = data[1]
#
#     # var = sp.symbols(var_str)
#     expr = sp.sympify(expr_str)
#
#     if len(data) < 3:
#         return str(sp.integrate(expr,var))
#     else:
#         lower_limit = data[2]
#         upper_limit = data[3]
#         result = sp.integrate(expr, (var, lower_limit, upper_limit))
#         return str(result)
def calculate_indefinite(data):
    name_list = ['exp', 'var', 'lower', 'upper']
    if len(data) == 4:
        data_dict = dict(zip(name_list,data))
    else:
        data_dict = dict(zip(['exp', 'lower', 'upper'],data))
        data_dict['var'] = "x"

    var = sp.symbols(data_dict['var'])
    expr_str = data_dict['exp']
    expr = sp.sympify(expr_str)
    lower_limit = data_dict['lower']
    upper_limit = data_dict['upper']
    result = sp.integrate(expr, (var, lower_limit, upper_limit))
    return str(result)


def calculate_integration(data):
    expr_str = data[0]
    if len(data) > 1:
        var_str = data[1]
        var = sp.symbols(var_str)
    else:
        var = sp.symbols("x")

    expr = sp.sympify(expr_str)
    return str(sp.integrate(expr,var))
