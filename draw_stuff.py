import pygame
import os
import time

from my_pygame import *
from my_pazaak import *

SIZE = 1


pygame.init()
pygame.font.init()

NUM_BOARD_CARDSP1: int = 0
NUM_BOARD_CARDSP2: int = 0

BLUEISH: Tuple = (52, 122, 235)
BLACK: Tuple = (0, 0, 0)
RED: Tuple = (180, 20, 5)
FPS: int = 60

BACKG: pygame = pygame.image.load(os.path.join('assets/B.jpg'))
BG: pygame = pygame.transform.scale(BACKG, (900*SIZE, 500*SIZE))

WIDTH: int = 900 * SIZE
HEIGHT: int = 500 * SIZE
#print(WIDTH)
#print(HEIGHT)
WIN: pygame = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my_Pazaak")

MOUSE_X: int = 0
MOUSE_Y: int = 0

P1_CIRCLES: List[Tuple[int]] = [
    (253* SIZE, 24* SIZE), 
    (308* SIZE, 24* SIZE),
    (365* SIZE, 24* SIZE)]

P2_CIRCLES: List[Tuple[int]] = [
    (537* SIZE, 24* SIZE), 
    (593* SIZE, 24* SIZE),
    (649* SIZE, 24* SIZE)]

P2_BOARD_DIS: List[Tuple[int]] = [
    (536* SIZE, 101* SIZE),
    (647* SIZE, 101* SIZE),
    (760* SIZE, 101* SIZE),
    (536* SIZE, 184* SIZE),
    (647* SIZE, 184* SIZE),
    (760* SIZE, 184* SIZE),
    (536* SIZE, 270* SIZE),
    (647* SIZE, 270* SIZE),
    (760* SIZE, 270* SIZE)
]

P1_BOARD_DIS: List[Tuple[int]] = [
    (88* SIZE, 101* SIZE),
    (200* SIZE, 101* SIZE),
    (311* SIZE, 101* SIZE),
    (88* SIZE, 184* SIZE),
    (200* SIZE, 184* SIZE),
    (311* SIZE, 184* SIZE),
    (88* SIZE, 270* SIZE),
    (200* SIZE, 270* SIZE),
    (311* SIZE, 270* SIZE),
]


SIDE_DECK_DIS: List[List[int]] = [
    [45* SIZE, 367* SIZE],
    [153* SIZE, 367* SIZE],
    [250* SIZE, 367* SIZE],
    [355* SIZE, 367* SIZE]]

SIDE_DECK_DIS2: List[List[int]] = [
    [494* SIZE, 367* SIZE],
    [599* SIZE, 367* SIZE],
    [696* SIZE, 367* SIZE],
    [802* SIZE, 367* SIZE]]



def draw_winner(player: int) -> None:
    font = pygame.font.Font(None, 128* SIZE)
    text = font.render("Player" + str(player) + " Wins", True, RED)
    text_rect = text.get_rect(center=(450* SIZE, 100* SIZE))
    WIN.blit(text, text_rect)
    pygame.display.update()
    return None

def get_card(nextCard: int) ->  pygame:
    i: int = -10
    while i < 10:
        if nextCard == i:
            plus: pygame = pygame.image.load(os.path.join('assets/plus' + str(i) + '.png'))
            Plus: pygame = pygame.transform.scale(plus, (52* SIZE, 60* SIZE))
            return Plus
        i += 1

    return None

