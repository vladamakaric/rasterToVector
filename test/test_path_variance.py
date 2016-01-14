from path_variance import *
from vec2 import *
from utils import *

def test_path_variance():

	path = [(0,0), (1,1), (2,0)]
	pv = PathVariance(getVec2ListFromTupleList(path))

	print pv.getLineSegmentVariance(0,2)
	print 2*math.sqrt(1/3.0)

	assert pv.getLineSegmentVariance(0,2) == 2*math.sqrt(1/3.0)

	path2 = [(0,0), (1,1), (2,2)]

	pv2 = PathVariance(getVec2ListFromTupleList(path2))

	assert pv2.getLineSegmentVariance(0,2) == 0
