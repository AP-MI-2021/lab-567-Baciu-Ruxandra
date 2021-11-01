from Domain.rezervare import creeazaRezervare, getId, getNume, getClasa, getPret, getCheckin


def test_rezervare():
    r=creeazaRezervare('1', 'Carmen', 'economy', 123, 'da')

    assert getId(r) == '1'
    assert getNume(r) == 'Carmen'
    assert getClasa(r) == 'economy'
    assert getPret(r) == 123
    assert getCheckin(r) == 'da'