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
import polygon_curve_fit

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

binImg = imgUtils.getBinImg('img/7.png')
biSize = len(binImg), len(binImg[0])

imgGrid = Grid(len(binImg), len(binImg[0]), Rect(Vec2(0,0), size[0], size[1]))

path = contour_extraction.extractShapeContourPathFromBinImg(binImg)
poly = optimal_polygon.getOptimalPolygonFromPath(path)

poly2 = [ Vec2(v.x*imgGrid.cellWidth, v.y*imgGrid.cellHeight) for v in poly ]

def postProcessPolygon(poly):
    n = len(poly)
    lens = 0.0
    for i in xrange(0,n):
        lens += (poly[i]-poly[(i+1)%n]).norm()

    avg = lens/n


    newPoly = []
    for i in xrange(0,n):
        newPoly.append(poly[i])
        l = (poly[i]-poly[(i+1)%n]).norm()

        if l > avg:
            newPoly.append((poly[i] + poly[(i+1)%n])/2.0)

    return newPoly

bCurves = polygon_curve_fit.getPolygonBezierCurveList(postProcessPolygon(poly2))

state = 0

numStates = 2
while not done:
 
    clock.tick(100)
     
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                state= (state-1)%numStates
            if event.key == pygame.K_RIGHT:
                state= (state+1)%numStates
        if event.type == pygame.QUIT:
            done=True 
 
    screen.fill(WHITE)

    if state==1:
        drawBinImgOnGrid(binImg, imgGrid)
        drawPolygon(poly, imgGrid, RED)

    if state==0:
        for bezCP in bCurves: 
            pygame.gfxdraw.bezier(screen, getTupleListFromVec2List(bezCP), 30, GREEN)

    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
