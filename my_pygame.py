from typing import Tuple
import pygame
import os

WIDTH: int = 900
HEIGHT: int = 500
WIN: pygame = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my_Pazaak")

BLUEISH: Tuple = (52, 122, 235)


FPS: int = 60


CARD5: pygame = pygame.image.load(os.path.join('5card.png'))





def draw_window() -> None:
    WIN.fill(BLUEISH)
    WIN.blit(CARD5, (10, 10))
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
        


        draw_window()

    pygame.quit()

    return None

if __name__ == "__main__":
    main()
