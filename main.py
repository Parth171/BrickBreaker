
"""
title: Brick Breaker
Author: Parth Sakpal
Date: 3/2/2024
"""

#IMPORT LIBRARIES

from window import Window
from box import Box
import pygame
from window import Text
from ball import Ball
from paddle import Paddle
from image import Image


# MAIN PROGRAM CODE

if __name__ == "__main__":

    ### INPUTS ###

    # SET UP FOR BRICKS

    BRICK = Box(104.285, 50)
    BRICK.setPOS(5, 35)

    BRICK2 = Box(104.285, 50)
    BRICK2.setPOS(30, 90)

    BRICK3 = Box(104.285, 50)
    BRICK3.setPOS(5, 145)

    BRICK4 = Box(104.285, 50)
    BRICK4.setPOS(30, 200)

    BRICK5 = Box(104.285, 50)
    BRICK5.setPOS(5, 255)

    ROW1 = [BRICK]
    ROW2 = [BRICK2]
    ROW3 = [BRICK3]
    ROW4 = [BRICK4]
    ROW5 = [BRICK5]

    # Row list for both levels
    ROWS_LIST_1 = [ROW1, ROW2, ROW3, ROW4, ROW5]


    for row in ROWS_LIST_1:

        for i in range(6):
            row.append(Box(104.285, 50))
            Prev_X = row[-2].getX() + 100
            Prev_y = row[-2].getY()
            row[-1].setPOS(
                Prev_X + 10,
                Prev_y
            )

    # VARIABLES #
    RUN = 0
    SCORE = 34
    LEVEL_1_LOSS_COUNTER = 0
    HIT_COUNTER = 34

    pygame.init()

    WINDOW = Window("BRICKER BREAKER")

    # 3 Heart Objects
    HEART_1 = Image()
    HEART_2 = Image()
    HEART_3 = Image()

    # Title Bar That will display Score
    UPPER_BOX = Box(WINDOW.getWidth(), 30)
    UPPER_BOX.setColor((128, 128, 128))

    TITLE_TEXT = Text("Welcome to Brick Breaker!", 25)
    TITLE_TEXT.setPOS(
        (UPPER_BOX.getSurface().get_width() - TITLE_TEXT.getSurface().get_width()) // 2,
        0
    )

    USER_TEXT = Text("Use the 'a' and 'd' keys to move the Paddle! Press SPACE to begin!", 20)
    USER_TEXT.setPOS((WINDOW.getSurface().get_width() - USER_TEXT.getSurface().get_width()) // 2,
                     ((WINDOW.getSurface().get_height() - USER_TEXT.getSurface().get_height()) // 2) + 60)

    SCORE_TEXT = Text(f"Score: {SCORE}", 25)
    SCORE_TEXT.setPOS(0, 0)

    HEART_1.setScale(0.07)
    HEART_1.setPOS(
        700,
        (UPPER_BOX.getSurface().get_height() - HEART_1.getSurface().get_height()) // 2
    )

    HEART_2.setScale(0.07)
    HEART_2.setPOS(
        730,
        (UPPER_BOX.getSurface().get_height() - HEART_1.getSurface().get_height()) // 2
    )

    HEART_3.setScale(0.07)
    HEART_3.setPOS(
        760,
        (UPPER_BOX.getSurface().get_height() - HEART_1.getSurface().get_height()) // 2
    )

    # Ball Object
    BALL = Ball(20, 7, (WINDOW.getWidth() // 2) - 5, (WINDOW.getHeight() // 2) + 100, (0, 0, 0))

    # Paddle Object
    PADDLE = Paddle(14)


    ### PROCESSING AND OUTPUTS ###

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Blitting all necessary components
        WINDOW.clearScreen()

        WINDOW.getSurface().blit(UPPER_BOX.getSurface(), UPPER_BOX.getPOS())

        WINDOW.getSurface().blit(HEART_1.getSurface(), HEART_1.getPOS())
        WINDOW.getSurface().blit(HEART_2.getSurface(), HEART_2.getPOS())
        WINDOW.getSurface().blit(HEART_3.getSurface(), HEART_3.getPOS())

        WINDOW.getSurface().blit(TITLE_TEXT.getSurface(), TITLE_TEXT.getPOS())
        WINDOW.getSurface().blit(SCORE_TEXT.getSurface(), SCORE_TEXT.getPOS())

        WINDOW.getSurface().blit(USER_TEXT.getSurface(), USER_TEXT.getPOS())

        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())
        WINDOW.getSurface().blit(PADDLE.getSurface(), PADDLE.getPOS())

        KEYS_PRESSED = pygame.key.get_pressed()

        if HIT_COUNTER == 35:
            """
            Checks if the user has cleared the first Level and sets up the layout of the second level
            """


            BALL = Ball(20, 7, (WINDOW.getWidth() // 2) - 5, (WINDOW.getHeight() // 2) + 100, (0, 0, 0))
            RUN = 0

            BRICK = Box(104.285, 50)
            BRICK.setPOS(5, 35)

            BRICK2 = Box(104.285, 50)
            BRICK2.setPOS(30, 90)

            BRICK3 = Box(104.285, 50)
            BRICK3.setPOS(5, 145)

            BRICK4 = Box(104.285, 50)
            BRICK4.setPOS(30, 200)

            BRICK5 = Box(104.285, 50)
            BRICK5.setPOS(5, 255)

            ROW1 = [BRICK]
            ROW2 = [BRICK2]
            ROW3 = [BRICK3]
            ROW4 = [BRICK4]
            ROW5 = [BRICK5]

            ROWS_LIST_1 = [ROW1, ROW2, ROW3, ROW4, ROW5]

            for row in ROWS_LIST_1:

                for i in range(6):

                    row.append(Box(104.285, 50))
                    Prev_X = row[-2].getX() + 100
                    Prev_y = row[-2].getY()
                    row[-1].setPOS(
                        Prev_X + 10,
                        Prev_y
                    )



            for box in ROW1:
                box.setColor((164, 50, 168))

            for box in ROW2:
                box.setColor((255,255,255))

            for box in ROW3:
                box.setColor((44, 124, 156))

            for box in ROW4:
                box.setColor((24, 252, 3))


            HIT_COUNTER += 1

        if SCORE == 110:
            RUN = 2





        for row in ROWS_LIST_1:
            for box in row:
                """
                Checks if the box has been hit, and sets the box position outside the WINDOW dimensions
                """

                WINDOW.getSurface().blit(box.getSurface(), box.getPOS())

                if BALL.UPPER_HIT_BOX.isCollision(box.getSurface(), box.getPOS()):
                    BALL.Y_DIR = 1



                    SCORE = SCORE + 1
                    SCORE_TEXT = Text(f"Score: {SCORE}", 25)

                    if box._COLOR == (164, 50, 168):
                        box.setColor((44, 124, 156))

                    elif box._COLOR == (44, 124, 156):
                        box.setColor((24, 252, 3))

                    elif box._COLOR == (24, 252, 3):
                        box.setColor((255, 255, 255))

                    elif box._COLOR == (255, 255, 255):
                        box.setPOS(900, 900)
                        HIT_COUNTER += 1


                if BALL.LEFT_HIT_BOX.isCollision(box.getSurface(), box.getPOS()):

                    BALL.X_DIR = 1



                    SCORE += 1
                    SCORE_TEXT = Text(f"Score: {SCORE}", 25)

                    if box._COLOR == (164, 50, 168):
                        box.setColor((44, 124, 156))

                    elif box._COLOR == (44, 124, 156):
                        box.setColor((24, 252, 3))

                    elif box._COLOR == (24, 252, 3):
                        box.setColor((255, 255, 255))

                    elif box._COLOR == (255, 255, 255):
                        box.setPOS(900, 900)
                        HIT_COUNTER += 1

                if BALL.RIGHT_HIT_BOX.isCollision(box.getSurface(), box.getPOS()):



                    BALL.X_DIR = -1

                    SCORE += 1
                    SCORE_TEXT = Text(f"Score: {SCORE}", 25)

                    if box._COLOR == (164, 50, 168):
                        box.setColor((44, 124, 156))

                    elif box._COLOR == (44, 124, 156):
                        box.setColor((24, 252, 3))

                    elif box._COLOR == (24, 252, 3):
                        box.setColor((255, 255, 255))

                    elif box._COLOR == (255, 255, 255):
                        box.setPOS(900, 900)
                        HIT_COUNTER += 1

                if BALL.BOTTOM_HIT_BOX.isCollision(box.getSurface(),
                                                   box.getPOS()) and not BALL.UPPER_HIT_BOX.isCollision(
                        box.getSurface(), box.getPOS()) and not BALL.LEFT_HIT_BOX.isCollision(box.getSurface(),
                                                                                              box.getPOS()) and not BALL.RIGHT_HIT_BOX.isCollision(
                        box.getSurface(), box.getPOS()):

                    box.setPOS(900, 900)

                    BALL.Y_DIR = -BALL.Y_DIR

                    SCORE += 1
                    SCORE_TEXT = Text(f"Score: {SCORE}", 25)

                    if box._COLOR == (164, 50, 168):
                        box.setColor((44, 124, 156))

                    elif box._COLOR == (44, 124, 156):
                        box.setColor((24, 252, 3))

                    elif box._COLOR == (24, 252, 3):
                        box.setColor((255, 255, 255))

                    elif box._COLOR == (255, 255, 255):
                        box.setPOS(900, 900)
                        HIT_COUNTER += 1



        # UPDATES THE LIFE COUNT OF THE USER #

        if BALL.getY() + BALL.getSurface().get_height() > 600:

            RUN = 0
            LEVEL_1_LOSS_COUNTER += 1

            if LEVEL_1_LOSS_COUNTER == 1:
                HEART_1.setPOS(900, 900)

            elif LEVEL_1_LOSS_COUNTER == 2:
                HEART_2.setPOS(900, 900)

            elif LEVEL_1_LOSS_COUNTER == 3:
                HEART_3.setPOS(900, 900)

            elif LEVEL_1_LOSS_COUNTER > 3:

                WINDOW.getSurface().fill((50, 50, 50))

                RUN = 2



        # Start Screen For User #

        if RUN == 0:
            BALL = Ball(20, 7, (WINDOW.getWidth() // 2) - 5, (WINDOW.getHeight() // 2) + 100, (0, 0, 0))

            USER_TEXT.setPOS((WINDOW.getSurface().get_width() - USER_TEXT.getSurface().get_width()) // 2,
                             ((WINDOW.getSurface().get_height() - USER_TEXT.getSurface().get_height()) // 2) + 60)

            PADDLE = Paddle(14)

        # ALLOWS THE GAME TO RUN #
        if RUN == 1:

            USER_TEXT.setPOS(900, 900)

            if BALL.BOTTOM_HIT_BOX.isCollision(PADDLE.getSurface(), PADDLE.getPOS()):
                BALL.Y_DIR = -BALL.Y_DIR
                BALL.X_DIR = PADDLE.DIR

            PADDLE.WASDmove(KEYS_PRESSED)

            BALL.updateX()
            BALL.updateY()



        # END SCREEN FOR USER #
        if RUN == 2:
            WINDOW.getSurface().fill((50, 50, 50))

            for row in ROWS_LIST_1:
                for box in row:
                    box.setPOS(900, 900)

            GAME_END = Text(f"GAME ENDED! SCORE: {SCORE}.", 40, (38, 169, 222))
            THANK_YOU_TEXT = Text("Press ESC to exit. Thanks for playing!", 40, (117, 95, 95))

            GAME_END.setPOS((WINDOW.getSurface().get_width() - GAME_END.getSurface().get_width()) // 2,
                            ((WINDOW.getSurface().get_height() - GAME_END.getSurface().get_height()) // 2) - 25)

            THANK_YOU_TEXT.setPOS((WINDOW.getSurface().get_width() - THANK_YOU_TEXT.getSurface().get_width()) // 2, (
                        WINDOW.getSurface().get_height() - THANK_YOU_TEXT.getSurface().get_height()) // 2 + 100)

            WINDOW.getSurface().blit(GAME_END.getSurface(), GAME_END.getPOS())
            WINDOW.getSurface().blit(THANK_YOU_TEXT.getSurface(), THANK_YOU_TEXT.getPOS())

            if KEYS_PRESSED[pygame.K_ESCAPE] == 1:
                exit()


        if KEYS_PRESSED[pygame.K_SPACE] == 1:
            RUN = 1

        # UPDATES THE WINDOW FRAME #
        WINDOW.updateFrame()

