import math
from fractions import Fraction

def parse_point(point_str):
    try:
        x, y = map(float, point_str.split(","))
        return x, y
    except ValueError:
        return None

def x_y_intercept_worker(val):
    if '/' in val :
        number = float(Fraction(val))
        return number
    else:
        return int(val)


def slope_intercept_from_trig_function(function, value):
    if function == 'sin':
        angle = math.asin(value)
    elif function == 'cos':
        angle = math.acos(value)
    elif function == 'tan':
        angle = math.atan(value)
    elif function == 'cot':
        angle = math.atan(1 / value)
    elif function == 'cosec':
        angle = math.asin(1 / value)
    elif function == 'sec':
        angle = math.acos(1 / value)
    else:
        return "Invalid function. Please use 'sin', 'cos', 'tan', 'cot', 'cosec', or 'sec'"

    slope = math.tan(angle)
    return f"y = {slope} * x"

def calculate_line_properties(properties):
    pointA_str = properties.get("PointA")
    pointB_str = properties.get("PointB")
    # single_point_str = properties.get("SinglePoint")
    slope_str = properties.get("Slope")
    x_intercept_str = properties.get("XIntercept")
    y_intercept_str = properties.get("YIntercept")
    equation = properties.get("Equation")

    # Parse point strings to coordinates
    if pointA_str != '':
        pointA = parse_point(pointA_str)
    else:
        pointA = None

    if pointB_str != '':
        pointB = parse_point(pointB_str)
    else:
        pointB = None

    if slope_str != '':
        slope = x_y_intercept_worker(slope_str)
    else:
        slope = None

    if x_intercept_str != '':
        x_intercept = x_y_intercept_worker(x_intercept_str)
    else:
        x_intercept = None

    if y_intercept_str != '':
        y_intercept = x_y_intercept_worker(y_intercept_str)
    else:
        y_intercept = None


    # pointA = properties.get("PointA")
    # pointB = properties.get("PointB")
    # single_point = properties.get("SinglePoint")
    # slope = properties.get("Slope")
    # x_intercept = properties.get("XIntercept")
    # y_intercept = properties.get("YIntercept")



    if pointA and pointB:
        # Given point A and point B, calculate the rest of the properties
        if pointA == pointB:
            distance="0"
        else:
            distance = math.sqrt((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2)
        midpoint = ((pointA[0] + pointB[0]) / 2, (pointA[1] + pointB[1]) / 2)
        if pointB[0] - pointA[0] != 0:
            slope = (pointB[1] - pointA[1]) / (pointB[0] - pointA[0])
        else:
            slope = "Vertical line"
        if slope != "Vertical line":
            b = pointA[1] - slope * pointA[0]
            equation = f"y = {slope}x + {b}"
        else:
            equation = f"x = {pointA[0]}"
        if slope != "Vertical line":
            x_intercept = -b / slope
            y_intercept = b
        else:
            x_intercept = "No x-intercept (vertical line)"
            y_intercept = pointA[1]

        return {
            "Distance": distance,
            "Midpoint": midpoint,
            "Slope": slope,
            "Equation": equation,
            "X-Intercept": x_intercept,
            "Y-Intercept": y_intercept
        }

    # elif single_point:
    #     return {"Message": "Insufficient information. Please provide more details."}

    elif slope and x_intercept:
        b = -slope * x_intercept
        equation = f"y = {slope}x + {b}"
        y_intercept = b
        pointB = (0, y_intercept)
        distance = math.sqrt((pointB[0] - x_intercept) ** 2 + (pointB[1] - y_intercept) ** 2)
        midpoint = ((pointB[0] + x_intercept) / 2, (pointB[1] + y_intercept) / 2)

        return {
            "Distance": distance,
            "Midpoint": midpoint,
            "Slope": slope,
            "Equation": equation,
            "X-Intercept": x_intercept,
            "Y-Intercept": y_intercept,
            "PointA": pointA,
            "PointB": pointB
        }

    elif slope and y_intercept:
        b = y_intercept
        equation = f"y = {slope}x + {b}"
        x_intercept = -b / slope
        pointB = (x_intercept, 0)
        pointA = (0,y_intercept)
        distance = math.sqrt((pointB[0] - x_intercept) ** 2 + (pointB[1] - y_intercept) ** 2)
        midpoint = ((pointB[0] + x_intercept) / 2, (pointB[1] + y_intercept) / 2)

        return {
            "Distance": distance,
            "Midpoint": midpoint,
            "Slope": slope,
            "Equation": equation,
            "X-Intercept": x_intercept,
            "Y-Intercept": y_intercept,
            "PointA": pointA,
            "PointB": pointB
        }

    elif x_intercept is not None and y_intercept is not None:
        if x_intercept != 0:
            slope = -y_intercept / x_intercept
        else:
            slope = "Vertical line"
        pointA = (0, y_intercept)
        equation = f"y = {slope}x + {y_intercept}"
        pointB = (x_intercept, 0)
        distance = math.sqrt((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2)
        midpoint = ((pointB[0] + pointA[0]) / 2, (pointB[1] + pointA[1]) / 2)

        return {
            "Distance": distance,
            "Midpoint": midpoint,
            "Slope": slope,
            "Equation": equation,
            "X-Intercept": x_intercept,
            "Y-Intercept": y_intercept,
            "PointA": pointA,
            "PointB": pointB
        }
    elif slope_str != '':
        if '**' in slope_str:
            trig_func, val = slope_str.split('**')
            slope = x_y_intercept_worker(val)
            equation = slope_intercept_from_trig_function(trig_func, slope)
            return {
                "Slope": slope,
                "Equation": equation,
                # other properties you might want to return
            }
    elif (pointA and slope) or (pointB and slope):
        if pointA:
            x = pointA[0]
            y = pointA[1]
        else:
            x = pointB[0]
            y = pointB[1]

        equation = f"y = {slope}x + {y - slope * x}"

        if slope != 0:
            x_intercept = -y / slope
        else:
            x_intercept = "No x-intercept (horizontal line)"
        y_intercept = y
        pointB = (0, y_intercept)
        distance = math.sqrt((pointB[0] - x_intercept) ** 2 + (pointB[1] - y_intercept) ** 2)
        midpoint = ((pointB[0] + x_intercept) / 2, (pointB[1] + y_intercept) / 2)

        return {
            "Distance": distance,
            "Midpoint": midpoint,
            "Slope": slope,
            "Equation": equation,
            "X-Intercept": x_intercept,
            "Y-Intercept": y_intercept,
            "PointA": (x, y),
            "PointB": pointB
        }

    else:
        return {"Message": "Insufficient information. Please provide more details."}
