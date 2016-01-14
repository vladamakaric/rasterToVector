from utils import *
from optimal_polygon import *

def test_cycle_cost():

	def costF(i,j):
		return 1

	cycle = [1,2,3]
	assert getCycleCost(cycle, costF) == 3

def test_optimal_path_aligned_polygon():

	path = getVec2ListFromTupleList( [
		(3,0), (3,1), (3,2), (3,3), (3,4), (2,4), (1,4), (0,4), (0,5), (1,5), (1,6), (2,6),
		(2,7), (3,7), (4,7), (5,7), (6,7), (7,7), (8,7), (8,6), (8,5), (7,5), (7,4), (7,3),
		(6,3), (6,2), (5,2), (5,1), (4,1), (4,0)])
    
	assert getOptimumPathAlignedPolygon(path) == (0,4,7,12,18,20)

