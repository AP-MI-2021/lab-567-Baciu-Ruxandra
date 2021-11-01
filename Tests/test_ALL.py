from Tests.test_Domain import test_rezervare
from Tests.test_CRUD import testAdd, testDelete, testUpdate


def run_all_tests():
    test_rezervare()
    testAdd()
    testDelete()
    testUpdate()
