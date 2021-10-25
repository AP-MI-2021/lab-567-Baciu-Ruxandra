from Domain.rezervare import Rezervare


def test_rezervare():
    r=Rezervare('1', 'Carmen', 'economy', 123, 'da')

    assert r.id_entity == '1'
    assert r.nume == 'Carmen'
    assert r.clasa == 'economy'
    assert r.pret == 123
    assert r.checkin == 'da'