





#from Domain.rezervare_validator import RezervareValidator
from Logic.options_service import OptionsService
from Logic.undoredo_service import UndoRedoService
from Tests.test_ALL import run_all_tests
from Logic.rezervare_service import RezervareService
from Repository.file_repository import FileRepository
from UI.console import Console



def main():
    rezervare_repository = FileRepository('rezervari.txt')
    operatiuni_repository = FileRepository ('operatii.txt')
    undo_redo_service = UndoRedoService()

    rezervare_service = RezervareService(rezervare_repository,undo_redo_service)
    options_service = OptionsService(rezervare_repository,operatiuni_repository,undo_redo_service)


    rezervare_service.create('1', 'Carmen', 'economy', 123, 'da')
    rezervare_service.create('2', 'Marius', 'economy plus', 250, 'nu')
    rezervare_service.create('3', 'Claudiu', 'business', 1023, 'da')

    user_interface = Console(rezervare_service,options_service,undo_redo_service)
    user_interface.run_console()

run_all_tests()
main()