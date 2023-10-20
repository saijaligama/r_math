from flask import Blueprint, render_template, request, jsonify
from portal.handlers.trigonometry_handler import TrigonometricCalculator

trigonometry_bp = Blueprint('trigonometry_bp', __name__, url_prefix='/uncg_math',
                            template_folder="./templates", static_folder="./static")


# @trigonometry_bp.route('/trigonometry', methods=["GET", "POST"])
# def trigonometry():
#     if request.method == "GET":
#         return render_template("trigonometry.html")
#     elif request.method == "POST":
#         data = request.json
#         trigonometric_object = TrigonometricCalculator(unit= data['unit'])
#         result = trigonometric_object.calculate_trig_expression(data['exp'])
#         return jsonify({'result':result})

@trigonometry_bp.route('/trigonometry', methods=["GET", "POST"])
def trigonometry():
    if request.method == "GET":
        return render_template("trigonometry.html")
    elif request.method == "POST":
        data = request.json
        trigonometric_object = TrigonometricCalculator(unit=data['unit'])
        result = trigonometric_object.trig_fractions(data['exp'])  # Provide the 'exp' argument
        return jsonify({'result': result})
