from task_1 import circle_array
def test_circle_array():
    """Проверка функции circle_array"""
    assert circle_array(4,3) == ["1","3"]
    assert circle_array(5,4) == ["1","4","2","5","3"]
    assert not circle_array(4,5)
    assert circle_array(4,4) == ["1"] 

