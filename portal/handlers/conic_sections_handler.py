import sympy as sp

def ellipse_parameters(equation):
    # Parse the equation
    x, y = sp.symbols('x y')
    parsed_eq = sp.sympify(equation)

    # Extract coefficients
    coeff_x_sq = parsed_eq.coeff(x**2)
    coeff_y_sq = parsed_eq.coeff(y**2)

    # Calculate lengths of major and minor axes
    a = sp.sqrt(1 / coeff_x_sq)
    b = sp.sqrt(1 / coeff_y_sq)

    # Calculate center
    center_x = 0
    center_y = 0

    # Calculate foci
    c = sp.sqrt(a**2 - b**2)

    foci = [str((center_x + c, center_y)), str((center_x - c, center_y))]
    focus = str(c.evalf())

    # if sp.im(c) == 0:  # Check if c is not a complex number
    #     foci = [f"{center_x + c}, {center_y}", f"{center_x - c}, {center_y}"]
    #     focus = float(c.evalf())
    # else:
    #     foci = "Complex foci"  # Handle complex foci appropriately
    #     focus = "Complex focus"  # Handle complex focus appropriately

    return {
        'center': f"({center_x}, {center_y})",
        'major_axis': str(round(a.evalf())),
        'minor_axis': str(round(b.evalf())),
        'foci': foci,
        'focus': focus
    }

# import sympy as sp
#
# def ellipse_parameters(equation):
#     # Parse the equation
#     x, y = sp.symbols('x y')
#     parsed_eq = sp.sympify(equation)
#
#     # Extract coefficients
#     coeff_x_sq = parsed_eq.coeff(x**2)
#     coeff_y_sq = parsed_eq.coeff(y**2)
#
#     # Calculate lengths of major and minor axes
#     a = sp.sqrt(1 / coeff_x_sq)
#     b = sp.sqrt(1 / coeff_y_sq)
#
#     # Calculate center
#     center_x = 0
#     center_y = 0
#
#     # Calculate foci
#     c = sp.sqrt(a**2 - b**2)
#     foci = [f"{center_x + c}, {center_y}", f"{center_x - c}, {center_y}"]
#
#     # Calculate focus
#     focus = float(c.evalf())
#
#     return {
#         'center': f"({center_x}, {center_y})",
#         'major_axis': str(a.evalf()),
#         'minor_axis': str(b.evalf()),
#         'foci': foci,
#         'focus': str(focus)
#     }


# import sympy as sp
#
# def ellipse_parameters(equation):
#     # Parse the equation
#     x, y = sp.symbols('x y')
#     parsed_eq = sp.sympify(equation)
#
#     # Extract coefficients
#     coeff_x_sq = parsed_eq.coeff(x**2)
#     coeff_y_sq = parsed_eq.coeff(y**2)
#
#     # Calculate lengths of major and minor axes
#     a = sp.sqrt(1 / coeff_x_sq)
#     b = sp.sqrt(1 / coeff_y_sq)
#
#     # Calculate center
#     center_x = 0
#     center_y = 0
#
#     # Calculate foci
#     c = sp.sqrt(a**2 - b**2)
#     foci = [(float(center_x + c), float(center_y)), (float(center_x - c), float(center_y))]
#
#     # Calculate focus
#     focus = float(c.evalf())
#
#     return {
#         'center': (float(center_x), float(center_y)),
#         'major_axis': float(a.evalf()),
#         'minor_axis': float(b.evalf()),
#         'foci': foci,
#         'focus': focus
#     }


# import sympy as sp
# import re
#
# def ellipse_parameters(equation):
#     # Parse the equation
#     x, y = sp.symbols('x y')
#     parsed_eq = sp.sympify(equation)
#
#     # Extract coefficients
#     coeff_x_sq = parsed_eq.coeff(x**2)
#     coeff_y_sq = parsed_eq.coeff(y**2)
#
#     # Calculate lengths of major and minor axes
#     a = sp.sqrt(1 / coeff_x_sq)
#     b = sp.sqrt(1 / coeff_y_sq)
#
#     # Calculate center
#     center_x = 0
#     center_y = 0
#
#     # Calculate foci
#     c = sp.sqrt(a**2 - b**2)
#     foci = [(center_x + c, center_y), (center_x - c, center_y)]
#
#     # Calculate focus
#     focus = c.evalf()
#
#     return {
#         'center': (center_x, center_y),
#         'major_axis': a.evalf(),
#         'minor_axis': b.evalf(),
#         'foci': foci,
#         'focus': focus
#     }