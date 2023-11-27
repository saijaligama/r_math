import sympy as sp

def manual_replace_sqrt_with_power(expr_str):
    # Find occurrences of sqrt(x) and replace them with x**(1/2)
    result_str = ""
    i = 0
    while i < len(expr_str):
        if expr_str[i:i+4] == "sqrt":
            j = i + 4
            while j < len(expr_str) and expr_str[j] != '(':
                j += 1

            if j < len(expr_str) and expr_str[j] == '(':
                k = j + 1
                while k < len(expr_str) and expr_str[k] != ')':
                    k += 1

                if k < len(expr_str) and expr_str[k] == ')':
                    sqrt_content = expr_str[j+1:k]
                    result_str += f"{sqrt_content}^(1/2)"
                    i = k + 1
                    continue

        result_str += expr_str[i]
        i += 1

    return result_str

# def exponential_expression_calculator(expression, output_type="default"):
#     try:
#         expression = expression.replace("^", "**")
#         # Parse the expression using sympy
#         expr = sp.sympify(expression)
#
#         # Factor the expression
#         simplified_expr = sp.factor(expr)
#
#         # Simplify the factored expression
#         simplified_expr = sp.simplify(simplified_expr)
#         # simplified_expr = sp.simplify(simplified_expr)
#         # simplified_expr = simplified_expr.evalf()
#
#         if output_type == "integer":
#             # Manually replace square roots with power representation
#             simplified_expr = manual_replace_sqrt_with_power(str(simplified_expr))
# #             print(simplified_expr)
# #             simplified_expr = sp.sympify(simplified_expr_str)
#
#         return str(simplified_expr)
#     except sp.SympifyError:
#         return "Invalid expression"


def exponential_expression_calculator(expression, output_type="default"):
    try:
        expression = expression.replace("^", "**")

        # Split the expression by the operator '+'
        parts = expression.split('+')
        print(parts)

        # Parse and simplify each part
        simplified_parts = []
        for part in parts:
            part_expr = sp.sympify(part)
            simplified_part = sp.simplify(part_expr)
            simplified_parts.append(simplified_part)

        # Combine the simplified parts
        simplified_expr = sum(simplified_parts)

        if output_type == "integer":
            # Manually replace square roots with power representation
            simplified_expr = manual_replace_sqrt_with_power(str(simplified_expr))
            # simplified_expr = sp.sympify(simplified_expr_str)

        return str(simplified_expr)
    except sp.SympifyError:
        return "Invalid expression"