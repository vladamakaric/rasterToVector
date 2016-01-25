from vec2 import *
from collections import deque
import numpy as np

def matrixSize(matrix):
	return len(matrix), len(matrix[0])

def isValidMatrixIndex(rows, cols, j,i):
	return 0 <= j < rows and 0 <= i < cols

def getTupleListFromVec2List(v2list):
	return [(v.x, v.y) for v in v2list]

def getVec2ListFromTupleList(tlist):
	return [Vec2(t[0], t[1]) for t in tlist]

def getIntVec2List(vec2List):
	return [Vec2(int(v.x), int(v.y)) for v in vec2List]

def getCyclicArrayRangeInclusive(start, end, array):
	n = len(array)
	return [array[i] for i in cyclicRange(start, (end+1)%n, n)]

# def getArrayRotatedRight(arr):
# 	adeq = deque(arr)
# 	adeq.rotate(1)
# 	return list(adeq)

def areVecArrsClose(a1, a2):
	if len(a1)!=len(a2): return False

	for v1, v2 in zip(a1,a2):
		if not areVecsClose(v1,v2):
			return False

	return True


def areVecsClose(v1, v2):
	return np.all(np.isclose([v1.x, v1.y], [v2.x, v2.y]))

def arrRotatedLeft(arr):
	n = len(arr)
	for i in range(0, n):
		yield arr[(i+1)%n]

def arrRotatedRight(arr):
	n = len(arr)
	for i in range(0, n):
		yield arr[(i+n-1)%n]


def changeReferencePoint(iterable, newRef):
	return (i - newRef for i in iterable)

def avg(arr):

	if len(arr)==0:
		return None

	sum = arr[0]

	for a in arr[1:]:
		sum+=a

	return sum/len(arr)

def cyclicRange(start, end, modulus):

	current = start

	while True:

		if current == end:
			break

		yield current
		current = (current+1)%modulus
