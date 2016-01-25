import math
from vec2 import *

def bern3(i,t):
	threeChose_i = 6/(math.factorial(i)*math.factorial(3-i))
	return threeChose_i*( (t**i) * ( (1-t)**(3-i) ) )

def Q(P, t):
	point = Vec2(0,0)

	for i, cp in enumerate(P):
		point+=P[i]*bern3(i,t)

	return point

def dQ(P, t):
	return 3*(1-t)**2 * (P[1] - P[0]) + 6*(1-t)*t*(P[2]-P[1]) + 3*t**2 * (P[3] - P[2])

def dQ2(P, t):
	return 6*(1-t)*(P[2] - 2*P[1] + P[0]) + 6*t*(P[3] - 2*P[2] + P[1])
