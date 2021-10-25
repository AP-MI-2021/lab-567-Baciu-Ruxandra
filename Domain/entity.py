class Entity:
    def __init__(self,id_entity):
        self.__id_entity = id_entity

    @property
    def id_entity(self):
        return self.__id_entity

    def __eq__(self, other):
        return type(self) == type(other) and self.id_entity == other.id_entity