def draw_window(pazaakGame: PazaakState) -> None:
    i: int = 0

    #WIN.fill(BLUEISH)
    WIN.blit(BG, (0, 0))


    #time.sleep(10)

    font = pygame.font.Font("assets/times.ttf", 32* SIZE)
    #time.sleep(10)
    if pazaakGame.P1stillPlaying == 0:
        S1 = font.render('S', True, RED)
        WIN.blit(S1, ( 185* SIZE, 10* SIZE))
    if pazaakGame.P2stillPlaying == 0:
        S2 = font.render('S', True, RED)
        WIN.blit(S2, ( 700* SIZE, 10* SIZE))

    img = font.render('Player 1', True, BLUEISH)
    WIN.blit(img, (63* SIZE, 10* SIZE))

    img1 = font.render(str(pazaakGame.P1setVal), True, BLUEISH)
    WIN.blit(img1, (400* SIZE, 10* SIZE))

    img2 = font.render('Player 2', True, BLUEISH)
    WIN.blit(img2, (732* SIZE, 10* SIZE))

    img2_1 = font.render(str(pazaakGame.P2setVal), True, BLUEISH)
    WIN.blit(img2_1, (465* SIZE, 10* SIZE))

    radius = 10* SIZE
    i = 0
    while i < pazaakGame.P1gamesWon:
        pygame.draw.circle(WIN, RED, P1_CIRCLES[i], radius)
        i += 1

    i = 0
    while i < pazaakGame.P2gamesWon:
        pygame.draw.circle(WIN, RED, P2_CIRCLES[i], radius)
        i += 1

    
    ET: pygame = pygame.image.load(os.path.join('assets/ET.png'))
    E: pygame = pygame.transform.scale(ET, (140* SIZE, 50* SIZE))
    WIN.blit(E, (380* SIZE, 150* SIZE))

    ET2: pygame = pygame.image.load(os.path.join('assets/ET.png'))
    E2: pygame = pygame.transform.scale(ET2, (140* SIZE, 50* SIZE))
    WIN.blit(E2, (380* SIZE, 250* SIZE))


    font = pygame.font.Font(None, 40* SIZE)
    text = font.render("End Turn", True, BLUEISH)
    text_rect = text.get_rect(center=(450* SIZE, 175* SIZE))
    WIN.blit(text, text_rect)

    font2 = pygame.font.Font(None, 40* SIZE)
    text2 = font2.render("Stand", True, BLUEISH)
    text_rect2 = text2.get_rect(center=(450* SIZE, 275* SIZE))
    WIN.blit(text2, text_rect2)



    pygame.draw.line(WIN, BLACK, (450* SIZE, 150* SIZE), (450* SIZE, 0* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (380* SIZE, 150* SIZE), (520* SIZE, 150* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (380* SIZE, 150* SIZE), (380* SIZE, 200* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (380* SIZE, 200* SIZE), (520* SIZE, 200* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (520* SIZE, 150* SIZE), (520* SIZE, 200* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (450* SIZE, 200* SIZE), (450* SIZE, 250* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (380* SIZE, 300* SIZE), (520* SIZE, 300* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (380* SIZE, 250* SIZE), (380* SIZE, 300* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (380* SIZE, 250* SIZE), (520* SIZE, 250* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (520* SIZE, 250* SIZE), (520* SIZE, 300* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (450* SIZE, 500* SIZE), (450* SIZE, 300* SIZE), 5* SIZE)

    i = 0
    while i < len(pazaakGame.P1boardCards):
        card = get_card(pazaakGame.P1boardCards[i])
        WIN.blit(card, (P1_BOARD_DIS[i]))
        i += 1
    i = 0
    while i < len(pazaakGame.P2boardCards):
        card = get_card(pazaakGame.P2boardCards[i])
        WIN.blit(card, (P2_BOARD_DIS[i]))
        i += 1
    i = 0
    while i < len(SIDE_DECK_DIS):
        new_card = get_card(pazaakGame.P1sideCards[i][0])
        WIN.blit(new_card, (SIDE_DECK_DIS[i]))
        i += 1
    i = 0
    while i < len(SIDE_DECK_DIS2):
        new_card = get_card(pazaakGame.P2sideCards[i][0])
        WIN.blit(new_card, (SIDE_DECK_DIS2[i]))
        i += 1
    pygame.display.update()
    return None
