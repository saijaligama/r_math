from flask import Blueprint, render_template, request, jsonify

calculus_bp = Blueprint('calculus_bp', __name__, url_prefix='/uncg_math',
                        template_folder="./templates", static_folder="./static")


@calculus_bp.route('/calculus', methods=["GET", "POST"])
def calculus():
    if request.method == "GET":
        return render_template("calculus.html")
