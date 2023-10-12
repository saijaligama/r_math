from flask import Blueprint, request, jsonify

check_answers_bp = Blueprint('check_answers_bp', __name__, url_prefix='/uncg_math', template_folder="./templates", static_folder="./static")

@check_answers_bp.route('/check_answers', methods=["GET", "POST"])
def checkintdecfracanswers():
    data = request.get_json()
    results = {}
    for question, values in data.items():
        if values['Answer'] == values['Submission']:
            results[question] = 'RIGHT'
        else:
            results[question] = 'WRONG'
    return jsonify(results)