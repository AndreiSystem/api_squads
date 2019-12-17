class Db:
    def __init__(self, db, id=None):
        self.__db = db
        self.__id = id

    @property
    def db(self):
        return self.__db

    @property
    def id(self):
        return self.__id
