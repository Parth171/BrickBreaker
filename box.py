"""
title: BOX SUBCLASS
author: Parth Sakpal
date-created: 12/22/2023
"""


from my_sprite import MySprite
import pygame

class Box(MySprite):
    """

    """

    def __init__(self, WIDTH, HEIGHT):
        MySprite.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)


    # --- MODIFIER --- #

    def setColor(self, TUPLE):
        """
        polymorphism
        """
        MySprite.setColor(self, TUPLE)
        self._SURFACE.fill(self._COLOR)

if __name__ == "__main__":

    from window import Window
    pygame.init()

    WINDOW = Window("Boxes subclass")

    RED_BOX = Box(100, 100)
    RED_BOX.setColor((255, 0, 0))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(RED_BOX.getSurface(), RED_BOX.getPOS())
        WINDOW.updateFrame()




