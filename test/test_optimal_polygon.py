from utils import *
from optimal_polygon import *

def test_optimal_path_aligned_polygon():

	path = getVec2ListFromTupleList( [
		(3,0), (3,1), (3,2), (3,3), (3,4), (2,4), (1,4), (0,4), (0,5), (1,5), (1,6), (2,6),
		(2,7), (3,7), (4,7), (5,7), (6,7), (7,7), (8,7), (8,6), (8,5), (7,5), (7,4), (7,3),
		(6,3), (6,2), (5,2), (5,1), (4,1), (4,0)])
    
	path2 = getVec2ListFromTupleList( [
		(3,0), (3,-1), (3,-2), (3,-3), (3,-4), (2,-4), (1,-4), (0,-4), (0,-5), (1,-5), (1,-6), (2,-6),
		(2,-7), (3,-7), (4,-7), (5,-7), (6,-7), (7,-7), (8,-7), (8,-6), (8,-5), (7,-5), (7,-4), (7,-3),
		(6,-3), (6,-2), (5,-2), (5,-1), (4,-1), (4,0)])

	assert getOptimumPathAlignedPolygonIndices(path) == (0,4,7,12,18,20)
	assert getOptimumPathAlignedPolygonIndices(path2) == (0,4,7,12,18,20)

def test_optimal_polygon_from_opt_aligned_polygon():
	path = getVec2ListFromTupleList( [
		(0,0), (0,-1), (0,-2), (0,-3),
		(1,-3), (2,-3), (3,-3),
		(3,-2), (3,-1), (3,0),
		(2,0), (1, 0)])

	assert getOptimumPolygonFromOptAlignedPolygon((0,3,6,9), path) == [
			Vec2(0,0), Vec2(0,-3), Vec2(3,-3), Vec2(3,0)]


