from flask import Blueprint, render_template, request, jsonify


home_bp = Blueprint('home_bp', __name__, url_prefix='/uncg_math',
                    template_folder="./templates", static_folder="./static")


@home_bp.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")