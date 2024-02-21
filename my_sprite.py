
"""
title: Parent Class
author: Parth Sakpal
date-created: 12/22/2023
"""

import pygame

class MySprite:

    """
    abstract sprite class for Pygame sprites. Abstract because it doesn't run by itself


    public:
    partially_protect:
    private:
    """

    def __init__(self, WIDTH=1, HEIGHT=1, X=0, Y=0, SPEED=5, COLOR=(255, 255, 255)):

        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.X = X
        self.Y = Y
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self.POS = (self.X, self.Y)
        self.__SPEED = SPEED
        self._COLOR = COLOR

        self._SURFACE = pygame.Surface # something the child class will have access too

        self.__DIR_X = 1
        self.__DIR_Y = 1


    # --- MODIFIER --- #

    def setX(self, X): # public methods
        self.X = X
        self.POS = (self.X, self.Y)

    def setY(self, Y):
        self.Y = Y
        self.POS = (self.X, self.Y)


    def setPOS(self, X, Y):
        self.setX(X)
        self.setY(Y)


    def setColor(self, TUPLE):
        self._COLOR = TUPLE


    def isCollision(self, SURFACE:pygame.Surface, POS):


        WIDTH = SURFACE.get_width()
        HEIGHT = SURFACE.get_height()
        X = POS[0]
        Y = POS[1]

        if X >= self.X - WIDTH and X <= self.X + self._SURFACE.get_width():
            if Y >= self.Y - HEIGHT and Y <= self.Y + self._SURFACE.get_height():
                return True

        return False

    # --- ACCESSOR --- #


    def getSurface(self):
        return self._SURFACE

    def getPOS(self):
        return self.POS

    def getX(self):
        return self.X

    def getY(self):
        return self.Y
