import os
import pytest

from task_2.task_2 import (calculate_point_position, get_circle_data,
                           get_points_data)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

@pytest.mark.parametrize(("gx","gy","r","x","y","position"),[
    (1,1,5,0,0,1),
    (1,1,5,1,6,0),
    (1,1,5,6,6,2),
    (2,2,2,4,2,0),
    (2,2,2,3,1,2)
])
def test_calculate_point_position(gx,gy,r,x,y,position):
    """Test calculate"""
    assert calculate_point_position(gx,gy,r,x,y) == position


def test_get_circle_data():
    """Проверка функции получение данных об окружности из файла"""
    assert get_circle_data(os.path.join(BASE_DIR,"task_2/test_data/file_1.txt")) == {"center":"1 1","radius":"5"}


def test_get_points_data():
    """Проверка получения данных о точках из файла"""
    assert get_points_data(os.path.join(BASE_DIR,"task_2/test_data/file_2.txt")) == ["0 0","1 6","6 6"]