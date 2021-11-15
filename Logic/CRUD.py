from copy import deepcopy

from Domain.rezervare import creeazaRezervare, getId, getClasa, getPret, getCheckin, getNume




def find_by_id(id,lista):
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None


def add( id, nume,clasa,pret,checkin,lista,undol,redol):
    '''
    se creaza o rezervare
    :param id_rezervare: unic
    :param nume: cir de caractere,doar litere
    :param clasa:strng
    :param pret:float
    :param checkin:string
    :param lista: lista de rezervari
    :param undol:
    :param redol:
    :return:o lista continand atat elem vechi cat si cea nou adaugata
    '''
    ls=['economic', 'economic plus','business']
    ls2=['da','nu']

    if find_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    if nume.isalpha() is False:
        raise ValueError("Numele trebuie sa contina doar litere!")
    if clasa in ls is None:
        raise ValueError("Clasa poate sa aia unul dintre urmatoarele tipuri:'economic', 'economic plus','business'")
    if pret<0:
        raise ValueError("Pretul trebuie sa fie mai mare decat 0!")
    if checkin in ls2 is None:
        raise ValueError("Campul checkin-ul poate fi completat doar cu: 'da','nu'")

    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)

    undolist=deepcopy(lista)
    undol.append(undolist)
    redol.clear()

    return lista+[rezervare]


def delete(id,lista,undol,redol):
    '''
    Sterge o rezervare dupa un id dat
    :param id:
    id-ul rezervarii care se va sterge
    :param lista: lista de rezervari
    :return: o lista de rezervari fara elementul cu id-ul dat
    '''
    if find_by_id(id, lista) is None:
        raise ValueError("Nu exista o prajitura cu id-ul dat!")

    undolist = deepcopy(lista)
    undol.append(undolist)
    redol.clear()

    new_ls=[]
    for rezervare in lista:
        if getId(rezervare) != id:
            new_ls.append(rezervare)
    return new_ls

def update( id, nume, clasa, pret, checkin,lista,undol,redol):
    '''
    Schimba datele unui rezervare dat prin id
    '''
    if find_by_id(id, lista) is None:
        raise ValueError("Nu exista o rezervare cu id-ul dat!")

    list=[]

    for rezervare in lista:
        if getId(rezervare) == id:

            if nume=='':
                nume=getNume(rezervare)
            if clasa=='':
                clasa=getClasa(rezervare)
            if float(pret)==-1:
                pret=getPret(rezervare)
            if checkin =='':
                 checkin=getCheckin(rezervare)

            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            list.append(rezervareNoua)

        else:
            list.append(rezervare)

    undolist = deepcopy(lista)
    undol.append(undolist)
    redol.clear()
    lista=deepcopy(list)
    return lista