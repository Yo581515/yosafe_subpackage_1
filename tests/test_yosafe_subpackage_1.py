
from yosafe_subpackage_1.yosafe_subpackage_1_functions import *
from yosafe_subpackage_1.yosafe_subpackage_1_functions_2 import *

def test_yosafe_get_yosafe_subpackage_1():
    result = yosafe_get_yosafe_subpackage_1()
    print(result)
    assert "Error" not in result



def test_yosafe_add():
    assert yosafe_add(1, 2) == 3
    assert yosafe_add(-1, 1) == 0

def test_yosafe_add_2():
    assert yosafe_add_2(1, 2) == 3
    assert yosafe_add_2(-1, 1) == 0
    assert yosafe_add_2(1, 1) == 2
    assert yosafe_add_2(2, 2) == 4