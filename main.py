
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


BRICK = Box(100, 50)
BRICK.setPOS(5, 35)

ROW = []

for i in range(7):
    ROW.append(BRICK)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    WINDOW.clearScreen()
    WINDOW.getSurface().blit(UPPER_BOX.getSurface(), UPPER_BOX.getPOS())
    WINDOW.getSurface().blit(TITLE_TEXT.getSurface(), TITLE_TEXT.getPOS())
    WINDOW.getSurface().blit(SCORE_TEXT.getSurface(), SCORE_TEXT.getPOS())

    WINDOW.updateFrame()
