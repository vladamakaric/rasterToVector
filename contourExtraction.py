from vec2 import *
from gridNode import *
from utils import *

def getUpperLeftFilledPixelCoords(binImg):
	cols = len(binImg)
	rows = len(binImg[0])

	for j, row in enumerate(binImg):
		for i, pix in enumerate(row):
			if binImg[j][i] == 1: return Vec2(i,j)

# def getClosedPathsFromBinImage(binImg):

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


def getNormalizedNeighborhoodNextDir(neighborhood):
	if neighborhood[0][0] == 0: return Vec2(-1, 0)
	if neighborhood[0][1] == 0: return Vec2(0, 1)
	return Vec2(1,0)

def getNextPathDir(binImg, currentCoord, prevCoord):
	direction = currentCoord - prevCoord

	neighborhood = get4PixelNeighborhood(binImg, currentCoord)

	neighborhood = normalize4PixelNeighborhood(neighborhood, direction)
	
	normNextDir = getNormalizedNeighborhoodNextDir(neighborhood)

	return denormalizeNextDirection(direction, normNextDir)

def denormalizeNextDirection(direction, newDirectionNormalized):
	yaxis = direction
	xaxis = direction.perpCW()

def normalize4PixelNeighborhood(neighborhood, direction):
	yaxis = direction
	xaxis = direction.perpCW()

	print yaxis, xaxis

	neighborCoords = [Vec2(0,0), Vec2(1,0), Vec2(1,1), Vec2(0,1)]
	neighborCornerCenterCoords = [Vec2(-1,1), Vec2(1,1), Vec2(1,-1), Vec2(-1,-1)]

	offset = Vec2(1,-1)

	normalizedNeighborCoords = ( (offset + v.x*xaxis + v.y*yaxis)/2 for v in neighborCornerCenterCoords) 
	normalizedNeighborhood = [[0,0], [0,0]]

	for nc, nnc in zip(neighborCoords, normalizedNeighborCoords):
		normalizedNeighborhood[nc.y][nc.x] = neighborhood[nnc.y][nnc.x]

	return tuple(normalizedNeighborhood[0]), tuple(normalizedNeighborhood[1])

def get4PixelNeighborhood(binImg, coord):
	cols = len(binImg)
	rows = len(binImg[0])

	neighborhood = [[0,0], [0,0]]

	directions = [Vec2(0,0), Vec2(-1,0), Vec2(0,-1), Vec2(-1,-1)]
	neighborCoords = (coord + vec for vec in directions)

	def isFilled(nc): return isValidMatrixIndex(rows, cols, nc.y, nc.x) and binImg[nc.y][nc.x]==1
	
	filledNeighborCoords = (nc for nc in neighborCoords if isFilled(nc))

	for relativeCoord in (nc - (coord + Vec2(-1,-1)) for nc in filledNeighborCoords):
		neighborhood[relativeCoord.y][relativeCoord.x] = 1
			
	return tuple(neighborhood[0]), tuple(neighborhood[1])

def getNextPathDir(binImg, currentCoord, prevCoord):
	neighborhood = get4PixelNeighborhood(binImg, currentCoord)
	direction = currentCoord - prevCoord

