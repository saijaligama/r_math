from flask import Blueprint, render_template, request, jsonify
from portal.handlers.differentiation_handler import calculate_differentiation

# diff_bp = Blueprint('diff_bp', __name__)
int_bp = Blueprint('int_bp', __name__, url_prefix='/uncg_math',
                    template_folder="./templates", static_folder="./static")


@int_bp.route('/integration', methods=["GET", "POST"])
def integration():
    if request.method == "GET":
        return render_template("integration.html")