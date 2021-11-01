from copy import deepcopy

from Domain.rezervare import creeazaRezervare, getId, getClasa, getPret, getCheckin, getNume
from Logic.undoredo_service import UndoRedoService



def find_by_id(id,lista):
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None
def add( id, nume,clasa,pret,checkin,lista):
    '''
    se creaza o rezervare
    :param id_rezervare: unic
    :param nume: cir de caractere,doar litere
    :param clasa:strng
    :param pret:float
    :param checkin:string
    :param lista: lista de rezervari
    :return:o lista continand atat elem vechi cat si cea nou adaugata
    '''
    if find_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja!")
    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def delete(id,lista):
    '''
    Sterge o rezervare dupa un id dat
    :param id:
    id-ul rezervarii care se va sterge
    :param lista: lista de rezervari
    :return: o lista de rezervari fara elementul cu id-ul dat
    '''
    if find_by_id(id, lista) is None:
        raise ValueError("Nu exista o prajitura cu id-ul dat!")
    return [rezervare for rezervare in lista if getId(rezervare) != id]

def update( id, nume, clasa, pret, checkin,lista):
    '''
    Schimba datele unui rezervare dat prin id
    '''
    if find_by_id(id, lista) is None:
        raise ValueError("Nu exista o rezervare cu id-ul dat!")
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:

            if nume=='':
                nume=getNume(rezervare)
            if clasa=='':
                clasa=getClasa(rezervare)
            if pret==-1:
                pret=getPret(rezervare)
            if checkin =='':
                 checkin=getCheckin(rezervare)

            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua