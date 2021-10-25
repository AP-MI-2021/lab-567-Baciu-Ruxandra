import datetime
from copy import deepcopy

from Domain.update_operation import UpdateOperation
from Logic.rezervare_service import RezervareService
from Logic.options_service import OptionsService
from Logic.undoredo_service import UndoRedoService


class Console:
    def __init__(self,
                rezervare_service: RezervareService,
                options_service: OptionsService,
                undo_redo_service:UndoRedoService):
        self.__rezervare_service = rezervare_service
        self.__options_service = options_service
        self.__undo_redo_service= undo_redo_service

    def print_menu(self):
        print('1. CRUD Rezervare')
        print('2. Operatii')
        print('a. Show all rezervare.')
        print('u. Undo')
        print('r. Redo')
        print('x. Iesire')

    def run_console(self):

        while True:
            self.print_menu()
            option = input('Alegeti optiunea: ')
            if option == '1':
                self.run_crud_rezervare()
            elif option == '2':
                self.run_options()
            elif option == 'a':
                self.handle_show_all_rezervare()
            elif option == 'u':
                self.__undo_redo_service.do_undo()
            elif option == 'r':
                self.__undo_redo_service.do_redo()
            elif option == 'x':
                break
            else:
                print('Comanda invalida!')


    def run_crud_rezervare(self):
        while True:
            print('1. Create rezervare.')
            print('2. Delete rezervare.')
            print('3. Update rezervare.')
            print('a. Show all rezervare.')
            print('b. Back')
            option = input('Alegeti optiunea: ')
            if option == '1':
                self.handle_create_rezervare()
            elif option == '2':
                self.handle_delete_rezervare()
            elif option == '3':
                self.handle_update_rezervare()
            elif option == 'a':
                self.handle_show_all_rezervare()
            elif option == 'b':
                break
            else:
                print('Optiune invalida.')

    def handle_create_rezervare(self):
        try:
            id_rezervare = input('ID-ul rezervarii: ')
            nume = input('Numele pe care a fost facuta rezervarea: ')
            clasa = input('Clasa: ')
            pret = int(input('Pretul rezervarii: '))
            checkin = input('A fost facut checkin-ul? (da/nu): ')

            self.__rezervare_service.create(id_rezervare, nume, clasa, pret, checkin)

            print('Rezervarea a fost adaugata cu succes!')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def handle_show_all_rezervare(self):
        for rezervare in self.__rezervare_service.get_all():
            print(rezervare)

    def handle_delete_rezervare(self):
        try:
            id_rezervare = input('ID-ul rezervarii pe care doriti sa o stergeti: ')
            self.__rezervare_service.delete(id_rezervare)
            print('Rezervarea a fost stearsa!')
        except KeyError as ke:
            print(ke)

    def handle_update_rezervare(self):
        try:
            id_rezervare = input('ID-ul rezervarii pe care doriti sa o modificati: ')
            nume = input('Numele pe care a fost facuta rezervarea:(lasati gol daca nu doriti sa il schimbati) ')
            clasa = input('Clasa:(lasati gol daca nu doriti sa il schimbati) ')
            pret = input('Pretul rezervarii:(lasati gol daca nu doriti sa il schimbati) ')
            checkin = input('A fost facut checkin-ul? (da/nu):(lasati gol daca nu doriti sa il schimbati) ')

            self.__rezervare_service.update(id_rezervare, nume, clasa, pret, checkin)

            print('Rezervarea a fost modificata cu succes!')
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)


    def run_options(self):
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
                self.handle_clasa_sup(nume)
            elif option == '2':
                self.handle_ieftinire()
            elif option == '3':
                self.handle_pret_max_per_clasa()
            elif option == '4':
                self.handle_ordonare_descresc_rezervari()
            elif option == '5':
                self.handle_sume_pret_per_nume()
            elif option == 'b':
                break
            else:
                print('Optiune invalida.')


    def handle_clasa_sup(self,nume):
        ok = 0

        print('Schimbari:\n')
        for rezervare in self.__rezervare_service.get_all():
            rezultat=self.__options_service.upgrade_clasa(rezervare,nume)
            if rezultat is not None:
                ok = +1
                print(rezultat)
        if ok == 0:
            print("Nu s-au putut face schimbari!")


    def handle_ieftinire(self):
        pass

    def handle_pret_max_per_clasa(self):
        pass

    def handle_ordonare_descresc_rezervari(self):
        pass

    def handle_sume_pret_per_nume(self):
        pass


