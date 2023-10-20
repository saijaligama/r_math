from flask import Blueprint, render_template, request, jsonify
from portal.handlers.integration_handler import calculate_integration, calculate_indefinite

# diff_bp = Blueprint('diff_bp', __name__)
int_bp = Blueprint('int_bp', __name__, url_prefix='/uncg_math',
                    template_folder="./templates", static_folder="./static")


@int_bp.route('/integration', methods=["GET", "POST"])
def integration():
    if request.method == "GET":
        return render_template("integration.html")
    elif request.method == "POST":
        data = request.json
        print(data)
        inp = data['eqn'].split(',')
        if data['type'] == "Indefinite":
            result = calculate_indefinite(inp)
        else:
            result = calculate_integration(inp)
        #
        #
        # print(inp)
        # result = calculate_integration(inp)
        return jsonify({'result':result})

