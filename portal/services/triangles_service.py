from flask import Blueprint, render_template, request, jsonify
from portal.handlers.triangles_handler import classify_triangle
triangles_bp = Blueprint('triangles_bp', __name__, url_prefix='/uncg_math',
                        template_folder="./templates", static_folder="./static")


@triangles_bp.route('/triangles', methods=["GET", "POST"])
def triangles():
    if request.method == "GET":
        return render_template("Triangles.html")
    else:
        data = request.json
        result = classify_triangle(data['pointa'],data['pointb'],data['pointc'])
        print(result)
        return jsonify(result)
