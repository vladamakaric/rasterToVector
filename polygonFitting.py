from vec2 import *


#is a<=b<=c, ordered modulo n
def cyclicLinearOrder(a,b,c):
	if a<=c:
		return a<=b and b<=c
	else:
		return a<=b or b<=c

def getPositiveAndNegativeConstraintDelta(delta):
	pos = delta.perpCW().normalizeCoordinatewise()
	neg = -pos

	if pos.y == 0 or pos.x == 0:
		deltaUnit = delta.normalizeCoordinatewise()
		pos -= deltaUnit
		neg -= deltaUnit

	return pos, neg

def updateAngleConstraints(posAngleConstraint, negAngleConstraint, delta):
	posDelta, negDelta = getPositiveAndNegativeConstraintDelta(delta)
	
	newPAC = delta + posDelta
	newNAC = delta + negDelta

	if posAngleConstraint.cross(newPAC) < 0:
		newPAC = posAngleConstraint

	if negAngleConstraint.cross(newNAC) > 0:
		newNAC = negAngleConstraint

	return newPAC, newNAC


def getPossiblePolygonImplicitGraph(path):

	n = len(path)
	lastIndex = n*[0]

	for startIndex in xrange(n-1, -1, -1):

		print  "Start index ", startIndex

		nextIndex = (startIndex+2)%n

		negAngleConstraint = Vec2(0,0)
		posAngleConstraint = Vec2(0,0)

		#directions in current path from start index
		directions = set()
		directions.add(path[(startIndex+1)%n] - path[startIndex])

		while nextIndex!=startIndex:

			if startIndex < n-1 and not cyclicLinearOrder(startIndex, nextIndex, lastIndex[startIndex+1]):
				print "cycle"
				break
			
			direction = path[nextIndex] - path[(nextIndex-1)%n]

			directions.add(direction)

			if len(directions) == 4:
				print "dir"
				break

		 	delta = path[nextIndex] - path[startIndex] 

			if negAngleConstraint.cross(delta) > 0 or posAngleConstraint.cross(delta) < 0:
				print "angleC"
				break

			if abs(delta.x) >1 or abs(delta.y) >1:
				
				posAngleConstraint, negAngleConstraint = updateAngleConstraints(
					posAngleConstraint,	negAngleConstraint, delta)

			nextIndex = (nextIndex+1)%n


		lastIndex[startIndex] = (nextIndex-1)%n


	return lastIndex


		









