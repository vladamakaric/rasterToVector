import numpy as np
import math

class PathVariance:
	def __init__(self, path):
		self.path = path
		self.n = len(path)
		self.psX = np.zeros(self.n)
		self.psY = np.zeros(self.n)
		self.psXY = np.zeros(self.n)
		self.psYY = np.zeros(self.n)
		self.psXX = np.zeros(self.n)
		
		curpsX = 0
		curpsY = 0
		curpsXX = 0
		curpsXY = 0
		curpsYY = 0

		for i in xrange(0,self.n):
			curpsX += path[i].x
			curpsY += path[i].y
			curpsXX += path[i].x**2
			curpsYY += path[i].y**2
			curpsXY += path[i].x*path[i].y

			self.psX[i] = curpsX
			self.psY[i] = curpsY

			self.psXY[i] = curpsXY
			self.psXX[i] = curpsXX
			self.psYY[i] = curpsYY

	#inclusive range
	def getLineSegmentVariance(self,i,j):

		def getRangeSum(psums, i,j):
			if i==0:
				iEl = psums[i]
			else:
				iEl = psums[i] - psums[i-1]

			if i <= j:
				return psums[j] - psums[i] + iEl
			else: #i>j
				return psums[-1] - psums[i] + psums[j] + iEl
				
		cyclicDiff = j-i + 1

		if i>j:
			cyclicDiff = self.n - i + j + 1

		eX = getRangeSum(self.psX, i, j)/cyclicDiff
		eY = getRangeSum(self.psY, i, j)/cyclicDiff
		eXY = getRangeSum(self.psXY, i, j)/cyclicDiff
		eXX = getRangeSum(self.psXX, i, j)/cyclicDiff
		eYY = getRangeSum(self.psYY, i, j)/cyclicDiff

		v = self.path[j] - self.path[i]
		vbar = (self.path[i] + self.path[j])/2.0

		a = eYY - 2*vbar.y*eY + vbar.y**2
		b = eXY - vbar.x*eY - vbar.y*eX + vbar.x*vbar.y
		c = eXX - 2*vbar.x*eX + vbar.x**2

		return math.sqrt(a*v.x**2 - 2*b*v.x*v.y + c*v.y**2)
