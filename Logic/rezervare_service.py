from copy import deepcopy

from Domain.add_operation import AddOperation
from Domain.rezervare import Rezervare
from Domain.delete_operation import DeleteOperation
from Domain.update_operation import UpdateOperation
from Repository.file_repository import FileRepository
from Logic.undoredo_service import UndoRedoService


class RezervareService:
    def __init__(self, rezervare_repository: FileRepository, undo_redo_service:UndoRedoService): #, card_client_validator:CardClientValidator
        self.__rezervare_repository = rezervare_repository
        self.__undo_redo_service = undo_redo_service

    def find_by_cnp(self,cnp):
        copie = self.get_all()
        for card_client in copie:
            if card_client.cnp == cnp:
                return card_client
        return  None

    def create(self, id_rezervare, nume,clasa,pret,checkin):
        '''
        se creaza o rezervare
        :param id_rezervare: unic
        :param nume: cir de caractere,doar litere
        :param clasa:
        :param pret:
        :param checkin:
        :return:
        '''


        rezervare = Rezervare(id_rezervare, nume,clasa,pret,checkin,)

        self.__rezervare_repository.create(rezervare)
        self.__undo_redo_service.add_to_undo(AddOperation(self.__rezervare_repository, rezervare))
        self.__undo_redo_service.clear_redo()

    def delete(self, id_rezervare):
        '''
        Sterge o rezervare dupa un id dat
        :param id_rezervare:
        :return:
        '''
        rezervare = self.__rezervare_repository.find_by_id(id_rezervare)
        self.__undo_redo_service.add_to_undo(DeleteOperation(self.__rezervare_repository,rezervare))

        self.__rezervare_repository.delete(id_rezervare)
        self.__undo_redo_service.clear_redo()

    def update(self, id_rezervare, nume, clasa, pret, checkin):
        '''
        Schimba datele unui rezervare dat prin id
        '''
        rezervare = self.__rezervare_repository.find_by_id(id_rezervare)
        if rezervare is None:
            raise KeyError(f'Cardul_client cu id-ul {id_rezervare} nu exista!')
        else:
            rezervare_vechi=deepcopy(rezervare)

        if nume != '':
            rezervare.nume = nume
        if clasa != '':
            rezervare.clasa = clasa
        if pret != '':
            rezervare.pret= int(pret)
        if checkin != '':
            rezervare.checkin = checkin

        self.__rezervare_repository.update(rezervare)

        if nume!='' or clasa!='' or pret != '' or checkin != '':
            self.__undo_redo_service.add_to_undo(UpdateOperation(self.__rezervare_repository,rezervare_vechi,rezervare))
            self.__undo_redo_service.clear_redo()

    def get_all(self):
        return self.__rezervare_repository.get_all()