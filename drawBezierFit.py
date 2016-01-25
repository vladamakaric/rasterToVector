import pygame
import pygame.gfxdraw
from utils import *

import bezier_fit
import bezier_curve

from vec2 import *
from math import pi
from copy import copy
import numpy as np

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

pygame.init()

size = [800, 640]
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
done = False

def drawVector(origin, vec, color):
    pygame.draw.line(screen, color, (origin.x, origin.y), (origin.x + vec.x, origin.y + vec.y))

def drawPoints(points, color):
	for p in points:
		pygame.draw.circle(screen, color, (p.x, p.y), 5, 0)

def discretizeBezierCurve(bezCP, pointNum):
	return [bezier_curve.Q(bezCP, t) for t in np.linspace(0, 1, num=pointNum)]


def drawBezierCurve(bezCP, pointNum, color):
	drawPoints(getIntVec2List(discretizeBezierCurve(bezCP, pointNum)), color)

points = getVec2ListFromTupleList([
	(20, 20),
	(93, 53),
	(232, 89),
	(323, 131),
	(371, 212),
	(457, 275),
	(571, 293),
	(673, 298)])

angles = np.linspace(np.pi, 0, num=10)

r = 300
tuples = zip( 300 + r*np.cos(angles), 300 + r*np.sin(angles) )

# halfCircle = getVec2ListFromTupleList(tuples)
# halfCBez = bezier_fit.getBezierFit(Vec2(0,1), Vec2(0,1), halfCircle)
# halfCircle = getIntVec2List(halfCircle)

bez2 = [Vec2(0,0), Vec2(0,300), Vec2(400,300), Vec2(400,0)]

pnum = 4

bez2RefP = discretizeBezierCurve(bez2, pnum)
beziers = bezier_fit.getBezierFit(Vec2(0,1), Vec2(0,1), bez2RefP)

# t1, t2 = bezier_fit._getPathEndpointTangents(points)
# bez = bezier_fit.getBezierFit(t1,t2,points)


while not done:

	clock.tick(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True 

	screen.fill(WHITE)


	drawBezierCurve(bez2, pnum, BLUE)

	for bezCP in beziers: 
		pygame.gfxdraw.bezier(screen, getTupleListFromVec2List(bezCP), 30, RED)

	# drawPoints(points, BLUE)
	# drawPoints(halfCircle, RED)
	# pygame.gfxdraw.bezier(screen, getTupleListFromVec2List(halfCBez), 30, RED)
	# pygame.gfxdraw.bezier(screen, [(0,0), (100,0), (320,640), (0,640)], 30, RED)

	# pygame.gfxdraw.bezier(screen, getTupleListFromVec2List(bez), 30, RED)
	# drawBezierCurve(halfCBez, 10, BLUE)

	# drawVector(points[0], t1*100, GREEN)
	# drawVector(points[-1], t2*100, GREEN)

	pygame.display.flip()

# Be IDLE friendly
pygame.quit()
