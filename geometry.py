import numpy as np

def getLineIntersection(l1, l2):
	A = np.array([[-l1.dir.x, l2.dir.x] , [-l1.dir.y, l2.dir.y]]) 
	b = np.array([l1.origin.x - l2.origin.x, l1.origin.y - l2.origin.y])

	if np.linalg.matrix_rank(A) != 2:
		return None

	solution = np.linalg.inv(A).dot(b)

	return l1.origin + solution[0]*l1.dir
