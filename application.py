import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
application.config['SQLALCHEMY_MODIFICATIONS'] = False
application.secret_key = os.environ.get('SECRET_KEY', '123')
api = Api(application)

# bcrypt = Bcrypt(application)

@application.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(application, authenticate, identity)

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(application)
    application.run()