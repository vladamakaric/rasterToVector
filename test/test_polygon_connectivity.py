from utils import *
from vec2 import *
from polygon_connectivity import *

def test_get_delta_contraint():

	assert getPositiveAndNegativeConstraintDelta(Vec2(2,4)) == (Vec2(1,-1), Vec2(-1,1))
	assert getPositiveAndNegativeConstraintDelta(Vec2(-3,2)) == (Vec2(1,1), Vec2(-1,-1))
	assert getPositiveAndNegativeConstraintDelta(Vec2(-3,-2)) == (Vec2(-1,1), Vec2(1,-1))

	assert getPositiveAndNegativeConstraintDelta(Vec2(0,-2)) == (Vec2(-1,1), Vec2(1,1))
	assert getPositiveAndNegativeConstraintDelta(Vec2(0,2)) == (Vec2(1,-1), Vec2(-1,-1))
	assert getPositiveAndNegativeConstraintDelta(Vec2(9,0)) == (Vec2(-1,-1), Vec2(-1,1))


def test_update_angle_constraints():

	assert updateAngleConstraints(Vec2(1,0), Vec2(0,1), Vec2(2,2)) == (Vec2(3,1), Vec2(1,3))

	assert updateAngleConstraints(Vec2(3,2), Vec2(2,3), Vec2(2,2)) == (Vec2(3,2), Vec2(2,3))


def test_getPossiblePolygonImplicitGraph():

	path2 = getVec2ListFromTupleList([(3,0),(3,-1),(3,-2),(2,-2),(1,-2),(0,-2),(0,-3),
			 (1,-3),(2,-3),(3,-3),(4,-3),(4,-2),(4,-1), (4,0)])

	assert getPossiblePolygonImplicitGraph(path2) == [4, 7, 7, 7, 10, 11, 11, 11, 12, 0, 1, 1, 4, 4]
