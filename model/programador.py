from model.framework import Framework
from model.db import Db
from model.linguagem_squad import Linguagem


class Programador:
    def __init__(self, nome, framework: Framework = None, db: Db = None, linguagem: Linguagem = None,
                 id_db=None, id_framework=None, id_linguagem=None, id=None):
        self.__nome = nome
        self.__linguagem = linguagem
        self.__framework = framework
        self.__db = db
        self.__id_db = id_db
        self.__id_framework = id_framework
        self.__id_linguagem = id_linguagem
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @property
    def linguagem(self):
        return self.__linguagem

    @property
    def framework(self):
        return self.__framework

    @property
    def db(self):
        return self.__db

    @property
    def id_db(self):
        return self.__id_db

    @property
    def id_framework(self):
        return self.__id_framework

    @property
    def id_linguagem(self):
        return self.__id_linguagem

    @property
    def id(self):
        return self.__id
