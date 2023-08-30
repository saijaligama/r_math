from flask import Blueprint, render_template, request, jsonify
from portal.handlers.matrix_matlab_handler import matrix_matlab_calc

matrix_matlab_bp = Blueprint('matrix_matlab_bp', __name__, url_prefix='/uncg_math',
                        template_folder="./templates", static_folder="./static")


@matrix_matlab_bp.route('/matrix_matlab_operation', methods=["GET", "POST"])
def matrix_matlab_operation():
    if request.method == "POST":
        data = request.json
        result = matrix_matlab_calc(data)
        return jsonify(result)

