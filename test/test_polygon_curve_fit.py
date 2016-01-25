import math
from polygon_curve_fit import _getPolygonCorners
from utils import *

def test_polygon_corners():

	poly = getVec2ListFromTupleList([
		(0,0), (100, 0), (100,100), (0,100)]) 


	assert _getPolygonCorners(poly) == [0,1,2,3]

