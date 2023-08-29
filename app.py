from portal import create_app

from portal.services import differentiation_service
from portal.services import calculus_service
from portal.services import home_service
from portal.services import algebra_service

app = create_app()

app.register_blueprint(differentiation_service.diff_bp)
app.register_blueprint(calculus_service.calculus_bp)
app.register_blueprint(home_service.home_bp)
app.register_blueprint(algebra_service.algebra_bp)

if __name__ == "__main__":
    app.run(port=8003)