from vec2 import *

def test_cross():
	assert Vec2(1,1).cross(Vec2(1,1)) == 0
	assert Vec2(1,0).cross(Vec2(0,1)) == 1

def test_coordinatewise_normalize():
	assert Vec2(-5,5).normalizeCoordinatewise() == Vec2(-1,1)
	assert Vec2(1,1).normalizeCoordinatewise() == Vec2(1,1)
	assert Vec2(4,0).normalizeCoordinatewise() == Vec2(1,0)
