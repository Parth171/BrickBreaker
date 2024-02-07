
from window import Window
from box import Box
import pygame
from window import Text


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


ROW1 = [BRICK]
ROW2 = [BRICK2]
ROW3 = [BRICK3]




for i in range(4):

    "ROW" + "f{i}".append(Box(104.285, 50))



    """ROW2.append(Box(104.285, 50))
    Prev_X = ROW2[-2].getX() + 100
    Prev_y = ROW2[-2].getY()
    ROW2[-1].setPOS(
        Prev_X + 10,
        Prev_y
    )"""





print(WINDOW.getWidth() - ROW1[-1].getX())
print(WINDOW.getHeight())

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



    for box in ROW1:
        WINDOW.getSurface().blit(box.getSurface(), box.getPOS())

    for box in ROW2:
        WINDOW.getSurface().blit(box.getSurface(), box.getPOS())



    WINDOW.updateFrame()
