def do_undo(undol:list,redol:list,current_ls:list):
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

def do_redo(undol:list,redol:list):
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
