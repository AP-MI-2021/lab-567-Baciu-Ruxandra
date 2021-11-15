from Tests.test_Domain import test_rezervare
from Tests.test_CRUD import testAdd, testDelete, testUpdate
from Tests.test_options import testMax, testSuma, testReducere
from Tests.test_undoRedo import test_undoRedo


def run_all_tests():
    test_rezervare()
    testAdd()
    testDelete()
    testUpdate()
    testMax()
    testSuma()
    testReducere()
    test_undoRedo()
