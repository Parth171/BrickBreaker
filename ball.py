from window import Window
import pygame
from my_sprite import MySprite
from box import Box


class Ball(MySprite):

    def __init__(self, SIZE, SPEED, X, Y, COLOR):
        MySprite.__init__(self, WIDTH=SIZE, HEIGHT=SIZE, SPEED=SPEED, X=X, Y=Y, COLOR=COLOR)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)
        self.__SPEED = SPEED
        self.X_DIR = 1
        self.Y_DIR = -1
        self.X = X
        self.Y = Y

        self.UPPER_HIT_BOX = Box(WIDTH=SIZE, HEIGHT=1)
        self.UPPER_HIT_BOX.setColor((0, 255, 255))
        self.UPPER_HIT_BOX.setPOS(self.getX(), self.getY())

        self.RIGHT_HIT_BOX = Box(WIDTH=1, HEIGHT=SIZE)
        self.RIGHT_HIT_BOX.setColor((245, 167, 66))
        self.RIGHT_HIT_BOX.setPOS(self.getX() + self.getSurface().get_width() - 1, self.getY())

        self.LEFT_HIT_BOX = Box(WIDTH=1, HEIGHT=SIZE)
        self.LEFT_HIT_BOX.setColor((7, 240, 104))
        self.LEFT_HIT_BOX.setPOS(self.getX(), self.getY())

        self.BOTTOM_HIT_BOX = Box(WIDTH=SIZE, HEIGHT=1)
        self.BOTTOM_HIT_BOX.setColor((216, 255, 23))
        self.BOTTOM_HIT_BOX.setPOS(self.getX(), self.getY() + self.getSurface().get_height())

        self.POS = (self.X, self.Y)



    def updateX(self):
        self.X = self.X + (self.X_DIR * self.__SPEED)
        self.UPPER_HIT_BOX.setPOS(self.X, self.Y)
        self.RIGHT_HIT_BOX.setPOS(self.X + self.getSurface().get_width() - 1, self.Y)
        self.LEFT_HIT_BOX.setPOS(self.X, self.Y)
        self.BOTTOM_HIT_BOX.setPOS(self.X, self.Y + self.getSurface().get_height())

        if self.RIGHT_HIT_BOX.getX() + self.RIGHT_HIT_BOX.getSurface().get_width() > 800:
            self.X_DIR = -self.X_DIR

        if self.LEFT_HIT_BOX.getX() < 0:
            self.X_DIR = -self.X_DIR

        self.POS = (self.X, self.Y)

    def updateY(self):
        self.Y = self.Y + (self.Y_DIR * self.__SPEED)
        self.UPPER_HIT_BOX.setPOS(self.X, self.Y)
        self.RIGHT_HIT_BOX.setPOS(self.X + self.getSurface().get_width() - 1, self.Y)
        self.LEFT_HIT_BOX.setPOS(self.X, self.Y)
        self.BOTTOM_HIT_BOX.setPOS(self.X, self.Y + self.getSurface().get_height())

        if self.UPPER_HIT_BOX.getY() < 35:
            self.Y_DIR = -self.Y_DIR

        self.POS = (self.X, self.Y)

    # ACCESSOR METHODS#

    def getPOS(self):
        return self.POS

    # UPPER HIT BOX #
    def getUpperHitBox(self):
        return self.UPPER_HIT_BOX.getSurface()

    def getUpperHitBoxPOS(self):
        return self.UPPER_HIT_BOX.getPOS()

    # RIGHT HIT BOX #

    def getRightHitBox(self):
        return self.RIGHT_HIT_BOX.getSurface()

    def getRightHitBoxPOS(self):
        return self.RIGHT_HIT_BOX.getPOS()

    # LEFT HIT BOX #
    def getLeftHitBox(self):
        return self.LEFT_HIT_BOX.getSurface()

    def getLeftHitBoxPOS(self):
        return self.LEFT_HIT_BOX.getPOS()

    # BOTTOM HIT BOX #

    def getBottomHitBox(self):
        return self.BOTTOM_HIT_BOX.getSurface()

    def getBottomHitBoxPOS(self):
        return self.BOTTOM_HIT_BOX.getPOS()

    def move(self):
        self.updateX()
        self.updateX()


if __name__ == "__main__":
    from window import Window

    WINDOW = Window("BALL TEST")
    pygame.init()

    BALL = Ball(150, 5, 100, 100, (0, 0, 255))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        BALL.updateX()
        BALL.updateY()

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())
        WINDOW.getSurface().blit(BALL.getUpperHitBox(), BALL.getUpperHitBoxPOS())
        WINDOW.getSurface().blit(BALL.getRightHitBox(), BALL.getRightHitBoxPOS())
        WINDOW.getSurface().blit(BALL.getLeftHitBox(), BALL.getLeftHitBoxPOS())
        WINDOW.getSurface().blit(BALL.getBottomHitBox(), BALL.getBottomHitBoxPOS())

        WINDOW.updateFrame()




