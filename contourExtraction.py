from vec2 import *
from gridNode import *
from utils import *

def getUpperLeftFilledPixelCoords(binImg):
	cols = len(binImg)
	rows = len(binImg[0])

	for j, row in enumerate(binImg):
		for i, pix in enumerate(row):
			if binImg[j][i] == 1: return Vec2(i,j)


# def extractShapeContourPathFromBinImg(binImg):
#
# 	startCoord = getUpperLeftFilledPixelCoords(binImg)
# 	prevCoord = startCoord
# 	currentCoord = startCoord + Vec2(0,1)
#
# 	# every path starts downward on the left edge of the first pixel
# 	path = [startCoord]
#
# 	while currentCoord != startCoord
# 		path.append(currentCoord)
# 		moveDir = getNextPathDir(binImg, currentCoord, prevCoord)
# 		prevCoord = currentCoord
# 		currentCoord += moveDir
#

# def getClosedPathsFromBinImage(binImg):
#

def get4PixelNeighborhood(binImg, coord):
	cols = len(binImg)
	rows = len(binImg[0])

	neighborhood = [[0,0], [0,0]]

	directions = [Vec2(0,0), Vec2(-1,0), Vec2(0,-1), Vec2(-1,-1)]
	neighborCoords = (coord + vec for vec in directions)
	filledNeighborCoords = (nc for nc in neighborCoords if isValidMatrixIndex(binImg, nc.y, nc.x) and binImg[nc.y][nc.x]==1)

	for relativeCoord in (nc - (coord + Vec2(-1,-1)) for nc in filledNeighborCoords):
		neighborhood[relativeCoord.y][relativeCoord.x] = 1
			
	return neighborhood


	
	
	
