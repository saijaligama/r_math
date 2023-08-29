from flask import Blueprint, render_template, request, jsonify

algebra_bp = Blueprint('algebra_bp', __name__, url_prefix='/uncg_math',
                        template_folder="./templates", static_folder="./static")


@algebra_bp.route('/algebra', methods=["GET", "POST"])
def algebra():
    if request.method == "GET":
        return render_template("algebra.html")