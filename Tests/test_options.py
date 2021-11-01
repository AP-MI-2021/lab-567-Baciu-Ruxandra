from Domain.rezervare import getClasa, getId
from Logic.CRUD import add
from Logic.options_service import upgrade_clasa, ordonare_descrescator_dupa_pret


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
    pass

def testSuma():
    pass

def testReducere():
    pass



