from Logic.CRUD import add
from Tests.test_ALL import run_all_tests
from UI.console import run_console


def main():
    lista=[]
    undol=[]
    redol=[]
    lista=add('1', 'Carmen', 'economy', 1230, 'da',lista,undol,redol)
    lista=add('2', 'Marius', 'economy plus', 250, 'nu',lista,undol,redol)
    lista=add('3', 'Marius', 'economy', 250, 'nu',lista,undol,redol)
    lista=add('4', 'Claudiu', 'business', 1023, 'da',lista,undol,redol)


    run_console(lista,undol,redol)

run_all_tests()
main()