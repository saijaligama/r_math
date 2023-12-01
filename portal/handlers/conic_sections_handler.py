import sympy as sp
import re
import math

def parabola_parameters(equation):
    # Extract coefficients from the equation using regular expressions
    match = re.match(r'\s*x\*\*2/(\d+)\s*[=<>]\s*y\s*$', equation)
    if not match:
        raise ValueError("Invalid parabola equation format")

    # Extract coefficient a
    a = int(match.group(1))

    # Vertex (h, k)
    h = 0
    k = 0
    vertex = (h, k)

    # Form of the parabola
    form = equation

    # Focus (h, k + 1/(4a)) for upward opening parabola
    # Focus (h, k - 1/(4a)) for downward opening parabola
    focus = (h, k + 1/(4*a))

    # Directrix: y = k - 1/(4a) for upward opening parabola
    # Directrix: y = k + 1/(4a) for downward opening parabola
    directrix = k - 1/(4*a)

    # Axis of symmetry: x = h
    axis_of_symmetry = h

    # Return the results
    return {
        "vertex": vertex,
        "form": form,
        "focus": focus,
        "directrix": directrix,
        "axis": str(axis_of_symmetry)
    }

# # Example usage with a parabola equation
# parabola_equation = "x**2/4 = y"
# parabola_result = parabola_properties(parabola_equation)
#
# # Print the results for the parabola
# for key, value in parabola_result.items():
#     print(f"{key}: {value}")

###############################################################################################

# def hyperbola_parameters(equation):
#     # Extract coefficients from the equation using regular expressions
#     match = re.match(r'\s*x\*\*2/(\d+)\s*-\s*y\*\*2/(\d+)\s*=\s*1\s*', equation)
#     if not match:
#         raise ValueError("Invalid hyperbola equation format")
#
#     # Extract coefficients a_squared and b_squared
#     a_squared, b_squared = map(int, match.groups())
#
#     # Calculate semi-major and semi-minor axes
#     a = math.sqrt(a_squared)
#     b = math.sqrt(b_squared)
#
#     # Center (h, k)
#     h = 0
#     k = 0
#     center = (h, k)
#
#     # Vertex (h + a, k) and (h - a, k)
#     vertex1 = (h + a, k)
#     vertex2 = (h - a, k)
#
#     # Form of the hyperbola
#     form = equation
#
#     # Distance from the center to the focus
#     c = math.sqrt(a_squared + b_squared)
#
#     # Focus (h + c, k) and (h - c, k)
#     focus1 = (h + c, k)
#     focus2 = (h - c, k)
#
#     # Directrices: x = h + a/e and x = h - a/e
#     e = c / a
#     directrix1 = h + a/e
#     directrix2 = h - a/e
#
#     # Axis length (major and minor axes)
#     major_axis = 2 * a
#     minor_axis = 2 * b
#
#     # Return the results
#     return {
#         "center": center,
#         "Vertex1": vertex1,
#         "Vertex2": vertex2,
#         "Form": form,
#         "Focus1": focus1,
#         "Focus2": focus2,
#         "Directrix1": directrix1,
#         "Directrix2": directrix2,
#         "MajorAxis": major_axis,
#         "MinorAxis": minor_axis
#     }

def hyperbola_parameters(equation):
    # Extract coefficients from the equation using regular expressions
    match = re.match(r'\s*x\*\*2/(\d+)\s*-\s*y\*\*2/(\d+)\s*=\s*1\s*', equation)
    if not match:
        raise ValueError("Invalid hyperbola equation format")

    # Extract coefficients a_squared and b_squared
    a_squared, b_squared = map(int, match.groups())

    # Calculate semi-major and semi-minor axes
    a = math.sqrt(a_squared)
    b = math.sqrt(b_squared)
    #
    # solutions = sp.solve([parsed_eq.subs(y, 0), parsed_eq.subs(x, 0)], (x, y))
    # print(solutions)
    # real_solutions = [val.evalf() for sol,val in solutions.items() if val.is_real]
    # print(real_solutions)
    #
    # if len(real_solutions) == 2:
    #     center_x, center_y = real_solutions
    # else:
    #     raise ValueError("Unable to determine the center of the hyperbola")
    # Center (h, k)
    h = 0
    k = 0
    center = (h, k)

    # Form of the hyperbola
    form = equation

    # Distance between vertices (2a)
    distance_vertices = 2 * a

    # Distance between foci (2c)
    c = math.sqrt(a_squared + b_squared)
    distance_foci = 2 * c

    # Foci (h + c, k) and (h - c, k)
    focus1 = (h + c, k)
    focus2 = (h - c, k)

    area = math.pi * a * b
    circumference = 2 * math.pi * math.sqrt((a ** 2 + b ** 2) / 2)

    # Return the results
    return {
        "center": center,
        "form": form,
        "distance_vertices": distance_vertices,
        "distance_foci": distance_foci,
        "Focus1": focus1,
        "Focus2": focus2,
        "foci": str((focus1,focus2)),
        "area":area,
        "circumference":circumference
    }

###############################################################################################


import re
import math

def ellipse_parameters(equation):
    # Extract coefficients from the equation using regular expressions
    match = re.match(r'\s*x\*\*2/(\d+)\s*\+\s*y\*\*2/(\d+)\s*=\s*(\d+)\s*', equation)
    if not match:
        raise ValueError("Invalid ellipse equation format")

    # Extract coefficients a_squared, b_squared, and rhs_coefficient
    a_squared, b_squared, rhs_coefficient = map(int, match.groups())

    # Calculate semi-major and semi-minor axes
    a = math.sqrt(a_squared)
    b = math.sqrt(b_squared)

    # Center (h, k)
    h = 0
    k = 0
    center = (h, k)

    # Vertex (h, k)
    vertex = (h, k)

    # Form of the ellipse
    form = equation

    # Distance from the center to the focus
    c = math.sqrt(abs(a_squared - b_squared))

    # Focus (h + c, k) and (h - c, k)
    focus1 = (h + c, k)
    focus2 = (h - c, k)

    # Directrices: x = h + a/e and x = h - a/e
    e = c / a
    directrix1 = h + a/e
    directrix2 = h - a/e

    # Axis length (major and minor axes)
    major_axis = 2 * a
    minor_axis = 2 * b

    area = math.pi * a * b
    circumference = 2 * math.pi * math.sqrt((a ** 2 + b ** 2) / 2)

    # Return the results
    return {
        "center": center,
        "vertex": vertex,
        "form": form,
        "focus": focus1,
        "Focus2": focus2,
        "foci":(focus1,focus2),
        "Directrix1": directrix1,
        "Directrix2": directrix2,
        "major_axis": major_axis,
        "minor_axis": minor_axis,
        "RightHandSideCoefficient": rhs_coefficient,
        "area": area,
        "circumference": circumference
    }

# # Example usage with the provided ellipse equation
# equation = "x**2/4 + y**2/9 = 10"
# result = ellipse_properties(equation)
#
# # Print the results
# for key, value in result.items():
#     print(f"{key}: {value}")
