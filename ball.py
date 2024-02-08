
from window import Window
import pygame
from my_sprite import MySprite
from box import Box

class Ball(MySprite):

    def __init__(self, SIZE, SPEED, X, Y, COLOR):
        MySprite.__init__(self, WIDTH=SIZE, HEIGHT=SIZE, SPEED=SPEED,X=X, Y=Y, COLOR=COLOR)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)
        self.__SPEED = SPEED
        self._X_DIR = -1
        self._Y_DIR = -1
        self.__X = X
        self.__Y = Y



    def updateX(self):

        self.__X = self.__X + (self._X_DIR * self.__SPEED)

        self.__POS = (self.__X, self.__Y)

    def updateY(self):
        self.__Y = self.__Y + (self._Y_DIR * self.__SPEED)
        self.__POS = (self.__X, self.__Y)

    def getPOS(self):
        return self.__POS




if __name__ == "__main__":
    from window import Window

    WINDOW = Window("BALL TEST")
    pygame.init()

    BALL = Ball(100, 5, 100, 100, (0, 0, 255))

    BOX = Box(100, 50)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()




        BALL.updateX()
        BALL.updateY()

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())

        WINDOW.updateFrame()




