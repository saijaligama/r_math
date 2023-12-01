import sympy as sp
import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr
import io
import base64
from sympy import Abs
import matplotlib
matplotlib.use('Agg')

def calculate_line_properties(m, c):
    m_fraction = Fraction(m).limit_denominator()
    c_fraction = Fraction(c).limit_denominator()
    return m_fraction, c_fraction


def slope_intercept_from_trig_function(func, x_val):
    if func == 'sin':
        slope = np.cos(x_val)
        intercept = -np.sin(x_val)
    # Additional cases for other trig functions
    # elif func == 'cos':
    #     ...
    # elif func == 'tan':
    #     ...
    # Add cases for other trig functions as needed
    else:
        slope = None
        intercept = None

    return slope, intercept


def plot_function_with_line(expression, x_min, x_max, points=1000, angle=0):
    x = np.linspace(x_min, x_max, points)

    try:
        y = [eval(expression, {'x': x_val, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                               'cot': lambda x: 1 / np.tan(x), 'cosec': lambda x: 1 / np.sin(x),
                               'sec': lambda x: 1 / np.cos(x), 'exp': np.exp, 'Abs': np.abs}) for
             x_val in x]

        # Rotate the coordinates by the specified angle
        angle_rad = np.radians(angle)
        coordinates = np.column_stack((x, y))
        rotated_coordinates = np.dot(coordinates, np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                                                            [np.sin(angle_rad), np.cos(angle_rad)]]).T)

        plt.figure(figsize=(5, 4))
        plt.plot(rotated_coordinates[:, 0], rotated_coordinates[:, 1], label=f'y = {expression}')
        plt.title(f'Graph of y = {expression} (Rotated by {angle} degrees)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(y=0, color='black', linewidth=0.5)  # Add x-axis
        plt.axvline(x=0, color='black', linewidth=0.5)  # Add y-axis
        plt.grid(True)
        if "tan" in expression or "cot" in expression:
            plt.ylim(-5, 5)
        plt.legend()

        # Convert plot to base64
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
        plt.close()
        return plot_base64
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def plot_function_with_2_lines(expression_list, x_min, x_max, points=1000, angle=0):
    expression1 = expression_list[0]
    expression2 = expression_list[1]

    x_expression1 = np.linspace(x_min, x_max, points)
    x_expression2 = np.linspace(x_min, x_max, points)

    try:
        y1 = [eval(expression1, {'x': x_val, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                               'cot': lambda x: 1 / np.tan(x), 'cosec': lambda x: 1 / np.sin(x),
                               'sec': lambda x: 1 / np.cos(x), 'exp': np.exp, 'Abs': np.abs}) for
             x_val in x_expression1]

        y2 = [eval(expression2, {'x': x_val, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                                'cot': lambda x: 1 / np.tan(x), 'cosec': lambda x: 1 / np.sin(x),
                                'sec': lambda x: 1 / np.cos(x), 'exp': np.exp, 'Abs': np.abs}) for
             x_val in x_expression2]

        # Rotate the coordinates by the specified angle
        angle_rad = np.radians(angle)
        coordinates1 = np.column_stack((x_expression1, y1))
        rotated_coordinates1 = np.dot(coordinates1, np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                                                            [np.sin(angle_rad), np.cos(angle_rad)]]).T)
        coordinates2 = np.column_stack((x_expression2, y2))
        rotated_coordinates2 = np.dot(coordinates2, np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                                                              [np.sin(angle_rad), np.cos(angle_rad)]]).T)

        plt.figure(figsize=(5, 4))
        plt.plot(rotated_coordinates1[:, 0], rotated_coordinates1[:, 1], label=f'y = {expression1}')
        plt.plot(rotated_coordinates2[:, 0], rotated_coordinates2[:, 1], label=f'y = {expression2}')
        plt.title(f'Graph of y = {expression1} and y = {expression2} (Rotated by {angle} degrees)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.axhline(y=0, color='black', linewidth=0.5)  # Add x-axis
        plt.axvline(x=0, color='black', linewidth=0.5)  # Add y-axis
        plt.grid(True)
        if "tan" in expression1 or "cot" in expression1 or "tan" in expression2 or "cot" in expression2:
            plt.ylim(-5, 5)
        plt.legend()

        # Convert plot to base64
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
        plt.close()
        return plot_base64
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def analyze_graph2(data):
    # Define the variable symbol
    variable = 'x'
    x = sp.symbols(variable)
    print(data)

    base64_plot = plot_function_with_2_lines([data['eqn1'],data['eqn2']], -2 * np.pi, 2 * np.pi,angle = int(data['angle']))

    return {"base64_plot": base64_plot}


    # if data['eqn1'] == "x**2":
    #     return {
    #         "Domain": ["All Real Numbers"],
    #         "Range": ["0", "+Inf"],
    #         "Period": "N/A",
    #         "Maxima": "No Max",
    #         "Minima": "0",
    #         "Symmetric": "Yes",
    #         "base64_plot": base64_plot,
    #         "eqn": data['eqn'],
    #         "vari": variable
    #     }
    #
    # # Parse the expression string into a SymPy expression
    # try:
    #     y = sp.sympify(data['eqn'])
    # except sp.SympifyError:
    #     return {
    #         "Error": "Invalid expression"
    #     }
    #
    # # Calculate the derivative for finding maxima and minima
    # dy_dx = sp.diff(y, x)
    #
    # # Find the domain (where the function is defined)
    # domain = sp.solve(sp.Eq(dy_dx, sp.nan), x)
    # domain = [float(value) for value in domain]  # Convert to float
    #
    # # Find the critical points for tan(x)
    # if 'tan' in str(y):
    #     critical_points = [float(n * np.pi / 2) for n in range(-5, 6, 2)]  # Odd multiples of pi/2
    # else:
    #     try:
    #         critical_points = sp.solve(dy_dx, x)
    #         critical_points = [float(point) for point in critical_points]
    #     except NotImplementedError:
    #         critical_points = [] # Convert to float
    #
    # # Initialize minima and maxima as None
    # minima = None
    # maxima = None
    #
    # # Check if there are critical points before finding min and max
    # if critical_points:
    #     critical_values = [float(y.subs(x, p)) for p in critical_points]  # Convert to float
    #     minima = min(critical_values)
    #     maxima = max(critical_values)
    #
    # # Check for symmetry
    # is_symmetric = True if y == y.subs(x, -x) else False
    #
    # # Calculate the period for periodic functions, including sin(x)
    # period = np.pi if 'tan' in str(y) else None
    #
    # # Set default values for minima and maxima when no critical points found
    # if minima is None:
    #     minima = "N/A"
    # if maxima is None:
    #     maxima = "N/A"
    #
    # data_x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    # data_y = [eval(data['eqn'], {'x': x_val, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
    #                              'cot': lambda x: 1 / np.tan(x), 'cosec': lambda x: 1 / np.sin(x),
    #                              'sec': lambda x: 1 / np.cos(x), 'exp': np.exp}) for x_val in data_x]
    #
    # return {
    #     "Domain": domain,
    #     "Range": (minima, maxima),
    #     "Period": float(period) if period else "N/A",
    #     "Maxima": maxima,
    #     "Minima": minima,
    #     "Symmetric": is_symmetric,
    #     "base64_plot": base64_plot,
    #     "eqn": data['eqn'],
    #     "vari": variable
    # }


import numpy as np
import sympy as sp


# def analyze_graph(data):
#
#     variable = 'x'
#     x = sp.symbols(variable)
#
#     # Parse the expression string into a SymPy expression
#     y = parse_expr(data['eqn'])
#
#     base64_plot = plot_function_with_line(data['eqn'], -2 * np.pi, 2 * np.pi, angle=int(data['angle']))
#
#     dy_dx = sp.diff(y, x)
#
#     # Find the domain (where the function is defined)
#     domain = sp.solveset(sp.denom(dy_dx) != 0, x)
#     domain_values = [float(value) for value in domain if value.is_real]
#
#     # Find the critical points for periodic functions
#     critical_points = sp.solveset(dy_dx, x)
#     print(critical_points)
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
#     is_symmetric = y.equals(y.subs(x, -x))
#
#     # Calculate the period for periodic functions
#     period = sp.periodicity(y, x)
#
#     # Set default values for minima and maxima when no critical points found
#     if minima is None:
#         minima = "N/A"
#     if maxima is None:
#         maxima = "N/A"
#
#     return {
#         "Domain": domain_values,
#         "Range": (minima, maxima),
#         "Period": float(period) if period is not None else "N/A",
#         "Maxima": maxima,
#         "Minima": minima,
#         "Symmetric": is_symmetric,
#         "base64_plot": base64_plot,
#         "eqn": data['eqn'],
#         "vari": variable
#     }


def analyze_graph(data):
    # Define the variable symbol
    variable = 'x'
    x = sp.symbols(variable)
    print(data)

    base64_plot = plot_function_with_line(data['eqn'], -2 * np.pi, 2 * np.pi,angle = int(data['angle']))

    if data['eqn'] == "x**2":
        return {
            "Domain": ["All Real Numbers"],
            "Range": ["0", "+Inf"],
            "Period": "N/A",
            "Maxima": "No Max",
            "Minima": "0",
            "Symmetric": "Yes",
            "base64_plot": base64_plot,
            "eqn": data['eqn'],
            "vari": variable
        }

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

    # Find the critical points for tan(x)
    if 'tan' in str(y):
        critical_points = [float(n * np.pi / 2) for n in range(-5, 6, 2)]  # Odd multiples of pi/2
    else:
        try:
            critical_points = sp.solve(dy_dx, x)
            critical_points = [float(point) for point in critical_points]
        except NotImplementedError:
            critical_points = [] # Convert to float

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
    period = np.pi if 'tan' in str(y) else None

    # Set default values for minima and maxima when no critical points found
    if minima is None:
        minima = "N/A"
    if maxima is None:
        maxima = "N/A"

    data_x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    data_y = [eval(data['eqn'], {'x': x_val, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                                 'cot': lambda x: 1 / np.tan(x), 'cosec': lambda x: 1 / np.sin(x),
                                 'sec': lambda x: 1 / np.cos(x), 'exp': np.exp}) for x_val in data_x]

    return {
        "Domain": domain,
        "Range": (minima, maxima),
        "Period": float(period) if period else "N/A",
        "Maxima": maxima,
        "Minima": minima,
        "Symmetric": is_symmetric,
        "base64_plot": base64_plot,
        "eqn": data['eqn'],
        "vari": variable
    }

# def analyze_graph(data):
#     # Define the variable symbol
#     variable = 'x'
#     x = sp.symbols(variable)
#
#     base64_plot = plot_function_with_line(data['eqn'], -2*np.pi, 2*np.pi)
#
#     if data['eqn'] == "x**2":
#         return {
#             "Domain": ["All Real Numbers"],
#             "Range": ["0","+Inf"],
#             "Period": "N/A",
#             "Maxima": "No Max",
#             "Minima": "0",
#             "Symmetric": "Yes",
#             "base64_plot": base64_plot,
#             "eqn": data['eqn'],
#             "vari": variable
#
#         }
#
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
#     # Set default values for minima and maxima when no critical points found
#     if minima is None:
#         minima = "N/A"
#     if maxima is None:
#         maxima = "N/A"
#     data_x = np.linspace(-2*np.pi, 2*np.pi, 1000)
#     data_y = [eval(data['eqn'], {'x': x_val, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan, 'cot': lambda x: 1 / np.tan(x),
#                                'cosec': lambda x: 1 / np.sin(x), 'sec': lambda x: 1 / np.cos(x), 'exp': np.exp}) for
#              x_val in data_x]
#
#     return {
#         "Domain": domain,
#         "Range": (minima, maxima),
#         "Period": float(period) if period else "N/A",
#         "Maxima": maxima,
#         "Minima": minima,
#         "Symmetric": is_symmetric,
#         "base64_plot": base64_plot,
#         "eqn": data['eqn'],
#         "vari": variable
#
#     }


# if __name__=="__main__":
#     data={}
#     data['eqn'] = "5*x+4"
#     print(analyze_graph(data))


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
