import numpy as np

from floyd_warshal import *

class DigraphShortestCycles:
	def __init__(self, edges, nodeNum):
		connectionMatrix = np.full((nodeNum,nodeNum), np.inf)

		for edge in edges:
			i,j = edge
			connectionMatrix[i][j] = 1

		fw = FloydWarshal(connectionMatrix)
		cycles = set()

		for i in xrange(0, nodeNum):
			pathDeuque = fw.getShortestPathDeque(i,i)
			pathDeuque.pop()
			pathDeuque.rotate(-np.argmin(pathDeuque))
			cycles.add(tuple(pathDeuque))

		self.cycles = cycles

	def getShortestCyclesSet(self):
		return self.cycles


		








