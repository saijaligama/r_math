import sympy as sp

def analyze_graph(data):
    # Define the variable symbol
    variable = 'x'
    x = sp.symbols(variable)

    # Parse the expression string into a SymPy expression
    try:
        y = sp.sympify(data['eqn'])
    except sp.SympifyError:
        return {
            "Error": "Invalid expression"
        }

    # Calculate the derivative for finding maxima and minima
    dy_dx = sp.diff(y, x)

    # Find the domain (where the function is defined)
    domain = sp.solve(sp.Eq(dy_dx, sp.nan), x)
    domain = [float(value) for value in domain]  # Convert to float

    # Find the critical points
    critical_points = sp.solve(dy_dx, x)
    critical_points = [float(point) for point in critical_points]  # Convert to float

    # Initialize minima and maxima as None
    minima = None
    maxima = None

    # Check if there are critical points before finding min and max
    if critical_points:
        critical_values = [float(y.subs(x, p)) for p in critical_points]  # Convert to float
        minima = min(critical_values)
        maxima = max(critical_values)

    # Check for symmetry
    is_symmetric = True if y == y.subs(x, -x) else False

    # Calculate the period for periodic functions, including sin(x)
    period = None
    if sp.sin(x) in sp.expand(y).as_ordered_terms():
        period = 2 * sp.pi

    # Set default values for minima and maxima when no critical points found
    if minima is None:
        minima = "N/A"
    if maxima is None:
        maxima = "N/A"

    return {
        "Domain": domain,
        "Range": (minima, maxima),
        "Period": float(period) if period else "N/A",
        "Maxima": maxima,
        "Minima": minima,
        "Symmetric": is_symmetric
    }


# import sympy as sp
#
# def analyze_graph(data):
#     # Define the variable symbol
#     if len(data) > 1:
#         variable = data[1]
#     else:
#         variable = 'x'
#     # variable = 'x'
#     x = sp.symbols(variable)
#
#     # Parse the expression string into a SymPy expression
#     try:
#         y = sp.sympify(data[0])
#     except sp.SympifyError:
#         return {
#             "Error": "Invalid expression"
#         }
#
#     # Calculate the derivative for finding maxima and minima
#     dy_dx = sp.diff(y, x)
#
#     # Find the domain (where the function is defined)
#     domain = sp.solve(sp.Eq(dy_dx, sp.nan), x)
#     domain = [float(value) for value in domain]  # Convert to float
#
#     # Find the critical points
#     critical_points = sp.solve(dy_dx, x)
#     critical_points = [float(point) for point in critical_points]  # Convert to float
#
#     # Initialize minima and maxima as None
#     minima = None
#     maxima = None
#
#     # Check if there are critical points before finding min and max
#     if critical_points:
#         critical_values = [float(y.subs(x, p)) for p in critical_points]  # Convert to float
#         minima = min(critical_values)
#         maxima = max(critical_values)
#
#     # Check for symmetry
#     is_symmetric = True if y == y.subs(x, -x) else False
#
#     # Calculate the period for periodic functions, including sin(x)
#     period = None
#     if sp.sin(x) in sp.expand(y).as_ordered_terms():
#         period = 2 * sp.pi
#
#     # Set default values for minima and maxima when no critical points found
#     if minima is None:
#         minima = "N/A"
#     if maxima is None:
#         maxima = "N/A"
#
#     return {
#         "Domain": domain,
#         "Range": (minima, maxima),
#         "Period": float(period) if period else "N/A",
#         "Maxima": maxima,
#         "Minima": minima,
#         "Symmetric": is_symmetric
#     }


# import sympy as sp
#
# def analyze_graph(data):
#     # Define the variable symbol
#     variable = 'x'
#     x = sp.symbols(variable)
#
#     # Parse the expression string into a SymPy expression
#     try:
#         y = sp.sympify(data['eqn'])
#     except sp.SympifyError:
#         return {
#             "Error": "Invalid expression"
#         }
#
#     # Calculate the derivative for finding maxima and minima
#     dy_dx = sp.diff(y, x)
#
#     # Find the domain (where the function is defined)
#     domain = sp.solve(sp.Eq(dy_dx, sp.nan), x)
#     domain = [float(value) for value in domain]  # Convert to float
#
#     # Find the critical points
#     critical_points = sp.solve(dy_dx, x)
#     critical_points = [float(point) for point in critical_points]  # Convert to float
#
#     # Initialize minima and maxima as None
#     minima = None
#     maxima = None
#
#     # Check if there are critical points before finding min and max
#     if critical_points:
#         critical_values = [float(y.subs(x, p)) for p in critical_points]  # Convert to float
#         minima = min(critical_values)
#         maxima = max(critical_values)
#
#     # Check for symmetry
#     is_symmetric = True if y == y.subs(x, -x) else False
#
#     # Calculate the period for periodic functions, including sin(x)
#     period = None
#     if sp.sin(x) in sp.expand(y).as_ordered_terms():
#         period = 2 * sp.pi
#
#     return {
#         "Domain": domain,
#         "Range": (float(minima), float(maxima)),
#         "Period": float(period) if period else None,
#         "Maxima": float(maxima) if maxima else None,
#         "Minima": float(minima) if minima else None,
#         "Symmetric": is_symmetric
#     }
#
#
# # import sympy as sp
# #
# #
# # def analyze_graph(data):
# #     # Define the variable symbol
# #     variable = 'x'
# #     x = sp.symbols(variable)
# #
# #     # Parse the expression string into a SymPy expression
# #     try:
# #         y = sp.sympify(data['eqn'])
# #     except sp.SympifyError:
# #         return {
# #             "Error": "Invalid expression"
# #         }
# #
# #     # Calculate the derivative for finding maxima and minima
# #     dy_dx = sp.diff(y, x)
# #
# #     # Find the domain (where the function is defined)
# #     domain = sp.solve(sp.Eq(dy_dx, sp.nan), x)
# #     domain = [float(value) for value in domain]  # Convert to float
# #
# #     # Find the critical points
# #     critical_points = sp.solve(dy_dx, x)
# #     critical_points = [float(point) for point in critical_points]  # Convert to float
# #
# #     # Initialize minima and maxima as None
# #     minima = None
# #     maxima = None
# #
# #     # Check if there are critical points before finding min and max
# #     if critical_points:
# #         critical_values = [float(y.subs(x, p)) for p in critical_points]  # Convert to float
# #         minima = min(critical_values)
# #         maxima = max(critical_values)
# #
# #     # Check for symmetry
# #     is_symmetric = True if sp.Eq(y, y.subs(x, -x)) else False
# #
# #     # Calculate the period for periodic functions
# #     period = None
# #     if sp.sin(variable) in sp.expand(y).as_ordered_terms():
# #         period = 2 * sp.pi
# #
# #     return {
# #         "Domain": domain,
# #         "Range": (float(minima), float(maxima)),
# #         "Period": float(period) if period else None,
# #         "Maxima": float(maxima) if maxima else None,
# #         "Minima": float(minima) if minima else None,
# #         "Symmetric": is_symmetric
# #     }
