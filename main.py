

from window import Window
from box import Box
import pygame
from window import Text

from ball import Ball


SCORE = 0

pygame.init()

WINDOW = Window("Test Window")

UPPER_BOX = Box(WINDOW.getWidth(), 30)
UPPER_BOX.setColor((128, 128, 128))

TITLE_TEXT = Text("Welcome to Brick Breaker!", 25)
TITLE_TEXT.setPOS(
    (UPPER_BOX.getSurface().get_width() - TITLE_TEXT.getSurface().get_width()) // 2,
    0
)

SCORE_TEXT = Text(f"Score: {SCORE}", 25)
SCORE_TEXT.setPOS(0, 0)
SCORE_TEXT.setColor((255, 0, 0))


BRICK = Box(104.285, 50)
BRICK.setPOS(5, 35)
BRICK.setColor((255, 0, 0))

BRICK2 = Box(104.285, 50)
BRICK2.setPOS(30, 90)
BRICK2.setColor((0, 255, 0))

BRICK3 = Box(104.285, 50)
BRICK3.setPOS(5, 145)
BRICK3.setColor((72, 149, 217))

BRICK4 = Box(104.285, 50)
BRICK4.setPOS(30, 200)
BRICK4.setColor((255, 150, 0))

ROW1 = [BRICK]
ROW2 = [BRICK2]
ROW3 = [BRICK3]
ROW4 = [BRICK4]

ROWS_LIST = [ROW1, ROW3, ROW2, ROW4]


for row in ROWS_LIST:

    for i in range(6):


        row.append(Box(104.285, 50))
        Prev_X = row[-2].getX() + 100
        Prev_y = row[-2].getY()
        row[-1].setPOS(
            Prev_X + 10,
            Prev_y
        )


if __name__ == "__main__":






    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        WINDOW.clearScreen()
        WINDOW.getSurface().blit(UPPER_BOX.getSurface(), UPPER_BOX.getPOS())
        WINDOW.getSurface().blit(TITLE_TEXT.getSurface(), TITLE_TEXT.getPOS())
        WINDOW.getSurface().blit(SCORE_TEXT.getSurface(), SCORE_TEXT.getPOS())
        #WINDOW.getSurface().blit(BRICK.getSurface(), BRICK.getPOS())

        for row in ROWS_LIST:

            for box in row:

                WINDOW.getSurface().blit(box.getSurface(), box.getPOS())

        BALL = Ball(14, 5, WINDOW.getWidth()//2, WINDOW.getHeight()//2, (0, 0, 255))

        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())


        WINDOW.updateFrame()



