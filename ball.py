
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

        self.__UPPER_HIT_BOX = Box(WIDTH=SIZE, HEIGHT=1)
        self.__UPPER_HIT_BOX.setColor((0, 255, 255))
        self.__UPPER_HIT_BOX.setPOS(self.getX(), self.getY())

        self.__RIGHT_HIT_BOX = Box(WIDTH=1, HEIGHT=SIZE)
        self.__RIGHT_HIT_BOX.setColor((245, 167, 66))
        self.__RIGHT_HIT_BOX.setPOS(self.getX() + self.getSurface().get_width()-1, self.getY())

        self.__POS = (self.__X, self.__Y)



    def updateX(self):

        self.__X = self.__X + (self._X_DIR * self.__SPEED)
        self.__UPPER_HIT_BOX.setPOS(self.__X, self.__Y)
        self.__RIGHT_HIT_BOX.setPOS(self.getX() + self.getSurface().get_width()-1, self.__Y)

        self.__POS = (self.__X, self.__Y)


    def updateY(self):
        self.__Y = self.__Y + (self._Y_DIR * self.__SPEED)
        self.__UPPER_HIT_BOX.setPOS(self.__X, self.__Y)
        self.__RIGHT_HIT_BOX.setPOS(self.getX() + self.getSurface().get_width()-1, self.__Y)

        self.__POS = (self.__X, self.__Y)


    #ACCESSOR METHODS#

    def getPOS(self):
        return self.__POS

    def getUpperHitBox(self):
        return self.__UPPER_HIT_BOX.getSurface()

    def getRightHitBox(self):
        return self.__RIGHT_HIT_BOX.getSurface()

    def getUpperHitBoxPOS(self):
        return self.__UPPER_HIT_BOX.getPOS()

    def getRightHitBoxPOS(self):
        return self.__RIGHT_HIT_BOX.getPOS()



if __name__ == "__main__":
    from window import Window

    WINDOW = Window("BALL TEST")
    pygame.init()

    BALL = Ball(100, 5, 100, 100, (0, 0, 255))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        #BALL.updateX()
        #BALL.updateY()

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())
        WINDOW.getSurface().blit(BALL.getUpperHitBox(), BALL.getUpperHitBoxPOS())
        WINDOW.getSurface().blit(BALL.getRightHitBox(), BALL.getRightHitBoxPOS())

        WINDOW.updateFrame()





