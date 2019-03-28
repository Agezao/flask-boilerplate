from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

class IndexResource(Resource):
  
  @staticmethod
  def get():
    return jsonify({'hello': 'world'})