from copy import copy, deepcopy


class FloydWarshal:
	def __init__(self, edgeWeightMatrix):

		n = len(edgeWeightMatrix)

		currentPredecessors = [ n*[None] for _ in xrange(0, n) ]

		for i in xrange(0,n):
			for j in xrange(0,n):
				if (i != j and edgeWeightMatrix[i][j] < float("inf")):
					currentPredecessors[i][j] = i

		print currentPredecessors
		
		currentPathLengths = edgeWeightMatrix

		for k in xrange(0,n):
			nextPathLengths = deepcopy(currentPathLengths)
			nextPredecessors = deepcopy(currentPredecessors)

			for i in xrange(0,n):
				for j in xrange(0,n):

					if (currentPathLengths[i][j] > currentPathLengths[i][k] + currentPathLengths[k][j]):
						nextPathLengths[i][j] = currentPathLengths[i][k] + currentPathLengths[k][j]
						nextPredecessors[i][j] = currentPredecessors[k][j]

			currentPathLengths = nextPathLengths
			currentPredecessors = nextPredecessors

		self.shortestPathLengths = currentPathLengths
		self.predecessors = currentPredecessors

	def getShortestPathLenth(self, i,j):
		return shortestPathLengths[i][j]


