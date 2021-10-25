from Domain.undoredo_operation import UndoRedoOperation

class AddOperation(UndoRedoOperation):

    def __init__(self, repository, added_object):
        super().__init__(repository)
        self.__added_object = added_object

    def undo(self):
        self._repository.delete(self.__added_object.id_entity)

    def redo(self):
        self._repository.create(self.__added_object)