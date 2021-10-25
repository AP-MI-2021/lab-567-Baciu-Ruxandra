from Domain.rezervare import Rezervare
from Repository.file_repository import FileRepository
from Tests.utils import clear_file


def test_file_repository():

    filename = 'test_masini.txt'
    clear_file(filename)

    repository = FileRepository(filename)
    r1 = Rezervare('1', 'Carmen', 'economy', 123, True)
    repository.create(r1)

    all = repository.get_all()
    assert all[-1] == r1

    r2=Rezervare('2', 'Carmen', 'economy plus', 333, False)
    repository.create(r2)

    all = repository.get_all()
    assert all[-1] == r2

    repository.delete('1')

    all = repository.get_all()
    assert all[-1] == r2


