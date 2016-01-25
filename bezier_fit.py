from vec2 import *
import numpy as np
import utils
import bezier_curve

def getBezierCurveListToFitPoints(points, t1=None, t2=None):
	if t1==None:
		t1 = (points[1] - points[0]).normalize()
		t2 = (points[-2] - points[-1]).normalize()
	elif t2==None:
		t2 = (points[-2] - points[-1]).normalize()

	points = _getProcessedPoints(t1, t2, points)

	return _getBezierFit(t1,t2, points)

def bern3(i,t):
	threeChose_i = 6/(math.factorial(i)*math.factorial(3-i))
	return threeChose_i*( (t**i) * ( (1-t)**(3-i) ) )

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


def _getBezierFit(t1, t2, points, eps=2, psy=15, iterNum=15):

	innerPointsParams = _getCoordLengthParameterization(points)[1:-1]
	bezCP = _getBezierFitParameterized(t1, t2, points, innerPointsParams)
	innerPoints = points[1:-1]

	errSq, splitIndex = _computeMaxErrorSq(innerPoints, bezCP, innerPointsParams)

	if errSq < eps**2:
		return [bezCP]

	if errSq < psy**2:
		for i in xrange(0,iterNum):
			innerPointsParams = [_getImprovedPointParam(bezCP, p, t) for  p,t in zip(innerPoints, innerPointsParams)] 
			bezCP = _getBezierFitParameterized(t1, t2, points, innerPointsParams)
			errSq, splitIndex = _computeMaxErrorSq(innerPoints, bezCP, innerPointsParams)

			if errSq < eps**2:
				return [bezCP]

	if len(points)==4:
		return [bezCP]

	beziers = []
	lpts, rpts, splitTan = _getLeftAndRightPointsAndLeftCenterTangent(t1,t2, points, splitIndex)

	beziers += _getBezierFit(t1, splitTan, lpts)
	beziers += _getBezierFit(-splitTan, t2, rpts)
	return beziers

def _getFirstPartOfSplitTangent(points, splitIndex):
	return (points[splitIndex-1] - points[splitIndex+1]).normalize()

def _getLeftAndRightPointsAndLeftCenterTangent(t1, t2, points, splitIndex):
	n = len(points)
	print n

	if 0 >=  splitIndex or splitIndex >= n-1:
		splitIndex = n/2

	leftTangnt = _getFirstPartOfSplitTangent(points, splitIndex)

	lpoints = _getProcessedPoints(t1, leftTangnt, points[:splitIndex+1])
	rpoints = _getProcessedPoints(-leftTangnt, t2, points[splitIndex:])

	return lpoints, rpoints, leftTangnt
	
def _getProcessedPoints(t1, t2, points):

	if len(points) > 3:
		return points

	newPts = [None]*4

	if len(points) == 2:
		dist = (points[0] - points[1]).norm()
		newPts[0] = points[0]
		newPts[1] = points[0] + t1*dist*0.25
		newPts[2] = points[1] + t2*dist*0.25
		newPts[3] = points[1]
	elif len(points) == 3:
		midpoint = points[1]
		lToM = midpoint - points[0]
		rToM = midpoint - points[2]
		newPts[0] = points[0]
		newPts[1] = points[0] + lToM*0.9
		newPts[2] = points[2] + rToM*0.9
		newPts[3] = points[2]

	return newPts

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

	A1 = lambda i: t1*bern3(1, u[i])
	A2 = lambda i: t2*bern3(2, u[i])

	a = np.zeros((2,2))
	b = np.zeros(2)

	for i in xrange(0,n):
		a[0][0] += A1(i)*A1(i)

		a[0][1] += A1(i)*A2(i)

		a[1][1] += A2(i)*A2(i)

		foo = V0*(bern3(0, u[i]) + bern3(1, u[i])) + V3*(bern3(2, u[i]) + bern3(3, u[i]))

		b[0] += (d[i] - foo)*A1(i)
		b[1] += (d[i] - foo)*A2(i)

	a[1][0] = a[0][1]

	alpha = np.linalg.solve(a, b)
	return V0, V0+t1*alpha[0], V3+t2*alpha[1], V3
