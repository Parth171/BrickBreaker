"""
title: Window class
author: Parth Sakpal
date-created: 12/22/2023
"""

import pygame
from my_sprite import MySprite

class Window:
    """
    creates the window that will load the game
    """

    def __init__(self, TITLE, WIDTH=800, HEIGHT=600, FPS=30):
        self.__TITLE = TITLE
        self.__FPS = FPS
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.__SCREEN_DIM = (self.__WIDTH, self.__HEIGHT)
        self.__CLOCK = pygame.time.Clock()

        self.__SURFACE = pygame.display.set_mode(self.__SCREEN_DIM)

        self.__SURFACE.fill((50, 50, 50))
        pygame.display.set_caption(self.__TITLE)

    def updateFrame(self):
        self.__CLOCK.tick(self.__FPS)
        pygame.display.flip()

    def clearScreen(self):
        self.__SURFACE.fill((50, 50, 50))

    def getSurface(self):
        return self.__SURFACE

    def getWidth(self):
        return self.__WIDTH

    def getHeight(self):
        return self.__HEIGHT


class Text(MySprite):

    """
    creates a text object to put on the screen
    """

    def __init__(self, TEXT, SIZE, COLOR=(255,255,255)):
        MySprite.__init__(self)
        self.__SIZE = SIZE
        self.__TEXT = pygame.font.SysFont("Arial", self.__SIZE)
        self.__SURFACE = self.__TEXT.render(TEXT, 1, COLOR)

    def getSurface(self):
        return self.__SURFACE



if __name__ == "__main__":

    pygame.init()
    WINDOW = Window("A Template", 800, 600, 30)
    TEXT = Text("Hello World")

    while True:

        # teaches pygame to exit when you click on the red "X"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()



        WINDOW.getSurface().blit(TEXT.getSurface(), (0,0))
        WINDOW.updateFrame()