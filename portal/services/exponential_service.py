from flask import Blueprint, render_template, request, jsonify
from portal.handlers.exponential_handler import exponential_expression_calculator
exponential_bp = Blueprint('exponential_bp', __name__, url_prefix='/uncg_math',
                        template_folder="./templates", static_folder="./static")


@exponential_bp.route('/exponentials', methods = ['GET','POST'])
def exponential():
    if request.method == 'GET':
        return render_template("exponentials.html")
    else:
        data = request.json
        result = exponential_expression_calculator(data['eqn'],data['radioValue'])
        # if data['radioValue'] == 'integer':

        return jsonify({'result': result})