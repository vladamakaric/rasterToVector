from bezier_fit import _getCoordLengthParameterization, getBezierCurveListToFitPoints 
import utils
import numpy as np
from vec2 import *

def test_coord_length_parameterization():
	path = utils.getVec2ListFromTupleList([(0,0), (1,0), (2,0), (2,1)])

	assert _getCoordLengthParameterization(path) == [0, 1/3.0, 2/3.0, 1]

def test_bezier_fit():

	points = [Vec2(0,0), Vec2(1,0), Vec2(2,0), Vec2(3,0)]
	b = getBezierCurveListToFitPoints(points)

	assert utils.areVecArrsClose(points, b[0])









	







