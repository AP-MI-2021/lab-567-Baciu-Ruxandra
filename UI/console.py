from Domain.rezervare import toString
from Logic.CRUD import add, delete, update
from Logic.options_service import upgrade_clasa, suma_pret_per_nume, ordonare_descrescator_dupa_pret, \
    pret_max_per_clasa, aplicare_reducere



def print_menu():
    print('1. CRUD Rezervare')
    print('2. Operatii')
    print('i. Interfata noua(add,delete,show all)')
    print('a. Show all rezervare.')
    print('u. Undo')
    print('r. Redo')
    print('x. Iesire')


def command_line_console(lista):
    # citim instructiunile asa: delete,7;add,mara,economic,1234,da;showall
    arr=input('Introduceti instructiunile (add,delete,showall) pe care doriti sa le utilizati separate din prin ; iar elementele prin ,\n')
    intructiuni_lst=arr.split(';')
    print('Au fost introduse {} comenzi\n'.format(len(intructiuni_lst)))
    com=0
    for instructiune in intructiuni_lst:
        com+=1
        arr=instructiune.split(',')
        if arr[0]=='add':
            if len(arr)!=6:
                print("Comanda 'add' nu e valida! Trebuie sa contina numele instructiunii, id,nume,clasa,pret,checkin!")
                break
            else:
                try:
                    print("Rezultatul dupa comanda numarul {}\n".format(com))
                    print(add(arr[1],arr[2],arr[3],float(arr[4]),arr[5],lista))
                except ValueError as ve:
                    print("Eroare: {}".format(ve))

        elif arr[0]=='delete':
            if len(arr)!=2:
                print("Comanda 'delete' nu e valida! Trebuie sa contina numele instructiunii si id rezervarii pe care doriti sa o stergeti!\n")
                break
            else:
                try:
                    print("Rezultatul dupa comanda numarul {}\n".format(com))
                    print(delete(arr[1],lista))
                except ValueError as ve:
                    print("Eroare: {}".format(ve))


        elif arr[0]=='showall':
            if len(arr)!=1:
                print('Comanda showall trebuie sa dontina doar numele intructiunii!')
                break
            else:
                print("Rezultatul dupa comanda numarul {}\n".format(com))
                for rezervare in lista:
                    print(toString(rezervare))
        else:
            print("Comanda nu e valida!")
            break
    return



def run_console(lista):

    while True:
        print_menu()
        option = input('Alegeti optiunea: ')
        if option == '1':
            run_crud_rezervare(lista)
        elif option == '2':
            run_options(lista)
        elif option=='i':
            command_line_console(lista)
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
    try:
        id_rezervare = input('ID-ul rezervarii: ')
        nume = input('Numele pe care a fost facuta rezervarea: ')
        clasa = input('Clasa: ')
        pret = float(input('Pretul rezervarii: '))
        checkin = input('A fost facut checkin-ul? (da/nu): ')

        return add(id_rezervare, nume, clasa, pret, checkin, lista)

    except ValueError as ve:
        print("Eroare: {}".format(ve))


def handle_show_all_rezervare(lista):
    for rezervare in lista:
        print(toString(rezervare))

def handle_delete_rezervare(lista):
    try:
        id_rezervare = input('ID-ul rezervarii pe care doriti sa o stergeti: ')
        return delete(id_rezervare,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))


def handle_update_rezervare(lista):
    try:
        id_rezervare = input('ID-ul rezervarii pe care doriti sa o modificati: ')
        nume = input('Numele pe care a fost facuta rezervarea:(lasati gol daca nu doriti sa il schimbati) ')
        clasa = input('Clasa:(lasati gol daca nu doriti sa il schimbati) ')
        pret = input('Pretul rezervarii:(introduceti -1 daca nu doriti sa il schimbati) ')
        checkin = input('A fost facut checkin-ul? (da/nu):(lasati gol daca nu doriti sa il schimbati) ')

        return update(id_rezervare, nume, clasa, pret, checkin,lista)

    except ValueError as ve:
        print("Eroare: {}".format(ve))

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
    try:
        handle_create_rezervare(aplicare_reducere(lista,procent))
    except ValueError as ve:
        print("Eroare: {}".format(ve))

def handle_pret_max_per_clasa(lista):
    rezultat = pret_max_per_clasa(lista)
    for clasa in rezultat:
        print("Clasa {} are preturl maxim {}".format(clasa, rezultat[clasa]))

def handle_ordonare_descresc_rezervari(lista):
    handle_create_rezervare(ordonare_descrescator_dupa_pret(lista))

def handle_sume_pret_per_nume(lista):
    rezultat = suma_pret_per_nume(lista)
    for nume in rezultat:
        print("Pe numele {}  sunt rezervari care in total au suma de {}".format(nume, rezultat[nume]))


