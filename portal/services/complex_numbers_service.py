from flask import request, Blueprint, render_template
from portal.handlers.complex_numbers_handler import complex_numbers_calc
complex_numbers_bp = Blueprint('complex_numbers_bp', __name__, url_prefix='/uncg_math',
                        template_folder="./templates", static_folder="./static")


@complex_numbers_bp.route('/complexnumbers', methods=["GET", "POST"])
def complexnumbers():
    if request.method == "GET":
        return render_template("complex_numbers.html")
    if request.method == "POST":
        data = request.json
        result = complex_numbers_calc(data)
        return result

