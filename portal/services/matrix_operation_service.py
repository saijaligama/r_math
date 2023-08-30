from flask import Blueprint, render_template, request, jsonify
import re
from portal.handlers.matrix_handler import get_final_out_1
from portal.application.matrix_operations import matrix_arithmetic, matrix_arithmetic_operations, get_matrix, \
    get_ones_zeros_eye, get_transpose_inv_det, get_Diagonal_Trace_Size, get_inverse
from portal.handlers.matrix_operations_handler import matrix_calc

matrix_operations_bp = Blueprint('matrix_operations_bp', __name__, url_prefix='/uncg_math',
                    template_folder="./templates", static_folder="./static")


@matrix_operations_bp.route('/matrix_operation', methods=["GET", "POST"])
def matrix_operation():
    if request.method == "GET":
        return render_template("matrix_operation.html")
    if request.method == "POST":
        data = request.json
        result = matrix_calc(data)
        return jsonify(result)
        