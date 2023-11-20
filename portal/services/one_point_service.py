from flask import Blueprint, render_template, request, jsonify
from portal.handlers.one_point_handler import analyze_point
one_point_bp = Blueprint('one_point_bp', __name__, url_prefix='/uncg_math',
                        template_folder="./templates", static_folder="./static")


@one_point_bp.route('/one_point', methods=["GET", "POST"])
def onepoint():
    if request.method == "GET":
        return render_template("one_point.html")
    else:
        data = request.json
        result = analyze_point(data['pointa'])
        return jsonify(result)
