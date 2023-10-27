from flask import Blueprint, render_template, request, jsonify
from portal.handlers.linear_graphing_handler import calculate_line_properties

linear_graphing_bp = Blueprint('linear_graphing_bp', __name__, url_prefix='/uncg_math',
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

@linear_graphing_bp.route('/linear_graphing', methods=["GET", "POST"])
def linear_graphing():
    if request.method == "GET":
        return render_template("linear_graphing.html")
    elif request.method == "POST":
        data = request.json
        print(data)
        result = calculate_line_properties(data)
        print(result)
        # result = trigonometric_object.trig_fractions(data['exp'])  # Provide the 'exp' argument
        return jsonify(result)