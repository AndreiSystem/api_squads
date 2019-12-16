from flask_restful import Resource
from flask import request
from model.programador import Programador
from dao.programadores_dao import ProgramadorDao


class ProgramadoresController(Resource):
    def __init__(self):
        self.dao = ProgramadorDao()

    def get(self, id=None):
        if id:
            return self.dao.buscar_por_id(id)
        return self.dao.listar()

    def post(self):
        nome = request.json['nome']
        id_db = request.json['id_db']
        id_framework = request.json['id_framework']
        id_linguagem = request.json['id_linguagem']
        programador = Programador(
            nome, id_framework=id_framework, id_db=id_db, id_linguagem=id_linguagem)
        programador_id = self.dao.inserir(programador)
        programador = self.dao.buscar_por_id(programador_id)
        return programador

    def put(self, id):
        id_body = request.json['id']
        nome = request.json['nome']
        id_db = request.json['id_db']
        id_framework = request.json['id_framework']
        id_linguagem = request.json['id_linguagem']

        if id_body != id:
            return 'Ids de rota e body diferentes, seu tatu'
        programador = Programador(
            nome, id_db=id_db, id_framework=id_framework, id_linguagem=id_linguagem, id=id)
        self.dao.alterar(programador)
        programador = self.dao.buscar_por_id(id)
        return programador

    def delete(self, id):
        self.dao.deletar(id)
        return 'deletado meu'
