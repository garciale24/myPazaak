from typing import Tuple
import pygame
import os

WIDTH: int = 900
HEIGHT: int = 500
WIN: pygame = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my_Pazaak")

BLUEISH: Tuple = (52, 122, 235)
BLACK: Tuple = (0, 0, 0)

FPS: int = 60


CARD5: pygame = pygame.image.load(os.path.join('5card.png'))
CARDFIVE: pygame = pygame.transform.scale(CARD5, (80, 80))




def draw_window() -> None:
    WIN.fill(BLUEISH)
    pygame.draw.line(WIN, BLACK, (450, 495), (450, 5), 10)
    WIN.blit(CARDFIVE, (100, 10))
    WIN.blit(CARDFIVE, (190, 10))
    WIN.blit(CARDFIVE, (280, 10))
    WIN.blit(CARDFIVE, (100, 100))
    WIN.blit(CARDFIVE, (190, 100))
    WIN.blit(CARDFIVE, (280, 100))
    WIN.blit(CARDFIVE, (100, 190))
    WIN.blit(CARDFIVE, (190, 190))
    WIN.blit(CARDFIVE, (280, 190))

    WIN.blit(CARDFIVE, (10, 300))
    WIN.blit(CARDFIVE, (100, 300))
    WIN.blit(CARDFIVE, (190, 300))
    WIN.blit(CARDFIVE, (280, 300))


    WIN.blit(CARDFIVE, (720, 10))
    WIN.blit(CARDFIVE, (630, 10))
    WIN.blit(CARDFIVE, (540, 10))
    WIN.blit(CARDFIVE, (720, 100))
    WIN.blit(CARDFIVE, (630, 100))
    WIN.blit(CARDFIVE, (540, 100))
    WIN.blit(CARDFIVE, (720, 190))
    WIN.blit(CARDFIVE, (630, 190))
    WIN.blit(CARDFIVE, (540, 190))

    WIN.blit(CARDFIVE, (810, 300))
    WIN.blit(CARDFIVE, (720, 300))
    WIN.blit(CARDFIVE, (630, 300))
    WIN.blit(CARDFIVE, (540, 300))
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
