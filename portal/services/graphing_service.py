from flask import Blueprint, render_template, request, jsonify
from portal.handlers.graphing_handler import analyze_graph
graphing_bp = Blueprint('graphing_bp', __name__, url_prefix='/uncg_math',
                        template_folder="./templates", static_folder="./static")


@graphing_bp.route('/graphing', methods=["GET", "POST"])
def graphing():
    if request.method == "GET":
        return render_template("graphing.html")
    else:
        data = request.json
        result = analyze_graph(data)
        print(result)
        return jsonify({'result':result})
