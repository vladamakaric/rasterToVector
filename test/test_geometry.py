from vec2 import *
from line import *
from geometry import *

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
