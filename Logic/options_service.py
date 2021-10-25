from copy import deepcopy

from Domain.rezervare import Rezervare
from Domain.update_operation import UpdateOperation
from Logic import rezervare_service
from Repository.file_repository import FileRepository
from Logic.undoredo_service import UndoRedoService

class OptionsService:

    def __init__(self,
                 rezervare_repository: FileRepository,
                 operatiuni_repository: FileRepository,
                 undo_redo_service:UndoRedoService):

        self.__rezervare_repository = rezervare_repository
        self.__operatiuni_repository = operatiuni_repository
        self.__undo_redo_service = undo_redo_service


    def upgrade_clasa(self,rezervare,nume):
        '''
        se cauta schimba clasa
        :param rezervare:
        :param nume:
        :return:
        '''
        lst=[rezervare.id_entity,rezervare.nume,rezervare.clasa,rezervare.pret,rezervare.checkin]

        if str(lst[1]).find(nume) != -1:
            if str(lst[2]).find('economy plus') != -1:
                rezervare_new = Rezervare(lst[0], lst[1], 'business', lst[3], lst[4])
                self.__undo_redo_service.add_to_undo(
                    UpdateOperation(self.__rezervare_repository, rezervare, rezervare_new))
                self.__undo_redo_service.clear_redo()

                rezervare = deepcopy(rezervare_new)
                self.__rezervare_repository.update(rezervare)
                return self.__rezervare_repository.operatie2(rezervare)

            elif str(lst[2]).find('economy') != -1:
                rezervare_new=Rezervare(lst[0],lst[1],'economy plus',lst[3],lst[4])

                self.__undo_redo_service.add_to_undo(
                    UpdateOperation(self.__rezervare_repository, rezervare, rezervare_new))
                self.__undo_redo_service.clear_redo()

                rezervare=deepcopy(rezervare_new)
                self.__rezervare_repository.update(rezervare)
                return self.__rezervare_repository.operatie2(rezervare)


        return None