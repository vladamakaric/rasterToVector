import numpy as np
from vec2 import *
from scipy import linalg as la
from line import *


def getPrincipalComponentLine(vec2Array):
	xs = np.array([v.x for v in vec2Array])
	ys = np.array([v.y for v in vec2Array])

	origin = Vec2(np.mean(xs), np.mean(ys))

	C = np.cov(xs - origin.x, ys - origin.y)

	evals, evecs = la.eig(C)

	dir =  evecs[:,np.argmax(evals)]

	return Line(origin, Vec2(dir[0], dir[1]))








