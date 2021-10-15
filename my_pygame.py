from sys import breakpointhook
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

P2_BOARD_DIS: List[Tuple[int]] = [
    (720, 60),
    (630, 60),
    (540, 60),
    (720, 150),
    (630, 150),
    (540, 150),
    (720, 240),
    (630, 240),
    (540, 240)
]

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

SIDE_DECK_DIS2: List[Tuple[int]] = [
    (810, 350),
    (720, 350),
    (630, 350),
    (540, 350)]

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
    img2_1 = font.render('Player 2 Set Total: ' + str(pazaakGame.P2setVal), True, BLACK)
    WIN.blit(img2_1, (470, 440))

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

    pygame.draw.line(WIN, BLACK, (450, 200), (450, 300), 5)

    font2 = pygame.font.Font(None, 40)
    text2 = font2.render("Stand", True, BLACK)
    text_rect2 = text2.get_rect(center=(450, 325))
    WIN.blit(text2, text_rect2)
    pygame.draw.line(WIN, BLACK, (380, 350), (520, 350), 5)
    pygame.draw.line(WIN, BLACK, (380, 300), (380, 350), 5)
    pygame.draw.line(WIN, BLACK, (380, 300), (520, 300), 5)
    pygame.draw.line(WIN, BLACK, (520, 300), (520, 350), 5)

    pygame.draw.line(WIN, BLACK, (450, 495), (450, 350), 5)



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


    #WIN.blit(PLUSFIVE, (720, 60))
    #WIN.blit(PLUSFIVE, (630, 60))
    #WIN.blit(PLUSFIVE, (540, 60))
    #WIN.blit(PLUSFIVE, (720, 150))
    #WIN.blit(PLUSFIVE, (630, 150))
    #WIN.blit(PLUSFIVE, (540, 150))
    #WIN.blit(PLUSFIVE, (720, 240))
    #WIN.blit(PLUSFIVE, (630, 240))
    #WIN.blit(PLUSFIVE, (540, 240))
    for card in SIDE_DECK_DIS2:
        WIN.blit(PLUSFIVE, (card))
    #WIN.blit(PLUSFIVE, (810, 350))
    #WIN.blit(PLUSFIVE, (720, 350))
    #WIN.blit(PLUSFIVE, (630, 350))
    #WIN.blit(PLUSFIVE, (540, 350))
    pygame.display.update()
    return None





def quit_game(event: pygame) -> bool:
    if event.type == pygame.QUIT:
        return False
    return True

def player2_AI(pazaakGame: PazaakState, nextCard: int) -> None:
    i: int = 0
    poppedCard: int = 0
    index: int = 0
    lencond: int = len(pazaakGame.P2sideCards)
    if pazaakGame.P2stillPlaying == 1:
        #pazaakGame.P2boardCards.append(nextCard)
        #pazaakGame.P2setVal += nextCard
        if pazaakGame.P2setVal == 20: 
            pazaakGame.P2stillPlaying = 0
            return None
        if monte_carlo_algorithm(pazaakGame) != 1:
            if pazaakGame.P2setVal >= 18: pazaakGame.P2stillPlaying = 0
            while i < lencond:
                i += 1
                if player2_playSideCard(pazaakGame, i-1, index) == 1: 
                    poppedCard = pazaakGame.P2sideCards.pop(i-1)
                    SIDE_DECK_DIS2.pop(i-1)
                    pazaakGame.P2boardCards.append(poppedCard[index])
                    break
                index = 1
                if pazaakGame.P2sideCards[i-1][0] == pazaakGame.P2sideCards[i-1][1]: continue
                if player2_playSideCard(pazaakGame, i-1, index) == 1: 
                    poppedCard = pazaakGame.P2sideCards.pop(i-1)
                    SIDE_DECK_DIS2.pop(i-1)
                    pazaakGame.P2boardCards.append(poppedCard[index])
                    break
    pazaakGame.player = 1 
    return None

def main() -> None:
    clock: pygame = pygame.time.Clock()
    i: int = 0
    run: bool = True
    run2: bool = True


    j: int = 0
    k: int = 2
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
        if k == 1 and pazaakGame.P2stillPlaying == 1: k = 2
        elif k == 2 and pazaakGame.P1stillPlaying == 1: k = 1
        pazaakGame.player = k

        if pazaakGame.player == 1 and pazaakGame.P1stillPlaying == 1:
            pazaakGame.P1boardCards.append(nextCard)
            pazaakGame.P1setVal += nextCard
        if pazaakGame.player == 2 and pazaakGame.P2stillPlaying == 1:
            pazaakGame.P2boardCards.append(nextCard)
            pazaakGame.P2setVal += nextCard
        # time.sleep(3)a
        if pazaakGame.whoWon() == 1 and pazaakGame.P2stillPlaying == 0 and pazaakGame.P1stillPlaying == 0:
            print("p1 won")
            break
        if pazaakGame.whoWon() == 2 and pazaakGame.P2stillPlaying == 0 and pazaakGame.P1stillPlaying == 0:
            print("p2 won")
            break
        if pazaakGame.player == 2:
                #time.sleep(1)
            player2_AI(pazaakGame, 0)
            run2 = False
        else:
            run2 = True
        draw_window(pazaakGame)
        
        while run2: 
            for event in pygame.event.get():
                #time.sleep(1)
                run = run2 = quit_game(event)
                if run2 == False:
                    break
                #time.sleep(2)

                #run = pazaak_main(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()
                    
                    #pazaak_main()

                    #print(MOUSE_X, MOUSE_Y)

    
                    i = 0
                    if pazaakGame.P1stillPlaying == 1:
                        for card in SIDE_DECK_DIS:
                            if card[0] <= int(MOUSE_X) and int(MOUSE_X) <= card[0] + 80:
                                if card[1] <= int(MOUSE_Y) and int(MOUSE_Y) <= card[1] + 80:
                                    SIDE_DECK_DIS.pop(i)
                                    card = pazaakGame.P1sideCards.pop(i)
                                    pazaakGame.P1boardCards.append(card[0])
                                    print(pazaakGame.P1setVal, "   ", card[0])

                                    pazaakGame.P1setVal += card[0]
                                    print(pazaakGame.P1setVal)
                                    draw_window(pazaakGame)

                            i += 1
                    if int(MOUSE_X) <= 520 and int(MOUSE_X) >= 380:
                        if int(MOUSE_Y) <= 350 and int(MOUSE_Y) >= 300:
                            # print('wut')
                            if k == 1:
                                pazaakGame.P1stillPlaying = 0
                            run2 = False
                        if int(MOUSE_Y) <= 200 and int(MOUSE_Y) >= 150:
                            run2 = False

        #time.sleep(2)
        draw_window(pazaakGame)

    pygame.quit()

    return None

if __name__ == "__main__":
    main()
