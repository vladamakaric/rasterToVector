import numpy as np
from line import *
from vec2 import *
from line_segment import *

def getLineIntersection(l1, l2):
	A = np.array([[-l1.dir.x, l2.dir.x] , [-l1.dir.y, l2.dir.y]]) 
	b = np.array([l1.origin.x - l2.origin.x, l1.origin.y - l2.origin.y])

	if np.linalg.matrix_rank(A) != 2:
		return None

	solution = np.linalg.inv(A).dot(b)

	return l1.origin + solution[0]*l1.dir

#assume line dir is normalized
def getVec2ToLineDistance(v, l):
	perpDir = l.dir.perpCW()
	relToOrig = v - l.origin
	proj = relToOrig*perpDir

	return np.fabs(proj)
	
def getVec2ToLineDistanceSq(v, l):
	return getVec2ToLineDistance(v,l)**2

def getLineSegmentIntersection(ls1, ls2):
	line1 = Line.createFrom2Endpoints(ls1.a, ls1.b)
	line2 = Line.createFrom2Endpoints(ls2.a, ls2.b)
	inter = getLineIntersection(line1, line2)

	if inter == None:
		return None

	if ls1.isVecProjectionBetweenEndPoints(inter) and ls2.isVecProjectionBetweenEndPoints(inter):
		return inter
	else:
		return None

def getLineLineSegmentIntersection(line, lineSegment):
	lsLine = Line.createFrom2Endpoints(lineSegment.a, lineSegment.b)

	inter = getLineIntersection(lsLine, line)

	if inter == None or not lineSegment.isVecProjectionBetweenEndPoints(inter):
		return None

	return inter

def getClosestPointToVecOnUnitSquare(sqCenter, vec):

	xleft = sqCenter.x - 0.5
	xright = sqCenter.x + 0.5

	ytop = sqCenter.y + 0.5
	ybottom = sqCenter.y - 0.5

	if xleft <= vec.x <= xright and ybottom <= vec.y <= ytop:
		return vec

	hLine = Line(vec, Vec2(1,0))
	vLine = Line(vec, Vec2(0,1))

	eps = [Vec2(xleft, ytop),
          Vec2(xright, ytop),
          Vec2(xright, ybottom),
          Vec2(xleft, ybottom)]

	hlss = [LineSegment(eps[0], eps[1]), LineSegment(eps[3], eps[2])]
	vlss = [LineSegment(eps[1], eps[2]), LineSegment(eps[0], eps[3])]

	hinters = [getLineLineSegmentIntersection(vLine, hlss[0]), getLineLineSegmentIntersection(vLine, hlss[1])]
	vinters = [getLineLineSegmentIntersection(hLine, vlss[0]), getLineLineSegmentIntersection(hLine, vlss[1])]

	inters = hinters+vinters
	inters = [i for i in inters if i != None]

	inters += eps

	return min(inters, key=lambda i: (vec - i).normSq())
