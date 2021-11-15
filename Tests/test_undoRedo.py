from Domain.rezervare import getId, getNume
from Logic.CRUD import add, find_by_id
from Logic.undo_redo import do_undo, do_redo


def test_undoRedo():
    undo=[]
    redo=[]
    ls=[]

    ls = add('1', 'Carmen', 'economy', 1230, 'da', ls, undo, redo)
    ls = add('2', 'Marius', 'economy plus', 250, 'nu',ls, undo, redo)
    ls = add('4', 'Marius', 'economy', 250, 'nu', ls, undo, redo)

    undo=do_undo(undo,redo,ls)
    assert len(undo)==2
    assert find_by_id('2',undo) is not None
    assert find_by_id('1',undo) is not None

    do_undo(undo, redo, ls)
    assert len(undo) == 1
    assert find_by_id('1', undo) is not None



    do_redo(undo,redo)
    assert len(redo) == 1
    # assert find_by_id('1', redo) is not None
    #
    # redo=do_redo(undo, redo)
    # assert len(redo) == 2
    # assert find_by_id('2', redo) is not None
    # assert find_by_id('1', redo) is not None
    #
    # redo=do_redo(undo, redo)
    # assert len(redo) == 3
    # assert find_by_id('2', redo) is not None
    # assert find_by_id('1', redo) is not None
    # assert find_by_id('4', redo) is not None