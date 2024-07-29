from flask_restful import Api
from .user import HealthCheck, UserRegistration, UserLogin, FetchUserProfile


def register_endpoint(app: Api):
    app.add_resource(HealthCheck, "/health-check")
    app.add_resource(UserRegistration, "/register")
    app.add_resource(UserLogin, "/login")
    app.add_resource(FetchUserProfile, "/my-profile")
