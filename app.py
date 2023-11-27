from portal import create_app

from portal.services import differentiation_service
from portal.services import calculus_service
from portal.services import home_service
from portal.services import algebra_service
from portal.services import sequence_service
from portal.services import matrix_operation_service
from portal.services import matrix_matlab_service
from portal.services import complex_numbers_service
from portal.services import equations_inequalities_service
from portal.services import integration_service
from portal.services import limits_service
from portal.services import trigonometry_service
from portal.services import integer_service
from portal.services import check_answers
from portal.services import graphing_service
from portal.services import linear_graphing_service
from portal.services import triangles_service
from portal.services import conic_sections_service
from portal.services import one_point_service
from portal.services import logarithm_service
from portal.services import exponential_service

app = create_app()

app.register_blueprint(differentiation_service.diff_bp)
app.register_blueprint(calculus_service.calculus_bp)
app.register_blueprint(home_service.home_bp)
app.register_blueprint(algebra_service.algebra_bp)
app.register_blueprint(sequence_service.sequence_bp)
app.register_blueprint(matrix_operation_service.matrix_operations_bp)
app.register_blueprint(matrix_matlab_service.matrix_matlab_bp)
app.register_blueprint(complex_numbers_service.complex_numbers_bp)
app.register_blueprint(equations_inequalities_service.equations_inequalities_bp)
app.register_blueprint(integration_service.int_bp)
app.register_blueprint(limits_service.limits_bp)
app.register_blueprint(trigonometry_service.trigonometry_bp)
app.register_blueprint(integer_service.integer_bp)
app.register_blueprint(check_answers.check_answers_bp)
app.register_blueprint(graphing_service.graphing_bp)
app.register_blueprint(linear_graphing_service.linear_graphing_bp)
app.register_blueprint(triangles_service.triangles_bp)
app.register_blueprint(conic_sections_service.conic_sections_bp)
app.register_blueprint(one_point_service.one_point_bp)
app.register_blueprint(logarithm_service.logarithm_bp)
app.register_blueprint(exponential_service.exponential_bp)

if __name__ == "__main__":
    app.run(port=8003)