from Domain.rezervare import toString
from Logic.CRUD import add, delete, update
from Logic.options_service import upgrade_clasa, suma_pret_per_nume, ordonare_descrescator_dupa_pret, \
    pret_max_per_clasa, aplicare_reducere
from Logic.undoredo_service import UndoRedoService



def print_menu():
    print('1. CRUD Rezervare')
    print('2. Operatii')
    print('a. Show all rezervare.')
    print('u. Undo')
    print('r. Redo')
    print('x. Iesire')

def run_console(lista):

    while True:
        print_menu()
        option = input('Alegeti optiunea: ')
        if option == '1':
            run_crud_rezervare(lista)
        elif option == '2':
            run_options(lista)
        elif option == 'a':
            handle_show_all_rezervare(lista)
        elif option == 'u':
            pass
        elif option == 'r':
            pass
        elif option == 'x':
            break
        else:
            print('Comanda invalida!')


def run_crud_rezervare(lista):
    while True:
        print('1. Create rezervare.')
        print('2. Delete rezervare.')
        print('3. Update rezervare.')
        print('a. Show all rezervare.')
        print('b. Back')
        option = input('Alegeti optiunea: ')
        if option == '1':
            handle_create_rezervare(lista)
        elif option == '2':
            handle_delete_rezervare(lista)
        elif option == '3':
            handle_update_rezervare(lista)
        elif option == 'a':
            handle_show_all_rezervare(lista)
        elif option == 'b':
            break
        else:
            print('Optiune invalida.')

def handle_create_rezervare(lista):
        id_rezervare = input('ID-ul rezervarii: ')
        nume = input('Numele pe care a fost facuta rezervarea: ')
        clasa = input('Clasa: ')
        pret = float(input('Pretul rezervarii: '))
        checkin = input('A fost facut checkin-ul? (da/nu): ')

        return add(id_rezervare, nume, clasa, pret, checkin,lista)


def handle_show_all_rezervare(lista):
    for rezervare in lista:
        print(toString(rezervare))

def handle_delete_rezervare(lista):
    id_rezervare = input('ID-ul rezervarii pe care doriti sa o stergeti: ')
    return delete(id_rezervare,lista)


def handle_update_rezervare(lista):

    id_rezervare = input('ID-ul rezervarii pe care doriti sa o modificati: ')
    nume = input('Numele pe care a fost facuta rezervarea:(lasati gol daca nu doriti sa il schimbati) ')
    clasa = input('Clasa:(lasati gol daca nu doriti sa il schimbati) ')
    pret = input('Pretul rezervarii:(introduceti -1 daca nu doriti sa il schimbati) ')
    checkin = input('A fost facut checkin-ul? (da/nu):(lasati gol daca nu doriti sa il schimbati) ')

    return update(id_rezervare, nume, clasa, pret, checkin,lista)


def run_options(lista):
    while True:
        print('1. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.')
        print('2. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.')
        print('3. Determinarea prețului maxim pentru fiecare clasă.')
        print('4. Ordonarea rezervărilor descrescător după preț.')
        print('5. Afișarea sumelor prețurilor pentru fiecare nume.')
        print('b. Back')
        option = input('Alegeti optiunea: ')
        if option == '1':
            nume = input("Introduceti numele persoanei careia doriti sa ii upgradati clasa: ")
            handle_clasa_sup(lista,nume)
        elif option == '2':
            procent=int(input("Introduceti procentul cu care doriti sa se reduca rezervarile: "))
            handle_ieftinire(lista,procent)
        elif option == '3':
            handle_pret_max_per_clasa(lista)
        elif option == '4':
            handle_ordonare_descresc_rezervari(lista)
        elif option == '5':
            handle_sume_pret_per_nume(lista)
        elif option == 'b':
            break
        else:
            print('Optiune invalida.')


def handle_clasa_sup(lista,nume):
    ok = 0
    print('Schimbari:\n')
    for rezervare in lista:
        rezultat=upgrade_clasa(rezervare,nume)
        if rezultat is not None:
            ok = +1
            print(rezultat)
    if ok == 0:
        print("Nu s-au putut face schimbari!")


def handle_ieftinire(lista,procent):
    handle_create_rezervare(aplicare_reducere(lista,procent))


def handle_pret_max_per_clasa(lista):
    rezultat = pret_max_per_clasa(lista)
    for an in rezultat:
        print("Anul {} are caloriile maxime {}".format(an, rezultat[an]))

def handle_ordonare_descresc_rezervari(lista):
    handle_create_rezervare(ordonare_descrescator_dupa_pret(lista))

def handle_sume_pret_per_nume(lista):
    rezultat = suma_pret_per_nume(lista)
    for nume in rezultat:
        print("pe numele {}  sunt rezervari care in total au suma de {}".format(nume, rezultat[nume]))


