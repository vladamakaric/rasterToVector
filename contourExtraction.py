from vec2 import *
from gridNode import *

def getUpperLeftFilledPixelCoords(binImg):
	cols = len(binImg)
	rows = len(binImg[0])

	for j, row in enumerate(binImg):
		for i, pix in enumerate(row):
			if binImg[j][i] == 1: return Vec2(i,j)


# def extractNodeListFromBinImg(binImg):
#
# 	startCoord = getUpperLeftFilledPixelCoords(binImg)
#
# 	firstNode = GridNode(startCoord)
#
# 	currNode = GridNode(startCoord + Vec2




# def getClosedPathsFromBinImage(binImg):
#
