from copy import deepcopy

from Domain.rezervare import toString
from Logic.CRUD import add, delete, update
from Logic.options_service import upgrade_clasa, suma_pret_per_nume, ordonare_descrescator_dupa_pret, \
    pret_max_per_clasa, aplicare_reducere
from Logic.undo_redo import do_undo, do_redo


def print_menu():
    print('1. CRUD Rezervare')
    print('2. Operatii')
    #print('i. Interfata noua(add,delete,showall)')
    print('a. Show all rezervare.')
    print('u. Undo')
    print('r. Redo')
    print('x. Iesire')


# def command_line_console(lista):
#     # citim instructiunile asa: delete,7;add,mara,economic,1234,da;showall
#     arr=input('Introduceti instructiunile (add,delete,showall) pe care doriti sa le utilizati separate din prin ; iar elementele prin ,\n')
#     intructiuni_lst=arr.split(';')
#     print('Au fost introduse {} comenzi\n'.format(len(intructiuni_lst)))
#     com=0
#     for instructiune in intructiuni_lst:
#         com+=1
#         arr=instructiune.split(',')
#         if arr[0]=='add':
#             if len(arr)!=6:
#                 print("Comanda 'add' nu e valida! Trebuie sa contina numele instructiunii, id,nume,clasa,pret,checkin!")
#                 break
#             else:
#                 try:
#                     print("Rezultatul dupa comanda numarul {}\n".format(com))
#                     print(add(arr[1],arr[2],arr[3],float(arr[4]),arr[5],lista))
#                 except ValueError as ve:
#                     print("Eroare: {}".format(ve))
#
#         elif arr[0]=='delete':
#             if len(arr)!=2:
#                 print("Comanda 'delete' nu e valida! Trebuie sa contina numele instructiunii si id rezervarii pe care doriti sa o stergeti!\n")
#                 break
#             else:
#                 try:
#                     print("Rezultatul dupa comanda numarul {}\n".format(com))
#                     print(delete(arr[1],lista))
#                 except ValueError as ve:
#                     print("Eroare: {}".format(ve))
#
#
#         elif arr[0]=='showall':
#             if len(arr)!=1:
#                 print('Comanda showall trebuie sa dontina doar numele intructiunii!')
#                 break
#             else:
#                 print("Rezultatul dupa comanda numarul {}\n".format(com))
#                 for rezervare in lista:
#                     print(toString(rezervare))
#         else:
#             print("Comanda nu e valida!")
#             break
#     return


def handle_undo(lista,undol,redol):
    undo_result = do_undo(undol, redol,lista)
    if undo_result is not None:
        return undo_result
    return lista



def handle_redo(lista,undol,redol):
    redo_result = do_redo(undol, redol)
    if redo_result is not None:
        return redo_result
    return lista

def run_console(lista,undol,redol):

    while True:
        print_menu()
        option = input('Alegeti optiunea: ')
        if option == '1':
            lista=run_crud_rezervare(lista,undol,redol)
        elif option == '2':
            lista=run_options(lista,undol,redol)
        # elif option=='i':
        #     command_line_console(lista)
        elif option == 'a':
            handle_show_all_rezervare(lista)
        elif option == 'u':
            lista=deepcopy(handle_undo(lista,undol,redol))
        elif option == 'r':
            lista=deepcopy(handle_redo(lista,undol,redol))
        elif option == 'x':
            break
        else:
            print('Comanda invalida!')

    return lista


def menu2():
    print('1. Create rezervare.')
    print('2. Delete rezervare.')
    print('3. Update rezervare.')
    print('a. Show all rezervare.')
    print('b. Back')

def run_crud_rezervare(lista,undol,redol):
    while True:
        menu2()
        option = input('Alegeti optiunea: ')
        if option == '1':
            lista=handle_create_rezervare(lista,undol,redol)
        elif option == '2':
            lista=handle_delete_rezervare(lista,undol,redol)
        elif option == '3':
            lista=handle_update_rezervare(lista,undol,redol)
        elif option == 'a':
            handle_show_all_rezervare(lista)
        elif option == 'b':
            break
        else:
            print('Optiune invalida.')

    return lista

