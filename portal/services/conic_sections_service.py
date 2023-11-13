from flask import Blueprint, render_template, request, jsonify
from portal.handlers.conic_sections_handler import ellipse_parameters
conic_sections_bp = Blueprint('conic_sections_bp', __name__, url_prefix='/uncg_math',
                        template_folder="./templates", static_folder="./static")


@conic_sections_bp.route('/conic_section', methods=["GET", "POST"])
def conic_section():
    if request.method == "GET":
        return render_template("conic_section.html")
    else:
        data = request.json
        result = ellipse_parameters(data['eqn'])
        print(result)
        return jsonify(result)