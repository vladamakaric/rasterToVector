from vec2 import *
import copy


class Grid:
	def __init__(self, rowNum, colNum, rect): 
		self.rowNum = rowNum
		self.colNum = colNum
		self.rect = rect

		self.cellWidth = float(rect.width)/colNum
		self.cellHeight = float(rect.height)/rowNum

	def getCenterOfGridCell(self,i,j):
		realCoord = Vec2(i*self.cellWidth,j*self.cellHeight)
		return self.rect.topLeft + realCoord + Vec2(self.cellWidth, self.cellHeight)/2.0

	def getTopLeftOfGridCell(self,i,j):
		realCoord = Vec2(i*self.cellWidth,j*self.cellHeight)
		return self.rect.topLeft + realCoord 