def handle_create_rezervare(lista,undol,redol):
    try:
        id_rezervare = input('ID-ul rezervarii: ')
        nume = input('Numele pe care a fost facuta rezervarea: ')
        clasa = input('Clasa: ')
        pret = float(input('Pretul rezervarii: '))
        checkin = input('A fost facut checkin-ul? (da/nu): ')

        return add(id_rezervare, nume, clasa, pret, checkin, lista,undol,redol)

    except ValueError as ve:
        print("Eroare: {}".format(ve))


def handle_show_all_rezervare(lista):
    for rezervare in lista:
        print(toString(rezervare))

def handle_delete_rezervare(lista,undol,redol):
    try:
        id_rezervare = input('ID-ul rezervarii pe care doriti sa o stergeti: ')
        return delete(id_rezervare,lista,undol,redol)
    except ValueError as ve:
        print("Eroare: {}".format(ve))


def handle_update_rezervare(lista,undol,redol):
    try:
        id_rezervare = input('ID-ul rezervarii pe care doriti sa o modificati: ')
        nume = input('Numele pe care a fost facuta rezervarea:(lasati gol daca nu doriti sa il schimbati) ')
        clasa = input('Clasa:(lasati gol daca nu doriti sa il schimbati) ')
        pret = input('Pretul rezervarii:(introduceti -1 daca nu doriti sa il schimbati) ')
        checkin = input('A fost facut checkin-ul? (da/nu):(lasati gol daca nu doriti sa il schimbati) ')

        return update(id_rezervare, nume, clasa, pret, checkin,lista,undol,redol)

    except ValueError as ve:
        print("Eroare: {}".format(ve))

def menu3():
    print('1. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.')
    print('2. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.')
    print('3. Determinarea prețului maxim pentru fiecare clasă.')
    print('4. Ordonarea rezervărilor descrescător după preț.')
    print('5. Afișarea sumelor prețurilor pentru fiecare nume.')
    print('a. Show all rezervare.')
    print('b. Back')


def run_options(lista,undol,redol):
    while True:
        menu3()
        option = input('Alegeti optiunea: ')
        if option == '1':
            nume = input("Introduceti numele persoanei careia doriti sa ii upgradati clasa: ")
            lista=handle_clasa_sup(lista,nume,undol,redol)
        elif option == '2':
            procent=int(input("Introduceti procentul cu care doriti sa se reduca rezervarile: "))
            lista=handle_ieftinire(lista,procent,undol,redol)
        elif option == '3':
            handle_pret_max_per_clasa(lista)
        elif option == '4':
            handle_ordonare_descresc_rezervari(lista)
        elif option == '5':
            handle_sume_pret_per_nume(lista)
        elif option == 'a':
            handle_show_all_rezervare(lista)
        elif option == 'b':
            break
        else:
            print('Optiune invalida.')

    return lista


def handle_clasa_sup(lista,nume,undol,redol):
    lista = upgrade_clasa(nume, lista,undol,redol)
    handle_show_all_rezervare(lista)
    return lista


def handle_ieftinire(lista,procent,undol,redol):
    try:
        return aplicare_reducere(lista,procent,undol,redol)
    except ValueError as ve:
        print("Eroare: {}".format(ve))

def handle_pret_max_per_clasa(lista):
    rezultat = pret_max_per_clasa(lista)
    for clasa in rezultat:
        print("Clasa {} are preturl maxim {}".format(clasa, rezultat[clasa]))

def handle_ordonare_descresc_rezervari(lista):
    handle_show_all_rezervare(ordonare_descrescator_dupa_pret(lista))

def handle_sume_pret_per_nume(lista):
    rezultat = suma_pret_per_nume(lista)
    for nume in rezultat:
        print("Pe numele {}  sunt rezervari care in total au suma de {}".format(nume, rezultat[nume]))


