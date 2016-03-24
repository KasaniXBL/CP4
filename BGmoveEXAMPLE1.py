## BG MOVE EXAMPLE 1, DAY 18

import pygame, sys
from pygame.locals import *
from characterclass import Character

BGimageFileName = 'J0tg59V.png'

pygame.init()
FPSCLOCK = pygame.time.Clock()

FPS = 30
DWIDTH = 1200
DHEIGHT = 800

DISPLAYSURF = pygame.display.set_mode((DWIDTH, DHEIGHT), HWSURFACE | DOUBLEBUF)

BGimage = pygame.image.load(BGimageFileName).convert()
#char1 = Character('mario1.png', DISPLAYSURF, (DWIDTH//2, DHEIGHT//2), 200)

def main():

    x, y = 0, 0
    move_x, move_y = 0, 0


    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

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
            x = 0   #Make X zero, push back to zero
        if y >= 0:
            y = 0
        if x <= -1 * (2000 - DWIDTH):
            x = -1 * (2000 - DWIDTH)
        if y <= -1 * (1100 - DHEIGHT):
            y = -1 * (1100 - DHEIGHT)

        DISPLAYSURF.blit(BGimage, (x,y))
        FPSCLOCK.tick(FPS)

##        if (pygame.key.get_pressed()[pygame.K_w] !=0): #Keyboard input, [pygame press w] !=0 not eq to zero means key pressed down, equal to zero means key not pressed)
##            char1.move()
            
        #char1.drawImage()
        pygame.display.update()

if __name__=="__main__": main ()


