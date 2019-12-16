from flask_restful import Resource
from flask import request
from model.programador import Programador
#from dao.algo_dao import AlgoDao


class ProgramadoresController(Resource):
    def __init__(self):
        self.dao = 'AlgoDao()'

    def get(self, id=None):
        pass

    def post(self):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass
