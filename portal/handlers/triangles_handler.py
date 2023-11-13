import math

def classify_triangle(point1_str, point2_str, point3_str):

    point1 = tuple(map(float, point1_str.split(',')))
    point2 = tuple(map(float, point2_str.split(',')))
    point3 = tuple(map(float, point3_str.split(',')))

    # Calculate distances
    dist12 = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
    dist23 = ((point3[0] - point2[0])**2 + (point3[1] - point2[1])**2)**0.5
    dist13 = ((point3[0] - point1[0])**2 + (point3[1] - point1[1])**2)**0.5

    # Calculate angles
    angle1 = round(math.degrees(math.acos((dist23**2 + dist13**2 - dist12**2) / (2 * dist23 * dist13))), 2)
    angle2 = round(math.degrees(math.acos((dist12**2 + dist23**2 - dist13**2) / (2 * dist12 * dist23))), 2)
    angle3 = round(180 - angle1 - angle2, 2)

    # Check for collinearity
    if dist12 == dist23 == dist13:
        triangle_type = "Equilateral Triangle"
    elif dist12 == dist23 or dist23 == dist13 or dist13 == dist12:
        triangle_type = "Isosceles Triangle"
    else:
        # Check for angles
        sides = [dist12, dist23, dist13]
        sides.sort()

        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            triangle_type = "Right Triangle"
        elif sides[0]**2 + sides[1]**2 < sides[2]**2:
            triangle_type = "Obtuse Triangle"
        else:
            triangle_type = "Acute Triangle"

    # Calculate circumference
    circumference = round(dist12 + dist23 + dist13, 2)

    # Calculate area using Heron's formula
    s = circumference / 2
    area = round(math.sqrt(s * (s - dist12) * (s - dist23) * (s - dist13)), 2)

    # Return results
    return {
        "Type": triangle_type,
        "Dist12": round(dist12, 2), "Dist23": round(dist23, 2), "Dist13": round(dist13, 2),
        # "Distances": {"Dist12": round(dist12, 2), "Dist23": round(dist23, 2), "Dist13": round(dist13, 2)},
        "Angle1": angle1, "Angle2": angle2, "Angle3": angle3,
        # "Angles": {"Angle1": angle1, "Angle2": angle2, "Angle3": angle3},
        "Circumference": circumference,
        "Area": area
    }

# # Example usage:
# point1 = (0, 0)
# point2 = (1, 0)
# point3 = (0, 1)
#
# result = classify_triangle(point1, point2, point3)
# print(result)
