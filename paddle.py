
from my_sprite import MySprite
import pygame


class Paddle(MySprite):

    def __init__(self,SPEED,X=0, Y=550):
        MySprite.__init__(self, WIDTH=150, HEIGHT=7, SPEED=SPEED)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)

        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32)
        self._SURFACE.fill(self._COLOR)
        self.__SPEED = SPEED
        self.X = X
        self.Y = Y
        self.POS = (self.X, self.Y)
        self.DIR = 1


        self.setPOS(400 - self.getSurface().get_width()//2,
        550)


    def WASDmove(self, KEY_PRESSES):

        """
        move the box based on WASD
        :param KEY_PRESSES: list[int]
        :return:
        """



        if KEY_PRESSES[pygame.K_d] == 1:
            self.X = self.X + self.__SPEED
            self.DIR = 1

        if KEY_PRESSES[pygame.K_a] == 1:
            self.X = self.X - self.__SPEED
            self.DIR = -1



        if self.X < 0:
            self.X = 0

        if self.X + self.getSurface().get_width() > 800:
            self.X = 800 - self.getSurface().get_width()



        self.POS = (self.X, self.Y)


if __name__ == "__main__":

    from window import Window

    WINDOW = Window("PADDLE TEST")
    pygame.init()

    PADDLE = Paddle(10)



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        KEYS_PRESSED = pygame.key.get_pressed()

        PADDLE.WASDmove(KEYS_PRESSED)

        WINDOW.clearScreen()
        WINDOW.getSurface().blit(PADDLE.getSurface(), PADDLE.getPOS())
        WINDOW.updateFrame()

