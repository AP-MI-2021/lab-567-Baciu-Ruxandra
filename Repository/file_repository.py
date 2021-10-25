import jsonpickle
from copy import deepcopy


class FileRepository:

    def __init__(self, filename):
        self.__storage = {}
        self.__filename = filename

    def __write_file(self):
        with open(self.__filename, 'w') as f:
            f.write(jsonpickle.encode(self.__storage))

    def __load_file(self):
        try:
            with open(self.__filename, 'r') as f:
                self.__storage = jsonpickle.decode(f.read())
        except:
            self.__storage = {}

    def find_by_id(self, id_entity):
        self.__load_file()
        if id_entity in self.__storage:
            return deepcopy(self.__storage[id_entity])
        return None

    def operatie2(self,entity):
        self.__storage[entity.id_entity]= entity
        return deepcopy(self.__storage[entity.id_entity])



    def create(self, entity):
        '''
        Adauga o rezervare si verifica daca id-ulintrodus nu exista deja
        :param entity:
        :return:
        '''

        if self.find_by_id(entity.id_entity) is not None:
            raise KeyError(f'Exista deja o entitate cu id-ul {entity.id_entity}!')
        self.__storage[entity.id_entity] = entity
        self.__write_file()

    def update(self, entity):
        '''
        Schimba datele unei rezervari dupa un id dat si verifica daca acesta exista
        :param entity:
        :return:
        '''
        if self.find_by_id(entity.id_entity) is None:
            raise KeyError(f'Nu exista nicio entitate cu id-ul {entity.id_entity}')
        self.__storage[entity.id_entity] = entity
        self.__write_file()

    def delete(self, id_entity):
        '''
        sterge o rezervare dupa un id di se verifica existenta acestuia

        :param id_entity:
        :return:
        '''
        if self.find_by_id(id_entity) is None:
            raise KeyError(f'Nu exista nicio entitate cu id-ul {id_entity}')
        del self.__storage[id_entity]
        self.__write_file()

    def get_all(self):
        self.__load_file()
        return list(self.__storage.values())

