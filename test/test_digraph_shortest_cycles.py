from digraph_shortest_cycles import *
import numpy as np

def test_digraph_shortest_cycles():

	edges = [(0,2,1), (0,3,1), (1,0,1), (1,3,1), (2,1,1), (3,2,1), (3,4,1), (4,2,1)]

	dsc = DigraphShortestLengthWeightedCycles(edges, 5)

	# print dsc.getShortestCyclesSet()

	assert dsc.getShortestCyclesSet() == set([(0,2,1), (1,3,2)])

	#the first edge is heavier now, so there will be one less shortest cycle
	edges2 = [(0,2,2), (0,3,1), (1,0,1), (1,3,1), (2,1,1), (3,2,1)]

	dsc2 = DigraphShortestLengthWeightedCycles(edges2, 4)

	assert dsc2.getShortestCyclesSet() == set([(1,3,2)])

	# edges2 = [(0,1), (0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,0), (5,1)]
	# dsc2 = DigraphShortestCycles(edges2, 6)
	# assert dsc2.getShortestCyclesSet() == set([(0,2,3,5), (0,2,4,5), (1,2,4,5), (1,2,3,5)])


