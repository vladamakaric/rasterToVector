import math
import bezier_fit
from utils import *

def _getPolygonCorners(poly, thresh=0.4):

	n = len(poly)

	corners = []

	for i in xrange(0,n):
		side1 = poly[(i+1)%n]
		side2 = poly[(i-1)%n]
		middle = poly[i]

		v1 = (side1 - middle).normalize()
		v2 = (side2 - middle).normalize()

		if math.fabs(v1*v2) < thresh:
			corners.append(i)

	return corners

def getPolygonBezierCurveList(poly):
	corners = _getPolygonCorners(poly)
	n = len(corners)

	bcurves = []

	for i in xrange(0,n):
		polyLine = getCyclicArrayRangeInclusive(corners[i], corners[(i+1)%n], poly)
		bcurves += bezier_fit.getBezierCurveListToFitPoints(polyLine)

	return bcurves


