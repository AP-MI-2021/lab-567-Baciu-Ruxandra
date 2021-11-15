def do_undo(undol,redol,current_ls):
    '''
    Se executa undo
    :param undol: lista cu toate instructiunile facute
    :param redol: lista cu toate instructiunile facute cu undo
    :return:
    '''
    if undol:
        redol.append(current_ls)
        return undol.pop()
    return None

def do_redo(undol,redol):
    '''
    se executa redo
    lista cu toate instructiunile facute
    :param redol: lista cu toate instructiunile facute cu undo
    :return:
    '''
    if redol:
        top_redo = redol.pop()
        undol.append(top_redo)
        return top_redo
    return None
