import numpy as np

from floyd_warshal import *

class DigraphShortestLengthWeightedCycles:
	def __init__(self, weightedEdges, nodeNum):
		inf = LengthWeightMetric.getInf()

		connectionMatrix = np.empty((nodeNum, nodeNum), dtype=object)
		connectionMatrix.fill(inf)

		for weightedEdge in weightedEdges:
			i,j,w = weightedEdge
			connectionMatrix[i][j] = LengthWeightMetric(1,w)

		fw = FloydWarshal(connectionMatrix, inf)
		cycles = set()

		minCycleLength = min([fw.getShortestPathLength(i,i) for i in xrange(0, nodeNum)])
		minCycleIndices = []

		if minCycleLength != inf: 
			minCycleIndices = [i for i in xrange(0, nodeNum) if fw.getShortestPathLength(i,i) == minCycleLength]
			for i in minCycleIndices:
				pathDeuque = fw.getShortestPathDeque(i,i)
				pathDeuque.pop()
				pathDeuque.rotate(-np.argmin(pathDeuque))
				cycles.add(tuple(pathDeuque))

		self.cycles = cycles

	def getShortestCyclesSet(self):
		return self.cycles

class LengthWeightMetric:

	@staticmethod
	def getInf():
		return LengthWeightMetric(np.inf, np.inf)


	def __init__(self, length, weight):
		self.length = length
		self.weight = weight

	def __eq__(self, other):
		return self.length == other.length and self.weight == other.weight

	def __ne__(self, other):
		return not self == other

	def __le__(self, other):
		if self.length == other.length:
			return self.weight <= other.weight

		return self.length < other.length

	def __ge__(self, other):
		return not self < other

	def __gt__(self,other):
		return not self <= other

	def __lt__(self,other):
		return self <= other and not self.__eq__(other)
		
	def __add__(self,other):
		return LengthWeightMetric(self.length + other.length, self.weight + other.weight)
		
		
	


