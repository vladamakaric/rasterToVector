from vec2 import *
import numpy as np
import utils
import bezier_curve

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

def _computeMaxErrorSq(innerPoints, bezCP, innerParams):
	maxDist = 0.0
	splitPoint = len(innerPoints)/2 + 1
	for i, (point, u) in enumerate(zip(innerPoints, innerParams)):
		dist = (bezier_curve.Q(bezCP, u) - point).normSq()

		if dist > maxDist:
			maxDist = dist
			splitPoint = i

	return maxDist, splitPoint+1

def getBezierFit(t1, t2, points, eps=2, psy=15, iterNum=15):
	innerPointsParams = _getCoordLengthParameterization(points)[1:-1]
	bezCP = _getBezierFitParameterized(t1, t2, points, innerPointsParams)
	innerPoints = points[1:-1]

	errSq, splitIndex = _computeMaxErrorSq(innerPoints, bezCP, innerPointsParams)
	print errSq

	if errSq < eps**2:
		return [bezCP]

	if errSq < psy**2:
		for i in xrange(0,iterNum):
			innerPointsParams = [_getImprovedPointParam(bezCP, p, t) for  p,t in zip(points[1:-1], innerPointsParams)] 
			bezCP = _getBezierFitParameterized(t1, t2, points, innerPointsParams)
			errSq, splitIndex = _computeMaxErrorSq(innerPoints, bezCP, innerPointsParams)
			print errSq

			if errSq < eps**2:
				return [bezCP]

	return [bezCP]

def _getImprovedPointParam(bezCP, point, t):
	Q = bezier_curve.Q(bezCP, t)
	dQ = bezier_curve.dQ(bezCP, t)
	dQ2 = bezier_curve.dQ2(bezCP, t)

	nom = (Q - point)*dQ
	denom = dQ*dQ + (Q - point)*dQ2

	if denom == 0:
		return t
	else:
		return t - nom/denom



def _getBezierFitParameterized(t1, t2, points, innerPointsParams):
	u = innerPointsParams

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
