from flask import jsonify
from portal.application.complex_numbers import evaluate_complex_expression
import cmath


def complex_numbers_calc(data):
    type = data["type"]
    complex_expression_ = data["complex_expression_"]
    try:
        message, result = evaluate_complex_expression(complex_expression_)
    except Exception as e:
        message = f'Error: Could not calculate the expression ({e})'
        if type == 'Complex Expressions':
            return jsonify(
                {"message": message, "result_real": "na.", "result_imagery": "na."})
        else:
            return jsonify(
                {"message": message, "result": "na."})
    if type == 'Complex Expressions':
        return jsonify({"message": message, "result_real": str(result.real), "result_imagery": str(result.imag)})
    elif type == 'Absolute':
        return jsonify({"message": message, "result": str(abs(result))})
    elif type == 'Angle':
        return jsonify({"message": message, "result": str(cmath.phase(result))})
    elif type == 'Conjugate':
        return jsonify({"message": message, "result": str(result.conjugate())})
    elif type == 'Real':
        return jsonify({"message": message, "result": str(result.real)})
    elif type == 'imagery':
        return jsonify({"message": message, "result": str(result.imag)})
    Status = {"status": 'as,mna,sn,s'}
    return jsonify(Status)