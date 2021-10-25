from Domain.undoredo_operation import UndoRedoOperation


class UpdateOperation(UndoRedoOperation):
    def __init__(self, repository, to_update_object, update_object):
        super().__init__(repository)
        self.__to_update_object = to_update_object
        self.__update_object = update_object

    def undo(self):
        self._repository.update(self.__to_update_object)

    def redo(self):
        self._repository.update(self.__update_object)