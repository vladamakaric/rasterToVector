from vec2 import *
import numpy as np
import utils

def _bern3(i,t):
	threeChose_i = 6/(math.factorial(i)*math.factorial(3-i))
	return threeChose_i*( (t**i) * ( (1-t)**(3-i) ) )

def _getPathEndpointTangents(path):
	n = len(path)
	neighborhood = max(n/3,1)

	t1 = utils.avg(list(utils.changeReferencePoint(path[1:1+neighborhood], path[0]))).normalize()
	t2 = utils.avg(list(utils.changeReferencePoint(path[-2:-2-neighborhood:-1], path[-1]))).normalize()
	return t1, t2

def _getCoordLengthParameterization(path):
	pathLen = 0

	coordLenParams = [0]

	for a, b in zip(path[:-1], path[1:]):
		pathLen += (a-b).norm()
		coordLenParams.append(pathLen)

	return [cl/pathLen for cl in coordLenParams]
			
def getBezierFit(t1, t2, points):
	u = _getCoordLengthParameterization(points)[1:-1]

	# u = np.linspace(0,1, num = len(points))[1:-1]

	d = points[1:-1]
	n = len(d)

	V0 = points[0]
	V3 = points[-1]

	A1 = lambda i: t1*_bern3(1, u[i])
	A2 = lambda i: t2*_bern3(2, u[i])

	a = np.zeros((2,2))
	b = np.zeros(2)

	for i in xrange(0,n):
		a[0][0] += A1(i)*A1(i)

		a[0][1] += A1(i)*A2(i)

		a[1][1] += A2(i)*A2(i)

		foo = V0*(_bern3(0, u[i]) + _bern3(1, u[i])) + V3*(_bern3(2, u[i]) + _bern3(3, u[i]))

		b[0] += (d[i] - foo)*A1(i)
		b[1] += (d[i] - foo)*A2(i)

	a[1][0] = a[0][1]

	alpha = np.linalg.solve(a, b)
	
	return V0, V0+t1*alpha[0], V3+t2*alpha[1], V3





	