'''
    def handle_cautare_fulltext_masini_clienti(self):
        try:
            str= input('Dati secventa pe care o cautati: ')
            ok=0

            for masina in self.__masina_service.get_all():
                rezultat= self.__options_service.cautare_masini(masina,str)
                if rezultat is not None:
                    ok=+1
                    print(rezultat)

            for card_client in self.__card_client_service.get_all():
                rezultat = self.__options_service.cautare_carduri(card_client,str)
                if rezultat is not None:
                    ok=+1
                    print(rezultat)
            if ok==0:
                print("Secventa cautata nu exista!")
        except ValueError as ve:
            print (ve)

    def handle_tranz_suma_interval(self):
        try:
            s1= input('Dati capatul inferior al intervalului: ')
            s2=input('Dati capatul superior al intervalului: ')
            lst = map(self.__options_service.afis_tranz_cu_suma_din_interval,self.__tranzactie_service.get_all())
            '''
           # lst=[]
            #for tranzactie in self.__tranzactie_service.get_all():
             #   lst.append(self.__options_service.afis_tranz_cu_suma_din_interval(tranzactie))
'''
            rezultat=filter(lambda x : int(s1)<=x<=int(s2),lst)
            for item in rezultat:
                for tranzactie in self.__tranzactie_service.get_all():
                    rez=self.__options_service.afis_tranz_cu_suma_din_interval(tranzactie)
                    if item == rez:
                        print(tranzactie)

        except ValueError as ve:
            print (ve)



    def handle_ordonare_masini(self):
      
        rezultat=[]
        print('Masinile ordonate descrescator dupa suma manopera:')
        lst=[tranzactie.suma_manopera for tranzactie in self.__tranzactie_service.get_all()]
        lst.sort()
        for i in range(len(lst)):
            for tranzactie in self.__tranzactie_service.get_all():
                if tranzactie.suma_manopera == lst[i]:
                    rezultat.append(self.__options_service.get_masina(tranzactie.masina))
        lst_rev=lst[::-1]
        s=0
        for element in reversed(rezultat):
            print(f'Masina :{element} are suma manopera :{lst_rev[s]}')
            s+=1



    def handle_ordonare_card_client(self):
        
        def merge_sort(rezultat, key=lambda x: x,reversed = False):
            if len(rezultat) > 1:
                aid = len(rezultat) // 2
                left = rezultat[:aid]
                right = rezultat[aid:]
                merge_sort(left, key,reversed)
                merge_sort(right, key,reversed)
                i = 0
                j = 0
                k = 0
                while i < len(left) and j < len(right):
                    if key(left[i]) < key(right[j]):
                        rezultat[k] = left[i]
                        i += 1
                    else:
                        rezultat[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    rezultat[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    rezultat[k] = right[j]
                    j += 1
                    k += 1
                if reversed == True:
                    return rezultat[::-1]
        rezultat = []
        print('Cardurile client ordonate descrescator dupa reducerile acordate:')
        lst = [tranzactie.suma_totala for tranzactie in self.__tranzactie_service.get_all()]
        lst_rev=merge_sort(lst,key = lambda x:x,reversed = True)
        for i in range(len(lst)):
            for tranzactie in self.__tranzactie_service.get_all():
                if tranzactie.suma_totala == lst[i]:
                    rezultat.append(self.__options_service.get_card_client(tranzactie.card_client))
                    lst[i]=tranzactie.suma_totala-(tranzactie.suma_manopera + tranzactie.suma_piese)

        s = 0
        for element in reversed(rezultat):
            print(f'Cardului client :{element} i-a fost aplicata reducerea :{lst_rev[s]}')
            s += 1


    def handle_sterge_tranz_interval(self):
        
        lst=[]
        date1= datetime.datetime.strptime(input('Introduceti ziua care reprezinta capatul inferior al intervalului (dd.mm.yyyy):'), '%d.%m.%Y')
        lst.append(date1)
        date2 = datetime.datetime.strptime(input('Introduceti ziua care reprezinta capatul superior al intervalului (dd.mm.yyyy):'), '%d.%m.%Y')
        lst.append(date2)
        ok=0
        for tranzactie in self.__tranzactie_service.get_all():
            date=datetime.datetime.strptime(tranzactie.data_time,'%d.%m.%Y %H:%M')
            lst.append(date)
            lst.sort()
            if lst[1] == date:
                self.__tranzactie_service.delete(tranzactie.id_entity)
                ok=+1
            lst.remove(date)
        if ok!=0:
            print('Tranzactiile care inplinesc conditia data au fost sterse!')
        else:
            print('Nu s-au gasit tranzactii care sa indeplineasca conditia data!')


    def handle_actualizare_garanztie(self):
        
        today_date=datetime.datetime.now()
        print(int(today_date.year))
        for masina in self.__masina_service.get_all():
            print(int(masina.an_achizitie))
            print(int(today_date.year) - int(masina.an_achizitie) + 1)
            #masina_veche=deepcopy(masina)
            if (int(today_date.year) - int(masina.an_achizitie) + 1 <=  3) and (int(masina.nr_km)<=60000):
                garantie='da'
            else :
                garantie = 'nu'
            self.__masina_service.update(masina.id_entity, '', '', '', garantie)





'''