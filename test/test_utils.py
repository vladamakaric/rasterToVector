from utils import *

def test_cyclic_range():

	arr = [ i for i in cyclicRange(2,4,10)]

	assert arr == [2,3]

	arr2 = [ i for i in cyclicRange(5,2,7)]

	assert arr2 == [5,6,0,1]

