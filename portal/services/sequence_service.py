from flask import Blueprint, render_template, request, jsonify
from portal.application.sequence import sequence_type, generat_arithmetic_sequence, generat_geometric_sequence

sequence_bp = Blueprint('sequence_bp', __name__, url_prefix='/uncg_math',
                    template_folder="./templates", static_folder="./static")

@sequence_bp.route('/sequences', methods=["GET", "POST"])
def sequences():
    if request.method == "GET":
        return render_template("sequences.html")
    if request.method == "POST":
        data = request.json
        type = data["type"]
        if type == 'a_or_g_output':
            arith_or_geo = data["arith_or_geo_input"]
            a_n_term = data["a_n_term"]
            finl_out = sequence_type(arith_or_geo, a_n_term, a_n_term)
            print(finl_out)
            return finl_out
        elif type == 'Arithmetic Sequence':
            print('Geometric', data)
            print("hi")
            final_output_ = generat_arithmetic_sequence(data)
            print('final_output_', final_output_)
            return final_output_
        elif type == 'Geometric Sequence':
            final_output_ = generat_geometric_sequence(data)
            return final_output_
        Status = {"status": 'as,mna,sn,s'}
        return jsonify(Status)