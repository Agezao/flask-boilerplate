from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

from contexts import mysql

class UsersResource(Resource):
  
  @staticmethod
  def get():
    cur = mysql.run("select id, name from Candidates")
    return jsonify({'total': cur.rowcount})