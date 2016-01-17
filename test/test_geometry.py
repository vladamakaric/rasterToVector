from vec2 import *
from line import *
from geometry import *
from line_segment import *

def test_line_intersection():

	l1 = Line(Vec2(0,0), Vec2(1,1))
	l2 = Line(Vec2(2,0), Vec2(-1,1))

	assert getLineIntersection(l1,l2) == Vec2(1,1)
	
	l1 = Line(Vec2(0,0), Vec2(1,1))
	l2 = Line(Vec2(2,0), Vec2(1,1))

	assert getLineIntersection(l1,l2) == None

	l1 = Line(Vec2(0,0), Vec2(1,0))
	l2 = Line(Vec2(0,2), Vec2(1,-1))

	assert getLineIntersection(l1,l2) == Vec2(2,0)

def test_line_distance():

	l1 = Line(Vec2(0,0), Vec2(1,1))

	assert getVec2ToLineDistance(Vec2(1,0), l1) == 1


def test_line_segment_intersection():

	ls1 = LineSegment(Vec2(0,0), Vec2(4,4))
	ls2 = LineSegment(Vec2(0,4), Vec2(4,0))

	assert getLineSegmentIntersection(ls1, ls2) == Vec2(2,2)

def test_closest_point_to_vec_on_unit_square():

	vec = Vec2(0.3,0.3)

	assert getClosestPointToVecOnUnitSquare(Vec2(0.5, 0.5), vec) == vec
	assert getClosestPointToVecOnUnitSquare(Vec2(0.5,0.5), Vec2(1.1, 1)) == Vec2(1,1)




