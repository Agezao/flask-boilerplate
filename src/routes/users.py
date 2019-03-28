from flask import Blueprint
from flask_restful import Api

from resources import UsersResource

USERS_BLUEPRINT = Blueprint('users', __name__)
Api(USERS_BLUEPRINT).add_resource(UsersResource, 'users')