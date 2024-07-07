import pytest

from task_4.task_4 import calculate_steps, calcultate_arithmetic_mean


@pytest.mark.parametrize(("digits","a_m"),[
    ([1,2,3],2),
    ([1,10,2,9],5)
])
def test_calcultate_arithmetic_mean(digits,a_m):
    """тест функции подсчета среднего арифметического списка чисел"""
    assert calcultate_arithmetic_mean(digits) == a_m



@pytest.mark.parametrize(("digits","steps"),[
    ([1,2,3],2),
    ([1,10,2,9],16)
])
def test_calculate_steps(digits,steps):
    """тест функции подсчета шагов """
    assert calculate_steps(digits) == steps
