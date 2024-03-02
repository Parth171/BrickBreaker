import pygame.image

from my_sprite import MySprite

class Image(MySprite):
    def __init__(self):
        MySprite.__init__(self)

        self._SURFACE = pygame.image.load("heart_icon.webp")

    def setScale(self, SCALE_X, SCALE_Y=0):
        """
        Adjust the scale of the Image
        :param SCALE_X: Float
        :param SCALE_Y: Float
        :return: None
        """

        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
        self._SURFACE = pygame.transform.scale(self._SURFACE, (
        self._SURFACE.get_width() * SCALE_X, self._SURFACE.get_height() * SCALE_Y))





