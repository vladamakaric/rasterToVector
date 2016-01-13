from digraph_shortest_cycles import *
import numpy as np

def test_digraph_shortest_cycles():

	edges = [(0,2), (0,3), (1,0), (1,3), (2,1), (3,2)]

	dsc = DigraphShortestCycles(edges, 4)

	print dsc.getShortestCyclesSet()

	assert dsc.getShortestCyclesSet() == set([(0,2,1), (1,3,2)])

