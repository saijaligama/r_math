from flask import Blueprint, render_template, request, jsonify
from portal.handlers.logarithm_handler import  calculate_log_from_expression,simplify_logarithmic_expression
logarithm_bp = Blueprint('logarithm_bp', __name__, url_prefix='/uncg_math',
                        template_folder="./templates", static_folder="./static")

@logarithm_bp.route('/logarithms', methods = ['GET','POST'])
def logarithm():
    if request.method == 'GET':
        return render_template("logarithms.html")
    else:
        data = request.json
        # result = simplify_logarithmic_expression(data['eqn'],data['radioValue'])
        result = calculate_log_from_expression(data['eqn'],data['radioValue'])
        return jsonify({'result': result})