from Domain.rezervare import getClasa, getId, getPret
from Logic.CRUD import add, find_by_id
from Logic.options_service import upgrade_clasa, ordonare_descrescator_dupa_pret, pret_max_per_clasa, \
    suma_pret_per_nume, aplicare_reducere


def testUpgrade():
    lista = []
    lista = add('1', 'Carmen', 'economy', 123, 'da', lista)
    lista = add('2', 'Marius', 'economy plus', 250, 'nu', lista)
    lista = add('3', 'Claudiu', 'business', 1023, 'da', lista)

    rez_upgradata= upgrade_clasa(lista[1],'Marius')
    assert getClasa(rez_upgradata)=='business'

    rez_upgradata = upgrade_clasa(lista[0], 'Carmen')
    assert getClasa(rez_upgradata) == 'economy plus'

def testOrdonare():
    lista = []
    lista = add('1', 'Carmen', 'economy', 1230, 'da', lista)
    lista = add('2', 'Marius', 'economy plus', 250, 'nu', lista)
    lista = add('3', 'Claudiu', 'business', 1023, 'da', lista)

    rezultat=ordonare_descrescator_dupa_pret(lista)

    assert getId(rezultat[0]) == "2"
    assert getId(rezultat[1]) == "3"
    assert getId(rezultat[2]) == "1"

def testMax():
    lista = []
    lista = add('1', 'Carmen', 'economy', 1230, 'da', lista)
    lista = add('2', 'Marius', 'economy plus', 250, 'nu', lista)
    lista = add('3', 'Claudiu', 'business', 1023, 'da', lista)
    lista = add('4', 'Claudiu', 'business', 1003, 'nu', lista)

    rezultat = pret_max_per_clasa(lista)

    assert len(rezultat) == 3
    assert rezultat['economy'] == 1230
    assert rezultat['economy plus'] == 250
    assert rezultat['business'] == 1023

def testSuma():
    lista = []
    lista = add('1', 'Carmen', 'economy', 1230, 'da', lista)
    lista = add('2', 'Marius', 'economy plus', 250, 'nu', lista)
    lista = add('3', 'Claudiu', 'business', 1023, 'da', lista)
    lista = add('4', 'Claudiu', 'business', 1003, 'nu', lista)

    rezultat = suma_pret_per_nume(lista)

    assert len(rezultat) == 3
    assert rezultat['Carmen'] == 1230
    assert rezultat['Marius'] == 250
    assert rezultat['Claudiu'] == 2026


def testReducere():
    lista = []
    lista = add('1', 'Carmen', 'economy', 1230, 'da', lista)
    lista = add('2', 'Marius', 'economy plus', 250, 'nu', lista)
    lista = add('3', 'Claudiu', 'business', 1023, 'da', lista)
    lista = add('4', 'Claudiu', 'business', 1003, 'nu', lista)

    rezultat = aplicare_reducere(lista,10)

    rezervare_modif=find_by_id('1',rezultat)
    assert getPret(rezervare_modif)==1107

    rezervare_modif=find_by_id('2',rezultat)
    assert getPret(rezervare_modif) == 250

    rezervare_modif=find_by_id('3',rezultat)
    assert getPret(rezervare_modif) == 920.7

    rezervare_modif=find_by_id('4',rezultat)
    assert getPret(rezervare_modif)==1003



