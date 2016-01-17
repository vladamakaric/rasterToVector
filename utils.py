from vec2 import *

def matrixSize(matrix):
	return len(matrix), len(matrix[0])

def isValidMatrixIndex(rows, cols, j,i):
	return 0 <= j < rows and 0 <= i < cols

def getVec2ListFromTupleList(tlist):
	return [Vec2(t[0], t[1]) for t in tlist]

def getCyclicArrayRangeInclusive(start, end, array):
	n = len(array)
	return [array[i] for i in cyclicRange(start, (end+1)%n, n)]


def cyclicRange(start, end, modulus):

	current = start

	while True:

		if current == end:
			break

		yield current
		current = (current+1)%modulus



