import math
import bezier_fit
from utils import *

def _getPolygonCorners(poly, thresh=0.1):

	n = len(poly)

	corners = []

	for i in xrange(0,n):
		side1 = poly[(i+1)%n]
		side2 = poly[(i-1)%n]
		middle = poly[i]

		v1 = (side1 - middle).normalize()
		v2 = (side2 - middle).normalize()

                if v1*v2 >= 0 or (v1*v2 < 0 and v1*v2> -thresh):
			corners.append(i)

	return corners

def getLeftTangent(poly, i):
	n = len(poly)
	return (poly[(i-1)%n] - poly[(i+1)%n]).normalize()

def getPolygonBezierCurveList(poly):
	corners = _getPolygonCorners(poly)
	ncorns = len(corners)

	bcurves = []
	n = len(poly)

	if ncorns == 0:
		print "ZURKA2"
		tl = getLeftTangent(poly, 0)
		tl2 = getLeftTangent(poly, n/2)

		bcurves += bezier_fit.getBezierCurveListToFitPoints(poly[0: 1 + n/2], -tl, tl2)
		bcurves += bezier_fit.getBezierCurveListToFitPoints(poly[n/2 : n] + [poly[0]], -tl2, tl)
		return bcurves
		
	if ncorns ==1:
		print "ZURKA"

		endp = (corners[0] + n/2)%n

		tl = getLeftTangent(poly, endp)

		polyLine = getCyclicArrayRangeInclusive(corners[0], endp, poly)

		bcurves+= bezier_fit.getBezierCurveListToFitPoints(polyLine, None, tl)
		polyLine = getCyclicArrayRangeInclusive(endp, corners[0], poly)
		bcurves+= bezier_fit.getBezierCurveListToFitPoints(polyLine, -tl)
		return bcurves

	for i in xrange(0,ncorns):
		polyLine = getCyclicArrayRangeInclusive(corners[i], corners[(i+1)%ncorns], poly)
		bcurves += bezier_fit.getBezierCurveListToFitPoints(polyLine)

	return bcurves


