import pygame
import imgUtils

from vec2D import *
from rect import Rect
from grid import Grid
from math import pi
from copy import copy

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

def drawBinImgOnGrid(bimg, grid):
    for j in xrange(0, grid.colNum):
        for i in xrange(0, grid.rowNum):
            topLeft = grid.getTopLeftOfGridCell(i,j)
            
            if bimg[j][i] == 1:
                pygame.draw.rect(screen, BLACK, [topLeft.x, topLeft.y, grid.cellWidth, grid.cellHeight],2)
            
pygame.init()
 
size = [640, 640]
screen = pygame.display.set_mode(size)
 
clock = pygame.time.Clock()
done = False

binImg = imgUtils.getBinImg('img/1.bmp')
biSize = len(binImg), len(binImg[0])

imgGrid = Grid(len(binImg), len(binImg[0]), Rect(Vec2D(0,0), size[0], size[1]))

print imgGrid.getCenterOfGridCell(0,0)

while not done:
 
    clock.tick(100)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True 
 
    screen.fill(WHITE)
    drawBinImgOnGrid(binImg, imgGrid)
    
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
