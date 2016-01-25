from utils import *

def test_cyclic_range():

	arr = [ i for i in cyclicRange(2,4,10)]

	assert arr == [2,3]

	arr2 = [ i for i in cyclicRange(5,2,7)]

	assert arr2 == [5,6,0,1]

def test_arr_rotate_right():
	assert [ i for i in arrRotatedRight([1,2,3])] == [3,1,2]

def test_arr_rotate_left():
	assert [ i for i in arrRotatedLeft([1,2,3])] == [2,3,1]

def test_vecs_close():
	assert areVecsClose(Vec2(0.0, 1.00000001), Vec2(0,1))



