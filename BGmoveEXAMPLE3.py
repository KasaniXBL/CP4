## BG MOVE EXAMPLE 1, DAY 18

import pygame, sys
from pygame.locals import *

BGimageFileName = 'J0tg59V.png'

pygame.init()
FPSCLOCK = pygame.time.Clock()

FPS = 30
DWIDTH = 1920
DHEIGHT = 1080

DISPLAYSURF = pygame.display.set_mode((DWIDTH, DHEIGHT), HWSURFACE|DOUBLEBUF)

BGimage = pygame.image.load(BGimageFileName).convert()

def main():

    x,y = 0,0
    move_x, move_y = 0,0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    while True:

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -10
            elif event.key == K_RIGHT:
                move_x = +10
            elif event.key == K_UP:
                move_y = +10
            elif event.key == K_DOWN:
                move_y = -10
                
            
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0
            elif event.key == K_RIGHT:
                move_x = 0
            elif event.key == K_UP:
                move_y = 0
            elif event.key == K_DOWN:
                move_y = 0

        x += move_x
        y += move_y


        # Makes it impossible to go display with the image
        if x >= 0:
            #DISPLAYSURF.blit(BGimage, (x - BGx, y))
            x = 0   #Make X zero, push back to zero
        if y >= 0:
            #DISPLAYSURF.blit(BGimage, (x, y - BGy))
            y = 0
        if x <= -1 * (2000 - DWIDTH):
        #if x <= -1 * (BGx - DWIDTH):
            #DISPLAYSURF.blit(BGimage, (x + BGx, y))
            x = -1 * (2000 - DWIDTH)
        if y <= -1 * (1100 - DHEIGHT):
        #if y <= -1 * (BGy - DHEIGHT):
            #DISPLAYSURF.blit(BGimage, (x, y + BGx))
            y = -1 * (1100 - DHEIGHT)

##        if x >= 0 and y >= 0:
##            DISPLAYSURF.blit(BGimage, (x - BGx, y - BGy))
##        if x <= -1 * (BGx - DWIDTH) and y <= -1 * 

        DISPLAYSURF.blit(BGimage, (x,y))
        FPSCLOCK.tick(FPS)

        pygame.display.update()

if __name__=="__main__": main ()
