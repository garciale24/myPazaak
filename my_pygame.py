from typing import Any, Tuple
import pygame
import os
import time
from my_pazaak import *

from typing import List




pygame.init()
pygame.font.init()

NUM_BOARD_CARDSP1: int = 0
NUM_BOARD_CARDSP2: int = 0

WIDTH: int = 900
HEIGHT: int = 500
WIN: pygame = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my_Pazaak")

BLUEISH: Tuple = (52, 122, 235)
BLACK: Tuple = (0, 0, 0)
RED: Tuple = (180, 20, 5)
FPS: int = 60

PLUS5: pygame = pygame.image.load(os.path.join('5card.png'))
PLUSFIVE: pygame = pygame.transform.scale(PLUS5, (80, 80))

MOUSE_X: int = 0
MOUSE_Y: int = 0



P1_BOARD_DIS: List[Tuple[int]] = [
    (100, 60),
    (190, 60),
    (280, 60),
    (100, 150),
    (190, 150),
    (280, 150),
    (100, 240),
    (190, 240),
    (280, 240),
]


SIDE_DECK_DIS: List[Tuple[int]] = [
    (10, 350),
    (100, 350),
    (190, 350),
    (280, 350)]

def get_card(nextCard: int) ->  pygame:
    if nextCard < 100:
        P5: pygame = pygame.image.load(os.path.join('5card.png'))
        PFIVE: pygame = pygame.transform.scale(P5, (80, 80))
    return PFIVE

def draw_window(pazaakGame: PazaakState) -> None:
    i: int = 0



    WIN.fill(BLUEISH)

    #time.sleep(10)

    font = pygame.font.Font("times.ttf", 32)
    #time.sleep(10)

    img = font.render('Player 1: Human', True, BLACK)
    WIN.blit(img, (20, 20))

    img1 = font.render('Player 1 Set Total: ' + str(pazaakGame.P1setVal), True, BLACK)
    WIN.blit(img1, (20, 440))

    img2 = font.render('Player 2: A.I.', True, BLACK)
    WIN.blit(img2, (470, 20))

    radius = 15
    pygame.draw.circle(WIN, RED, (50, 135), radius)
    pygame.draw.circle(WIN, RED, (50, 180), radius)
    pygame.draw.circle(WIN, RED, (50, 225), radius)

    pygame.draw.circle(WIN, RED, (850, 135), radius)
    pygame.draw.circle(WIN, RED, (850, 180), radius)
    pygame.draw.circle(WIN, RED, (850, 225), radius)

    pygame.draw.line(WIN, BLACK, (450, 150), (450, 5), 5)

    font = pygame.font.Font(None, 40)
    text = font.render("End Turn", True, BLACK)
    text_rect = text.get_rect(center=(450, 175))
    WIN.blit(text, text_rect)
    pygame.draw.line(WIN, BLACK, (380, 150), (520, 150), 5)
    pygame.draw.line(WIN, BLACK, (380, 150), (380, 200), 5)
    pygame.draw.line(WIN, BLACK, (380, 200), (520, 200), 5)
    pygame.draw.line(WIN, BLACK, (520, 150), (520, 200), 5)



    pygame.draw.line(WIN, BLACK, (450, 495), (450, 350), 5)


    while i < len(pazaakGame.P1boardCards):
        card = get_card(pazaakGame.P1boardCards[i])
        WIN.blit(card, (P1_BOARD_DIS[i]))
        i += 1


    #WIN.blit(PLUSFIVE, (100, 60))
    #WIN.blit(PLUSFIVE, (190, 60))
    #WIN.blit(PLUSFIVE, (280, 60))
    #WIN.blit(PLUSFIVE, (100, 150))
    #WIN.blit(PLUSFIVE, (190, 150))
    #WIN.blit(PLUSFIVE, (280, 150))
    #WIN.blit(PLUSFIVE, (100, 240))
    #WIN.blit(PLUSFIVE, (190, 240))
    #WIN.blit(PLUSFIVE, (280, 240))



    for card in SIDE_DECK_DIS:
        WIN.blit(PLUSFIVE, (card))
    #WIN.blit(PLUSFIVE, (100, 350))
    #WIN.blit(PLUSFIVE, (190, 350))
    #WIN.blit(PLUSFIVE, (280, 350))


    WIN.blit(PLUSFIVE, (720, 60))
    WIN.blit(PLUSFIVE, (630, 60))
    WIN.blit(PLUSFIVE, (540, 60))
    WIN.blit(PLUSFIVE, (720, 150))
    WIN.blit(PLUSFIVE, (630, 150))
    WIN.blit(PLUSFIVE, (540, 150))
    WIN.blit(PLUSFIVE, (720, 240))
    WIN.blit(PLUSFIVE, (630, 240))
    WIN.blit(PLUSFIVE, (540, 240))

    WIN.blit(PLUSFIVE, (810, 350))
    WIN.blit(PLUSFIVE, (720, 350))
    WIN.blit(PLUSFIVE, (630, 350))
    WIN.blit(PLUSFIVE, (540, 350))
    pygame.display.update()
    return None





def quit_game(event: pygame) -> bool:
    if event.type == pygame.QUIT:
        return False
    return True


def main() -> None:
    clock: pygame = pygame.time.Clock()
    i: int = 0
    run: bool = True
    run2: bool = True


    j: int = 0
    k: int = 1
    p1wins: int = 0
    p2wins: int = 0
    pazaakGame = PazaakState(k)


    ties: int = 0
    pazaakGame.createSideDeck(pazaakGame.P1sideCards)
    pazaakGame.createSideDeck(pazaakGame.P2sideCards)
    pazaakGame.player = k



    while run:
        clock.tick(FPS)
        nextCard: int = pazaakGame.nextCard()

        if pazaakGame.player == 1:
            pazaakGame.P1boardCards.append(nextCard)
            pazaakGame.P1setVal += nextCard
        draw_window(pazaakGame)

        # time.sleep(3)

        run2 = True
        while run2: 
            for event in pygame.event.get():
                #time.sleep(1)
                run = run2 = quit_game(event)
                #time.sleep(2)

                #run = pazaak_main(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
                    
                    #pazaak_main()

                    #print(MOUSE_X, MOUSE_Y)

                    i = 0
                    for card in SIDE_DECK_DIS:
                        if card[0] <= int(MOUSE_X) and int(MOUSE_X) <= card[0] + 80:
                            if card[1] <= int(MOUSE_Y) and int(MOUSE_Y) <= card[1] + 80:
                                SIDE_DECK_DIS.pop(i)
                                run2 = False

                        i += 1
                    if int(MOUSE_X) <= 520 and int(MOUSE_X) >= 380:
                        if int(MOUSE_Y) <= 200 and int(MOUSE_Y) >= 150:
                            run2 = False
        #time.sleep(2)
        draw_window(pazaakGame)

    pygame.quit()

    return None

if __name__ == "__main__":
    main()
