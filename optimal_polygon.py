from polygon_connectivity import *
from digraph_shortest_cycles import *
from collections import deque
from path_variance import PathVariance
from geometry import *
import pca
import utils

def getOptimumPathAlignedPolygonIndices(path):
	implicitGraph = getPossiblePolygonImplicitGraph(path)

	print implicitGraph

	edges = getPossiblePolygonContractedEdges(implicitGraph)

	pv = PathVariance(path)
	

	eweights = [pv.getLineSegmentVariance(i,j) for i,j in edges]

	weightedEdges = [ (i,j,w) for (i,j), w in zip(edges, eweights) ]


	dslwc = DigraphShortestLengthWeightedCycles(weightedEdges, len(path))

	return dslwc.getShortestCyclesSet().pop()

def getOptimumPolygonFromOptAlignedPolygon(optAlignedPolyIndices, path):

	n = len(optAlignedPolyIndices)

	lineIndices = [ (optAlignedPolyIndices[i], optAlignedPolyIndices[(i+1)%n] ) for i in xrange(0,n)]
	linePointRanges = [utils.getCyclicArrayRangeInclusive(lindx[0], lindx[1], path) for lindx in lineIndices]
	principalLines = [pca.getPrincipalComponentLine(lpr) for lpr in linePointRanges] 
	inters = [geometry.getLineIntersection(principalLines[(i-1)%n], principalLines[i]) for i in xrange(0,n)]

	pathPoints = [path[i] for i in optAlignedPolyIndices]
	bestPoints = [getClosestPointToVecOnUnitSquare(sqCenter, vec) for sqCenter, vec in zip(pathPoints, inters)]
	
	return bestPoints



	




	













		














	
