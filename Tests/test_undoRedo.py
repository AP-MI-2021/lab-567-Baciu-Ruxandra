from copy import deepcopy

from Domain.rezervare import getId, getNume, creeazaRezervare
from Logic.CRUD import add, find_by_id
from Logic.undo_redo import do_undo, do_redo
from UI.console import handle_undo, handle_redo


def test_undoRedo():
    undo=[]
    redo=[]
    ls=[]

    ls = add('1', 'Carmen', 'economy', 1230, 'da', ls, undo, redo)
    ls = add('2', 'Marius', 'economy plus', 250, 'nu',ls, undo, redo)
    ls = add('4', 'Marius', 'economy', 250, 'nu', ls, undo, redo)

    ls=handle_undo(ls,undo,redo)
    assert len(ls)==2
    assert find_by_id('2',ls) is not None
    assert find_by_id('1',ls) is not None

    ls=handle_undo(ls,undo,redo)
    assert len(ls)==1
    assert find_by_id('1', ls) is not None

    ls=handle_undo(ls,undo,redo)
    assert len(ls) == 0

    ls = handle_undo(ls, undo, redo)
    assert len(ls) == 0

    ls = add('1', 'Carmen', 'economy', 1230, 'da', ls, undo, redo)
    ls = add('2', 'Marius', 'economy plus', 250, 'nu', ls, undo, redo)
    ls = add('4', 'Marius', 'economy', 250, 'nu', ls, undo, redo)


    ls = handle_undo(ls, undo, redo)
    assert len(ls) == 2
    assert find_by_id('2', ls) is not None
    assert find_by_id('1', ls) is not None

    ls = handle_undo(ls, undo, redo)
    assert len(ls) == 1
    assert find_by_id('1', ls) is not None

    ls = handle_redo(ls, undo, redo)
    assert len(ls) == 2
    assert find_by_id('1', ls) is not None
    assert find_by_id('2', ls) is not None

    ls = handle_redo(ls, undo, redo)
    assert len(ls) == 3
    assert find_by_id('1', ls) is not None
    assert find_by_id('2', ls) is not None
    assert find_by_id('4', ls) is not None


    ls = handle_undo(ls, undo, redo)
    assert len(ls) == 3
    assert find_by_id('2', ls) is not None
    assert find_by_id('1', ls) is not None
    assert find_by_id('4', ls) is not None

    ls = handle_undo(ls, undo, redo)
    assert len(ls) == 2
    assert find_by_id('2', ls) is not None
    assert find_by_id('1', ls) is not None



    ls = add('10', 'Claudiu', 'business', 1023, 'da', ls, undo, redo)

    ls = handle_redo(ls, undo, redo)
    assert len(ls) == 3
    assert find_by_id('1', ls) is not None
    assert find_by_id('10', ls) is not None

    ls = handle_undo(ls, undo, redo)
    assert len(ls) == 2
    assert find_by_id('1', ls) is not None


    ls = handle_redo(ls, undo, redo)
    assert len(ls) == 3
    assert find_by_id('1', ls) is not None
    assert find_by_id('2', ls) is not None

    ls = handle_redo(ls, undo, redo)
    assert len(ls) == 3
    assert find_by_id('1', ls) is not None
    assert find_by_id('2', ls) is not None