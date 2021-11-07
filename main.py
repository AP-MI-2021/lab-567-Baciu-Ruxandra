from Logic.CRUD import add
from Tests.test_ALL import run_all_tests
from UI.console import run_console


def main():
    lista=[]

    lista=add('1', 'Carmen', 'economy', 1230, 'da',lista)
    lista=add('2', 'Marius', 'economy plus', 250, 'nu',lista)
    lista=add('3', 'Claudiu', 'business', 1023, 'da',lista)

    run_console(lista)

run_all_tests()
main()