from copy import copy, deepcopy
from collections import deque
import numpy as np

class FloydWarshal:
	def __init__(self, edgeWeightMatrix, inf=np.inf):

		n = edgeWeightMatrix.shape[0]

		currentPredecessors = np.full( (n,n), -1, dtype=np.int64 )

		for i in xrange(0,n):
			for j in xrange(0,n):
				if (i != j and edgeWeightMatrix[i][j] < inf):
					currentPredecessors[i][j] = i
		
		currentPathLengths = edgeWeightMatrix

		for k in xrange(0,n):

			print "FW, iter %d out of %d:" % (k,n) 

			nextPathLengths = np.array(currentPathLengths)
			nextPredecessors = np.array(currentPredecessors)

			for i in xrange(0,n):
				for j in xrange(0,n):

					if (currentPathLengths[i][j] > currentPathLengths[i][k] + currentPathLengths[k][j]):
						nextPathLengths[i][j] = currentPathLengths[i][k] + currentPathLengths[k][j]
						nextPredecessors[i][j] = currentPredecessors[k][j]

			currentPathLengths = nextPathLengths
			currentPredecessors = nextPredecessors

		self.shortestPathLengths = currentPathLengths
		self.predecessors = currentPredecessors

	def isConnected(self, i, j):
		return shortestPathLengths[i][j] != inf


	def getShortestPathLength(self, i,j):
		return self.shortestPathLengths[i][j]

	#prerequisity is that shortest path exists, i.e. shortestPathLengths[i][j] != inf
	def getShortestPathDeque(self, i, j):
		path = deque([j])

		node = j

		while True: 
			node = self.predecessors[i][node]
			path.appendleft(node)

			if node == i:
				break

		return path
