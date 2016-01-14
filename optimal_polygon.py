from polygon_connectivity import *
from digraph_shortest_cycles import *
from collections import deque
from path_variance import PathVariance

def getOptimumPathAlignedPolygon(path):
	implicitGraph = getPossiblePolygonImplicitGraph(path)
	edges = getPossiblePolygonContractedEdges(implicitGraph)
	pv = PathVariance(path)

	eweights = [pv.getLineSegmentVariance(i,j) for i,j in edges]
	weightedEdges = [ (i,j,w) for (i,j), w in zip(edges, eweights) ]

	dslwc = DigraphShortestLengthWeightedCycles(weightedEdges, len(path))

	return dslwc.getShortestCyclesSet().pop()
	
def getCycleCost(cycle, costFunc):

	cycleShift = deque(cycle)
	cycleShift.rotate(1)
	
	cost = 0
	for i,j in zip(cycleShift, cycle):
		cost+=costFunc(i,j)
		
	return cost











	
