from  task_2.task_2 import calculate_point_position
import pytest



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