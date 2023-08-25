def evaluate_complex_expression(expression):
    expression = expression.replace('i', 'j')
    expression = expression.replace('^', '**')
    result = ''
    try:
        result = eval(expression, {"__builtins__": None}, {'j': 1j})
        message = f"Data extracted successfully"
    except ValueError:
        message = 'Invalid complex expression'
    except Exception as e:
        message = f'Error: Could not calculate the expression ({e})'
    return message, result
