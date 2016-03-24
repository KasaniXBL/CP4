## Lab 4 pt 2


import pygame, sys
from pygame.locals import *

class Character(object):

    def __init__(self, imagename, surf, pos, size): #Classes always need initialization function @ beginning, also always add a self parameter inside a class for a function
        self.SURF = surf
        self.POS = pos #position of image
        self.posx = pos[0]
        self.posy = pos[1]
        self.IMAGESURF = pygame.image.load(imagename)
        self.IMAGESURF = pygame.transform.scale(self.IMAGESURF, (size,size)) #scale image, (size,size) = width height from the characterclass

    def drawImage(self):
        self.SURF.blit(self.IMAGESURF, self.POS) #Draw on DISPLAYSURF, blit = draw

    def move(self):
        self.posx += 1
        self.posy -= 1
        self.POS = (self.posx, self.posy)

    #def move(self):
        #print("Trying to Move")

    #def __init__(self,name): #Classes always need initialization function @ beginning, also always add a self parameter inside a class for a function
        #print(name) 'if char1 in the mainclass file says Character('Mario') prints Mario
