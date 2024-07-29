import bcrypt
import datetime
from utils.status import *
from functools import wraps
from flask_jwt_extended import create_access_token, decode_token
from jwt import ExpiredSignatureError, InvalidTokenError
from flask import request
import logging

def get_hashed_password(password):
    """Hash password using bcrypt"""
    pwhash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    return pwhash.decode('utf8')


def check_password(plain_text_password, hashed_password):
    """Check hashed password. Password should be already hashed"""
    # encoding password with utf-8
    password_bytes = plain_text_password.encode('utf-8')
    # enoding hashed password with utf-8 as it is stored as string in the db
    hashed_password_bytes = hashed_password.encode('utf-8')
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)


def get_jwt_token(user_email):
    """Generate JWT token for user"""
    return create_access_token(identity=user_email)  #, expires_delta=datetime.timedelta(hours=1)


def validate_token(func):
    """Validate JWT token"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        access_token = request.headers.get("Authorization").split(" ")[1]
        try:
            decoded_token = decode_token(access_token)
            kwargs["email"] = decoded_token["sub"]
            return func(*args, **kwargs)
        except ExpiredSignatureError as e:
            return {"message": "Invalid token, Signature expred", "data": None}, HTTP_401_UNAUTHORIZED
        except InvalidTokenError as e:
            return {"message": "Invalid token", "data": None}, HTTP_401_UNAUTHORIZED
        except Exception as e:
            logging.error(e)
            return {"message": INTERNAL_SERVER_ERROR, "data": None}, HTTP_500_INTERNAL_SERVER_ERROR
    return wrapper
