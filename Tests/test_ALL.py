from Tests.test_Domain import test_rezervare
from Tests.test_CRUD import testAdd, testDelete, testUpdate
from Tests.test_options import testMax, testSuma, testReducere


def run_all_tests():
    test_rezervare()
    testAdd()
    testDelete()
    testUpdate()
    testMax()
    testSuma()
    testReducere()
