import math

def analyze_point(coord_str):
    # Split the input string into x and y coordinates
    x_str, y_str = coord_str.split(',')

    # Convert coordinates to float
    x = float(x_str)
    y = float(y_str)

    # Check quadrant
    if x > 0 and y > 0:
        quadrant = "Quadrant I"
    elif x < 0 and y > 0:
        quadrant = "Quadrant II"
    elif x < 0 and y < 0:
        quadrant = "Quadrant III"
    elif x > 0 and y < 0:
        quadrant = "Quadrant IV"
    elif x == 0 and y == 0:
        quadrant = "At Origin"
    elif x < 0  and y == 0:
        quadrant = "Negative X-axis"
    elif x > 0 and y==0:
        quadrant = "Positive X-axis"
    else:
        if x == 0 and y != 0:
            quadrant = "Negative Y-axis" if y < 0 else "Positive Y-axis"

    # Calculate distance from origin
    distance = math.sqrt(x ** 2 + y ** 2)

    # Calculate theta (angle in radians)
    if x != 0:
        theta = math.atan(y / x)
    elif y > 0:
        theta = math.pi / 2
    elif y < 0:
        theta = -math.pi / 2
    else:
        theta = 0

    return {
        "quadrant": quadrant,
        "distance": distance,
        "theta": theta
    }

# def analyze_point(coord_str):
#     # Split the input string into x and y coordinates
#     x_str, y_str = coord_str.split(',')
#
#     # Convert coordinates to float
#     x = float(x_str)
#     y = float(y_str)
#
#     # Check quadrant
#     if x > 0 and y > 0:
#         quadrant = "Quadrant I"
#     elif x < 0 and y > 0:
#         quadrant = "Quadrant II"
#     elif x < 0 and y < 0:
#         quadrant = "Quadrant III"
#     elif x > 0 and y < 0:
#         quadrant = "Quadrant IV"
#     elif x == 0 and y != 0:
#         quadrant = "On Y-axis"
#     elif x != 0 and y == 0:
#         quadrant = "On X-axis"
#     else:
#         quadrant = "At Origin"
#
#     # Calculate distance from origin
#     distance = math.sqrt(x ** 2 + y ** 2)
#
#     # Calculate theta (angle in radians)
#     if x != 0:
#         theta = math.atan(y / x)
#     elif y > 0:
#         theta = math.pi / 2
#     elif y < 0:
#         theta = -math.pi / 2
#     else:
#         theta = 0
#
#     return {
#         "quadrant": quadrant,
#         "distance": distance,
#         "theta": theta
#     }


# Example usage:
# coord_str = "3,4"
# result = analyze_point(coord_str)
# print(result)
# print("Point ({}) is in {}, distance from origin is {:.2f}, and theta is {:.2f} radians.".format(coord_str, result["quadrant"], result["distance"], result["theta"]))
