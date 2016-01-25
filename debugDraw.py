import pygame
import pygame.gfxdraw
import imgUtils
from utils import *

from vec2 import *
from rect import Rect
from grid import Grid
from math import pi
from copy import copy

import contour_extraction
import optimal_polygon

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

def drawBinImgOnGrid(bimg, grid):
    for j in xrange(0, grid.rowNum):
        for i in xrange(0, grid.colNum):
            topLeft = grid.getTopLeftOfGridCell(i,j)
            
            if bimg[j][i] == 1:
                pygame.draw.rect(screen, BLACK, [topLeft.x, topLeft.y, grid.cellWidth, grid.cellHeight],2)
           
def drawPolygon(poly, grid, color):
    for a,b in zip(poly, arrRotatedRight(poly)):
        pygame.draw.line(screen, color, (a.x*grid.cellWidth, a.y*grid.cellHeight), (b.x*grid.cellWidth, b.y*grid.cellHeight))

pygame.init()
 
size = [640, 640]
screen = pygame.display.set_mode(size)
 
clock = pygame.time.Clock()
done = False

binImg = imgUtils.getBinImg('img/5.png')
biSize = len(binImg), len(binImg[0])

imgGrid = Grid(len(binImg), len(binImg[0]), Rect(Vec2(0,0), size[0], size[1]))

path = contour_extraction.extractShapeContourPathFromBinImg(binImg)
poly = optimal_polygon.getOptimalPolygonFromPath(path)


while not done:
 
    clock.tick(100)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True 

 
    screen.fill(WHITE)
    drawBinImgOnGrid(binImg, imgGrid)

    pygame.gfxdraw.bezier(screen, [(0,0), (100,0), (320,640), (0,640)], 30, RED)

    drawPolygon(poly, imgGrid, RED)
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
