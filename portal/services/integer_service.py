from flask import Blueprint, render_template, request, jsonify
import random
from portal.handlers.integer_handler import IntegerClass

integer_bp = Blueprint('integer_bp', __name__, url_prefix='/uncg_math', template_folder="./templates", static_folder="./static")


@integer_bp.route('/integer', methods=["GET", "POST"])
def integer():
    if request.method == "GET":
        return render_template("integer.html")
    if request.method == "POST":
        data = request.json
        integer_object = IntegerClass()
        result = integer_object.integerRandomTests(data)
        return jsonify(result)


