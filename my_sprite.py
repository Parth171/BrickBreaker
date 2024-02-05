
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
        self.__X = X
        self.__Y = Y
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self.__POS = (self.__X, self.__Y)
        self.__SPEED = SPEED
        self._COLOR = COLOR

        self._SURFACE = pygame.Surface # something the child class will have access too

        self.__DIR_X = 1
        self.__DIR_Y = 1


    # --- MODIFIER --- #

    def setX(self, X): # public methods
        self.__X = X
        self.__POS = (self.__X, self.__Y)

    def setY(self, Y):
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)


    def setPOS(self, X, Y):
        self.setX(X)
        self.setY(Y)


    def setColor(self, TUPLE):
        self._COLOR = TUPLE


    # --- ACCESSOR --- #


    def getSurface(self):
        return self._SURFACE

    def getPOS(self):
        return self.__POS
