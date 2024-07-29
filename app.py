from flask import Flask
from flask_restful import Api
from routes import register_endpoint
from flask_jwt_extended import JWTManager
import os
import logging
from logging.config import dictConfig
import datetime

app = Flask(__name__)

log = logging.getLogger('file')
# Set root logger to log DEBUG and above
log.setLevel(logging.DEBUG)
# Add Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "auth-secret")
# setting access token expire time
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=1)
jwt = JWTManager(app)
api = Api(app)
register_endpoint(api)

if __name__ == "__main__":
    app.run(port=os.environ.get("PORT_NUMBER", 5000), debug=True)


# logger config
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] {%(filename)s:%(lineno)d} %(threadName)s %(levelname)s in %(module)s\
        (PID:%(process)d): %(message)s',
    }},
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
        }
    },
    'loggers': {
        'file': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': ''
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    }
})