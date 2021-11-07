from copy import deepcopy

from Domain.rezervare import creeazaRezervare, getId, getCheckin, getPret, getClasa, getNume
from Logic.CRUD import update




def upgrade_clasa(rezervare,nume,lista):
    '''
    se cauta schimba clasa
    :param rezervare:
    :param nume:
    :return:
    '''
    lst=[getId(rezervare),getNume(rezervare),getClasa(rezervare),getPret(rezervare),getCheckin(rezervare)]

    if str(lst[1]).find(nume) != -1:
        if str(lst[2]).find('economy plus') != -1:
            rezervare_new = creeazaRezervare(lst[0], lst[1], 'business', lst[3], lst[4])
            rezervare = deepcopy(rezervare_new)
            update(getId(rezervare),getNume(rezervare),getClasa(rezervare),getPret(rezervare),getCheckin(rezervare),lista)
            return rezervare

        elif str(lst[2]).find('economy') != -1:
            rezervare_new=creeazaRezervare(lst[0],lst[1],'economy plus',lst[3],lst[4])
            rezervare=deepcopy(rezervare_new)
            update(getId(rezervare), getNume(rezervare), getClasa(rezervare), getPret(rezervare), getCheckin(rezervare),lista)
            return rezervare

    return None

def ordonare_descrescator_dupa_pret(lista):
    '''
    sorteaza descrescator dupa pret rezervarile din lista
    :param lista: lista cu rezervari
    :return: lista ordonata dupa cerinta de mai sus
    '''
    return sorted(lista,key=lambda rezervare: getPret(rezervare),reverse=True)

def pret_max_per_clasa(lista):
    '''
    determina pretul maxim pentru fiecare clasa
    :param lisat: lista cu rezervari
    :return: dictionar care are ca si chei cele trei tipuri de clase si ca si valori pretul maxim pentru fiecare clasa
    '''
    rezultat = {}
    for rezervare in lista:
        clasa = getClasa(rezervare)
        pret = getPret(rezervare)
        if clasa in rezultat:
            if pret > rezultat[clasa]:
                rezultat[clasa] = pret
        else:
            rezultat[clasa] = pret
    return rezultat

def suma_pret_per_nume(lista):
    '''
    determina suma preturilor pentru fiecare nume din lista
    :param lista: lista rezervarilor
    :return: dictionar care are ca si chei numele persoanelor iar ca si valori are suma preturilor corespunzatoare
     numelor respective
    '''
    rezultat = {}
    for rezervare in lista:
        nume = getNume(rezervare)
        pret = getPret(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + pret
        else:
            rezultat[nume] = pret
    return rezultat

def aplicare_reducere(lista,procent):
    '''
    ieftineste toate rezervarile la care s-a facut checkin-ul cu un procent dat
    :param lista: lista cu rezervari
    :param procent: procentul cu care se doreste ieftinirea
    :return: lista care contine modificarile facute
    '''

    if procent<0:
        raise ValueError("Procentul trebuie sa fie mai mare decat 0!")
    for rezervare in lista:
        if getCheckin(rezervare) == "da":
            reducere=((100-procent)/100)*getPret(rezervare)
            rezervareNoua=creeazaRezervare(getId(rezervare),getNume(rezervare),getClasa(rezervare),reducere,
                                           getCheckin(rezervare))
            lista.remove(rezervare)
            lista.append(rezervareNoua)
    return lista

