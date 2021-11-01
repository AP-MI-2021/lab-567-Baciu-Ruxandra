from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import add, find_by_id, delete, update


def testAdd():
    ls=[]
    ls=add('1', 'Carmen', 'economy', 123, 'da',ls)

    assert len(ls)==1
    assert getId(find_by_id("1",ls)) == '1'
    assert getNume(find_by_id("1",ls)) == 'Carmen'
    assert getClasa(find_by_id("1",ls)) == 'economy'
    assert getPret(find_by_id("1",ls)) == 123
    assert getCheckin(find_by_id("1",ls)) == 'da'

def testDelete():
    ls = []
    ls = add('1', 'Carmen', 'economy', 123, 'da', ls)
    ls = add('2', 'Marius', 'economy plus', 250, 'nu', ls)

    assert len(ls) == 2
    assert find_by_id("3", ls) is None
    assert find_by_id("2", ls) is not None

    try:
        ls = delete("3", ls)
        assert False
    except ValueError:
        assert len(ls) == 2
        assert find_by_id("2", ls) is not None
    except Exception:
        assert False

def testUpdate():
    ls = []
    ls = add('1', 'Carmen', 'economy', 123, 'da', ls)
    ls = add('2', 'Marius', 'economy plus', 250, 'nu', ls)

    ls=update('2', '', '', 450, '', ls)

    rezervare_noua=find_by_id('1',ls)

    assert getId(rezervare_noua) == '1'
    assert getNume(rezervare_noua) == 'Carmen'
    assert getClasa(rezervare_noua) == 'economy'
    assert getPret(rezervare_noua) == 123
    assert getCheckin(rezervare_noua) == 'da'

    rezervare_noua = find_by_id('2', ls)
    assert getId(rezervare_noua) == '2'
    #assert getNume(rezervare_noua) == 'Marius'
    assert getClasa(rezervare_noua) == 'economy plus'
    assert getPret(rezervare_noua) == 450
    assert getCheckin(rezervare_noua) == 'nu'



