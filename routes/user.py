from flask_restful import Resource
from flask import request
from validator import RegistrationPayload, LoginPayload
from controller.user_controller import UserController, validate_token
from utils.status import *
import logging
usr_controller = UserController()


class HealthCheck(Resource):

    def get(self):
        return "OK, user auth system is up", HTTP_200_OK


class UserRegistration(Resource):

    def post(self):
        try:
            payload = RegistrationPayload(**request.get_json()).dict()
            msg, status_code = usr_controller.register_user(payload)
            return {"message": msg, "data": None}, status_code
        except ValueError as e:
            logging.error(e)
            return {"message": str(e), "data": None}, HTTP_400_BAD_REQUEST
        except Exception as e:
            logging.error(e)
            return {"message": INTERNAL_SERVER_ERROR, "data": None}, HTTP_500_INTERNAL_SERVER_ERROR


class UserLogin(Resource):

    def post(self):
        try:
            payload = LoginPayload(**request.get_json()).dict()
            data, status_code = usr_controller.login_user(payload)
            if status_code == HTTP_200_OK:
                return {"message": SUCCESS_MSG, "access_token": data}, status_code
            return {"message": data, "data": None}, status_code
        except ValueError as e:
            logging.error(e)
            return {"message": str(e), "data": None}, HTTP_400_BAD_REQUEST
        except Exception as e:
            logging.error(e)
            return {"message": INTERNAL_SERVER_ERROR, "data": None}, HTTP_500_INTERNAL_SERVER_ERROR


class FetchUserProfile(Resource):
    @validate_token
    def get(self, *args, **kwargs):
        try:
            data, status_code = usr_controller.fetch_user_profile(kwargs["email"])
            if status_code == HTTP_200_OK:
                return {"message": SUCCESS_MSG, "data": data},status_code
            return {"message": data, "data": None}, status_code
        except Exception as e:
            logging.error(e)
        return {"message": INTERNAL_SERVER_ERROR, "data": None}, HTTP_500_INTERNAL_SERVER_ERROR







