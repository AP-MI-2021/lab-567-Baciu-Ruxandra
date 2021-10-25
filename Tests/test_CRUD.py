from Logic.rezervare_service import RezervareService
from Logic.undoredo_service import UndoRedoService
from Repository.file_repository import FileRepository
from Tests.utils import clear_file


def test_crud_rezervare():
    filename = 'test_rez.txt'
    clear_file(filename)
    repository = FileRepository('test_rez.txt')
    undo_redo_service = UndoRedoService()
    service=RezervareService(repository,undo_redo_service)
    service.create('1', 'Carmen', 'economy', 123, 'da')
    assert len(service.get_all())==1
    service.create('2', 'Carmen', 'economy plus', 123, 'da')
    assert len(service.get_all()) == 2
    added = repository.find_by_id('2')
    assert added is not None
    assert added.pret==123


    service.delete('1')
    assert len(service.get_all()) == 1

    service.update('2','','','','nu')
    updated = repository.find_by_id('2')
    assert updated.checkin=='nu'