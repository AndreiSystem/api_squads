class Framework:
    def __init__(self, framework, id=None):
        self.__framework = framework
        self.__id = id

    @property
    def framework(self):
        return self.__framework

    @property
    def id(self):
        return self.__id
