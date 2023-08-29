from flask import Blueprint, render_template, request, jsonify

algebra2_bp = Blueprint('algebra2_bp', __name__, url_prefix='/uncg_math',
                        template_folder="./templates", static_folder="./static")


@algebra2_bp.route('/algebra2', methods=["GET", "POST"])
def algebra2():
    if request.method == "GET":
        return render_template("calculus.html")