from typing import Tuple
import pygame
import os
import time

WIDTH: int = 900
HEIGHT: int = 500
WIN: pygame = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my_Pazaak")

BLUEISH: Tuple = (52, 122, 235)
BLACK: Tuple = (0, 0, 0)
RED: Tuple = (180, 20, 5)
FPS: int = 60


CARD5: pygame = pygame.image.load(os.path.join('5card.png'))
CARDFIVE: pygame = pygame.transform.scale(CARD5, (80, 80))

pygame.init()
pygame.font.init()



def draw_window() -> None:
    WIN.fill(BLUEISH)

    #time.sleep(10)

    font = pygame.font.SysFont(None, 32)
    #time.sleep(10)

    img = font.render('Player 1: Human', False, BLACK)
    WIN.blit(img, (20, 20))

    img2 = font.render('Player 2: A.I.', False, BLACK)
    WIN.blit(img2, (470, 20))

    radius = 15
    pygame.draw.circle(WIN, RED, (50, 135), radius)
    pygame.draw.circle(WIN, RED, (50, 180), radius)
    pygame.draw.circle(WIN, RED, (50, 225), radius)

    pygame.draw.circle(WIN, RED, (850, 135), radius)
    pygame.draw.circle(WIN, RED, (850, 180), radius)
    pygame.draw.circle(WIN, RED, (850, 225), radius)

    pygame.draw.line(WIN, BLACK, (450, 495), (450, 5), 10)
    WIN.blit(CARDFIVE, (100, 60))
    WIN.blit(CARDFIVE, (190, 60))
    WIN.blit(CARDFIVE, (280, 60))
    WIN.blit(CARDFIVE, (100, 150))
    WIN.blit(CARDFIVE, (190, 150))
    WIN.blit(CARDFIVE, (280, 150))
    WIN.blit(CARDFIVE, (100, 240))
    WIN.blit(CARDFIVE, (190, 240))
    WIN.blit(CARDFIVE, (280, 240))

    WIN.blit(CARDFIVE, (10, 350))
    WIN.blit(CARDFIVE, (100, 350))
    WIN.blit(CARDFIVE, (190, 350))
    WIN.blit(CARDFIVE, (280, 350))


    WIN.blit(CARDFIVE, (720, 60))
    WIN.blit(CARDFIVE, (630, 60))
    WIN.blit(CARDFIVE, (540, 60))
    WIN.blit(CARDFIVE, (720, 150))
    WIN.blit(CARDFIVE, (630, 150))
    WIN.blit(CARDFIVE, (540, 150))
    WIN.blit(CARDFIVE, (720, 240))
    WIN.blit(CARDFIVE, (630, 240))
    WIN.blit(CARDFIVE, (540, 240))

    WIN.blit(CARDFIVE, (810, 350))
    WIN.blit(CARDFIVE, (720, 350))
    WIN.blit(CARDFIVE, (630, 350))
    WIN.blit(CARDFIVE, (540, 350))
    pygame.display.update()
    return None

def main() -> None:
    clock: pygame = pygame.time.Clock()
    run: bool = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # print("hello")
                pass

        draw_window()

    pygame.quit()

    return None

if __name__ == "__main__":
    main()
