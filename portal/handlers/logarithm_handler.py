import math
import re
import sympy as sp
def simplify_logarithmic_expression(expression_str,radiovalue="dec"):
    # Parse the input string into a symbolic expression
    expression = sp.sympify(expression_str)

    # Separate log terms
    separated_expression = sp.expand_log(expression, force=True)

    # Combine log terms at the end
    combined_expression = sp.logcombine(separated_expression, force=True)

    return str(combined_expression)

def calculate_log_from_expression(log_expression, radiovalue="dec"):
    # Regular expression to find log expressions
    log_expression = log_expression.replace("^", "**")

    if "a" in log_expression or "b" in log_expression:
        return simplify_logarithmic_expression(log_expression)
    else:
        log_expression = re.sub(r'ln\(([^)]+)\)', r'log(e,\1)', log_expression)

        # Split the input expression based on addition operator
        # terms = re.split(r'\s*\+\s*', log_expression)
        terms = re.split(r'\s*[-+]\s*', log_expression)

        # Regular expression to find log expressions
        pattern = r"log\(([^,]+)(?:,([^)]+))?\)"

        # Calculate logarithm for each term
        results = []
        for term in terms:
            # Find all matches of log expressions in the term
            matches = re.findall(pattern, term)

            if matches:
                for match in matches:
                    value_str, base_str = match

                    if value_str == 'e':
                        value = math.e
                    else:
                        value = float(value_str)

                    if base_str and base_str.lower() == 'e':
                        base = math.e
                    else:
                        base = float(base_str) if base_str else 10  # Set default base to 10 if not provided

                    if base <= 0 or value <= 0 or base == 1:
                        return "Invalid input. Base and value must be positive, and base cannot be 1."

                    result = math.log(value, base)
                    results.append(result)
            else:
                return "No valid log expression found in the input."

        # Return the sum of logarithm results
        if radiovalue == "integer":
            return int(sum(results))
        else:
            return sum(results)
# def calculate_log_from_expression(log_expression, radiovalue="dec"):
#     # Check if the expression contains specific variables or ln
#     if "a" in log_expression or "b" in log_expression:
#         # Replace ln with log(e) for consistency
#
#
#         # Simplify the expression using the specified function
#         return simplify_logarithmic_expression(log_expression)
#
#     if "ln" in log_expression:
#         log_expression = log_expression.replace("ln", "log(e)")
#
#     # Regular expression to find log expressions (allowing both log and ln)
#     pattern = r"log\(([^,]+)(?:,(\d+|e))?\)"
#
#     # Find all matches of log expressions in the input
#     matches = re.findall(pattern, log_expression)
#
#     if matches:
#         # Calculate logarithm for each matched expression
#         results = []
#         for match in matches:
#             value_str, base_str = match
#
#             value = math.e if value_str == 'e' else float(value_str)
#             base = math.e if base_str.lower() == 'e' else float(base_str) if base_str else 10
#
#             if base <= 0 or value <= 0 or base == 1:
#                 return "Invalid input. Base and value must be positive, and base cannot be 1."
#
#             result = math.log(value, base)
#             results.append(result)
#
#         # Return the sum of logarithm results
#         return int(sum(results)) if radiovalue == "integer" else sum(results)
#     else:
#         return "No valid log expression found in the input."