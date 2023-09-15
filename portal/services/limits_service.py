from flask import Blueprint, render_template, request, jsonify
from portal.handlers.limits_handler import LimitCalculator

limits_bp = Blueprint('limits_bp', __name__, url_prefix='/uncg_math',
                      template_folder="./templates", static_folder="./static")


@limits_bp.route('/limits', methods=["GET", "POST"])
def limits():
    if request.method == 'POST':
        data = request.json
        inp = data['eqn'].split(',')
        limit_object = LimitCalculator()
        result = limit_object.calculate_limit(inp)
        return jsonify({'result': result})
