from flask import Blueprint, render_template, request, jsonify
from portal.handlers.differentiation_handler import calculate_differentiation

# diff_bp = Blueprint('diff_bp', __name__)
diff_bp = Blueprint('diff_bp', __name__, url_prefix='/uncg_math',
                    template_folder="./templates", static_folder="./static")


@diff_bp.route('/differentiation', methods=["GET", "POST"])
def differentiation():
    if request.method == "GET":
        return render_template("differentiation.html")
    if request.method == "POST":
        data = request.json
        result = calculate_differentiation(data)

        return jsonify({'result':result})


