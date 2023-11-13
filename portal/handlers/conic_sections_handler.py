import sympy as sp

def parabola_parameters(equation):
    # Parse the equation
    x, y = sp.symbols('x y')

    # Extract the expression from the equation
    if "=" in equation:
        parsed_eq = sp.sympify(equation.split("=")[1].strip())
    else:
        parsed_eq = sp.sympify(equation)

    # Extract coefficients
    if y in parsed_eq.free_symbols:
        a, b, c = parsed_eq.as_coefficients_dict()[y**2], parsed_eq.as_coefficients_dict()[y], parsed_eq.as_coefficients_dict()[1]
        form = "Vertical"
        vertex_x = -b / (2 * a)
        vertex_y = -b**2 / (4 * a) + c
        focus = (vertex_x, vertex_y + 1 / (4 * a))
        directrix = vertex_y - 1 / (4 * a)
        axis = x
    elif x in parsed_eq.free_symbols:
        a, b, c = parsed_eq.as_coefficients_dict()[x**2], parsed_eq.as_coefficients_dict()[x], parsed_eq.as_coefficients_dict()[1]
        form = "Horizontal"
        vertex_x = -b**2 / (4 * a) + c
        vertex_y = -b / (2 * a)
        focus = (vertex_x + 1 / (4 * a), vertex_y)
        directrix = vertex_x - 1 / (4 * a)
        axis = y
    else:
        raise ValueError("Invalid parabola equation")

    return {
        'vertex': f"({vertex_x}, {vertex_y})",
        'form': form,
        'focus': f"{focus} (approx)",
        'directrix': f"{directrix} (approx)",
        'axis': str(axis)
    }

# import sympy as sp

def hyperbola_parameters(equation):
    # Parse the equation
    x, y = sp.symbols('x y')

    # Extract the expression from the equation
    if "=" in equation:
        parsed_eq = sp.sympify(equation.split("=")[0].strip())
        print(parsed_eq)
    else:
        parsed_eq = sp.sympify(equation)
        print(parsed_eq)

    # Extract coefficients
    coeff_x_sq = parsed_eq.coeff(x**2)
    coeff_y_sq = parsed_eq.coeff(y**2)
    print(coeff_x_sq, coeff_y_sq)
    # Determine the form of the hyperbola
    if coeff_x_sq < 0:
        form = "Vertical"
        a = sp.sqrt(abs(1 / coeff_x_sq))
        b = sp.sqrt(abs(1 / coeff_y_sq))
    elif coeff_y_sq < 0:
        form = "Horizontal"
        a = sp.sqrt(abs(1 / coeff_y_sq))
        b = sp.sqrt(abs(1 / coeff_x_sq))
    else:
        raise ValueError("Invalid hyperbola equation")

    # Calculate center
    solutions = sp.solve([parsed_eq.subs(y, 0), parsed_eq.subs(x, 0)], (x, y))
    print(solutions)
    real_solutions = [val.evalf() for sol,val in solutions.items() if val.is_real]
    print(real_solutions)

    if len(real_solutions) == 2:
        center_x, center_y = real_solutions
    else:
        raise ValueError("Unable to determine the center of the hyperbola")

    # Calculate foci
    c = sp.sqrt(a*2 + b*2)
    foci = [(center_x + c, center_y), (center_x - c, center_y)]

    return {
        'center': f"({center_x}, {center_y})",
        'form': str(form),
        'distance_vertices': str(2*a.evalf()),
        'distance_foci': str(2*c.evalf()),
        'foci': str(foci)
    }

# def hyperbola_parameters(equation):
#     # Parse the equation
#     x, y = sp.symbols('x y')
#     parsed_eq = sp.sympify(equation)
#
#     # Extract coefficients
#     coeff_x_sq = parsed_eq.coeff(x**2)
#     coeff_y_sq = parsed_eq.coeff(y**2)
#
#     # Determine the form of the hyperbola
#     if coeff_x_sq < 0:
#         form = "Vertical"
#     elif coeff_y_sq < 0:
#         form = "Horizontal"
#     else:
#         raise ValueError("Invalid hyperbola equation")
#
#     # Calculate lengths of major and minor axes
#     a = sp.sqrt(abs(1 / coeff_x_sq))
#     b = sp.sqrt(abs(1 / coeff_y_sq))
#
#     # Calculate center
#     center_x, center_y = sp.solve([parsed_eq.subs(y, 0), parsed_eq.subs(x, 0)], (x, y))[0]
#
#     # Calculate foci
#     c = sp.sqrt(a**2 + b**2)
#     foci = [str((center_x + c, center_y)), str((center_x - c, center_y))]
#
#     return {
#         'center': f"({center_x}, {center_y})",
#         'form': form,
#         'distance_vertices': str(2*a.evalf()),
#         'distance_foci': str(2*c.evalf()),
#         'foci': foci
#     }

# Example usage:
# equation_str_hyperbola = "x**2/4 - y**2/9 = 1"
# params_hyperbola = hyperbola_parameters(equation_str_hyperbola)
# print(params_hyperbola)

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