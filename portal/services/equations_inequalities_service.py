from flask import Blueprint, jsonify, render_template, request
from portal.application.equations_inequalities import evaluate_expression, find_variables, calculate_logarithm, \
    quad_equation_solution

equations_inequalities_bp = Blueprint('equations_inequalities_bp', __name__,
                                      url_prefix='/uncg_math',
                                      template_folder="./templates",
                                      static_folder="./static")


@equations_inequalities_bp.route('/equationsandinequalities', methods=["GET", "POST"])
def equationsandinequalities():
    if request.method == "GET":
        return render_template("equations_and_inequalities.html")
    if request.method == "POST":
        message = 'na.'
        result = 'na.'
        data = request.json
        type_ = data["type"]
        print("From views:,", data)
        if type_ == 'get_equations':

            Equation = data["Equations"]
            Equation = Equation.split(',')
            print(Equation)
            Equations = Equation[0]
            Value_1 = Equation[1]
            Value_2 = Equation[2]
            try:
                Value_3 = Equation[3]
                print('Value_3', Value_3)
            except:
                Value_3 = 'z=0'
                pass

            print('Equations', Equations)
            print('Value_1', Value_1)
            print('Value_2', Value_2)

            result, message = evaluate_expression(Equations, x=str(Value_1), y=str(Value_2), z=str(Value_3))
            return jsonify({"message": message, "result": str(result)})

        elif type_ == '2nd_type_equations':

            Equation = data["Equations1"]
            Equation = Equation.split(',')
            print(Equation)
            Equations1 = Equation[0]
            Equations2 = Equation[1]
            Value_1 = Equation[2]
            Value_2 = Equation[3]

            # Equations1 = data["Equations1"]
            # Equations2 = data["Equations2"]
            # Value_1 = data["Value_1"]
            # Value_2 = data["Value_2"]
            result, message = find_variables(Equations1, Equations2, Value_1, Value_2)
            return jsonify({"message": message, "result": str(result)})

        elif type_ == 'Logarithm and Exponential':
            Equations1 = data["Equations"]
            result, message = calculate_logarithm(Equations1)
            return jsonify({"message": message, "result": str(result)})

        elif type_ == 'quad_equations':
            Equations1 = data["Equations1"]
            print("From init", Equations1)
            result, message = quad_equation_solution(Equations1)
            print("From result", result)
            return jsonify({"message": message, "result": str(result[0]), "result2": str(result[1])})

        return jsonify({"message": message, "result": str(result)})