from typing import Any, Tuple
import pygame
import os
import time
from my_pazaak import *

from typing import List

SIZE = 2


pygame.init()
pygame.font.init()

NUM_BOARD_CARDSP1: int = 0
NUM_BOARD_CARDSP2: int = 0

BLUEISH: Tuple = (52, 122, 235)
BLACK: Tuple = (0, 0, 0)
RED: Tuple = (180, 20, 5)
FPS: int = 1

BACKG: pygame = pygame.image.load(os.path.join('B.jpg'))
BG: pygame = pygame.transform.scale(BACKG, (900*SIZE, 500*SIZE))

WIDTH: int = 900 * SIZE
HEIGHT: int = 500 * SIZE
#print(WIDTH)
#print(HEIGHT)
WIN: pygame = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my_Pazaak")

MOUSE_X: int = 0
MOUSE_Y: int = 0

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

def get_card(nextCard: int) ->  pygame:
    i: int = -10
    while i < 10:
        if nextCard == i:
            plus: pygame = pygame.image.load(os.path.join('plus' + str(i) + '.png'))
            Plus: pygame = pygame.transform.scale(plus, (52* SIZE, 60* SIZE))
            return Plus
        i += 1

    return None

def draw_window(pazaakGame: PazaakState) -> None:
    i: int = 0

    #WIN.fill(BLUEISH)
    WIN.blit(BG, (0, 0))


    #time.sleep(10)

    font = pygame.font.Font("times.ttf", 32* SIZE)
    #time.sleep(10)

    img = font.render('Player 1', True, BLUEISH)
    WIN.blit(img, (63* SIZE, 10* SIZE))

    img1 = font.render(str(pazaakGame.P1setVal), True, BLUEISH)
    WIN.blit(img1, (400* SIZE, 10* SIZE))

    img2 = font.render('Player 2', True, BLUEISH)
    WIN.blit(img2, (732* SIZE, 10* SIZE))

    img2_1 = font.render(str(pazaakGame.P2setVal), True, BLUEISH)
    WIN.blit(img2_1, (465* SIZE, 10* SIZE))

    radius = 10* SIZE
    pygame.draw.circle(WIN, RED, (253* SIZE, 24* SIZE), radius)
    pygame.draw.circle(WIN, RED, (308* SIZE, 24* SIZE), radius)
    pygame.draw.circle(WIN, RED, (365* SIZE, 24* SIZE), radius)

    pygame.draw.circle(WIN, RED, (537* SIZE, 24* SIZE), radius)
    pygame.draw.circle(WIN, RED, (593* SIZE, 24* SIZE), radius)
    pygame.draw.circle(WIN, RED, (649* SIZE, 24* SIZE), radius)

    
    ET: pygame = pygame.image.load(os.path.join('ET.png'))
    E: pygame = pygame.transform.scale(ET, (140* SIZE, 50* SIZE))
    WIN.blit(E, (380* SIZE, 150* SIZE))

    ET2: pygame = pygame.image.load(os.path.join('ET.png'))
    E2: pygame = pygame.transform.scale(ET2, (140* SIZE, 50* SIZE))
    WIN.blit(E2, (380* SIZE, 250* SIZE))

    pygame.draw.line(WIN, BLACK, (450* SIZE, 150* SIZE), (450* SIZE, 5* SIZE), 5* SIZE)

    font = pygame.font.Font(None, 40* SIZE)
    text = font.render("End Turn", True, BLUEISH)
    text_rect = text.get_rect(center=(450* SIZE, 175* SIZE))
    WIN.blit(text, text_rect)

    pygame.draw.line(WIN, BLACK, (380* SIZE, 150* SIZE), (520* SIZE, 150* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (380* SIZE, 150* SIZE), (380* SIZE, 200* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (380* SIZE, 200* SIZE), (520* SIZE, 200* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (520* SIZE, 150* SIZE), (520* SIZE, 200* SIZE), 5* SIZE)

    pygame.draw.line(WIN, BLACK, (450* SIZE, 200* SIZE), (450* SIZE, 250* SIZE), 5* SIZE)

    font2 = pygame.font.Font(None, 40* SIZE)
    text2 = font2.render("Stand", True, BLUEISH)
    text_rect2 = text2.get_rect(center=(450* SIZE, 275* SIZE))
    WIN.blit(text2, text_rect2)
    pygame.draw.line(WIN, BLACK, (380* SIZE, 300* SIZE), (520* SIZE, 300* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (380* SIZE, 250* SIZE), (380* SIZE, 300* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (380* SIZE, 250* SIZE), (520* SIZE, 250* SIZE), 5* SIZE)
    pygame.draw.line(WIN, BLACK, (520* SIZE, 250* SIZE), (520* SIZE, 300* SIZE), 5* SIZE)

    pygame.draw.line(WIN, BLACK, (450* SIZE, 495* SIZE), (450* SIZE, 300* SIZE), 5* SIZE)



    i = 0
    while i < len(pazaakGame.P1boardCards):
        #card: pygame = None
        card = get_card(pazaakGame.P1boardCards[i])
        WIN.blit(card, (P1_BOARD_DIS[i]))
        i += 1


    i = 0
    while i < len(pazaakGame.P2boardCards):
        #print(pazaakGame.P2boardCards[i])
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


    i = 0
    while i < len(SIDE_DECK_DIS):
        #print(card[0])
        new_card = get_card(pazaakGame.P1sideCards[i][0])
        WIN.blit(new_card, (SIDE_DECK_DIS[i]))
        i += 1
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
    i = 0
    while i < len(SIDE_DECK_DIS2):
        #print(card[0])
        new_card = get_card(pazaakGame.P2sideCards[i][0])
        WIN.blit(new_card, (SIDE_DECK_DIS2[i]))
        i += 1
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
            if pazaakGame.P2setVal >= 18: 
                pazaakGame.P2stillPlaying = 0
            if pazaakGame.P2setVal > pazaakGame.P1setVal:
                print("yoooooo")
                if pazaakGame.P1stillPlaying == 0: 
                    print("wtf")
                    pazaakGame.P2stillPlaying == 0
                    return None
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
    pick_card: bool = True

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


        # time.sleep(3)a
        if pazaakGame.whoWon() == 1:
            print("p1 won")
            break
        if pazaakGame.whoWon() == 2:
            print("p2 won")
            break
        if pazaakGame.whoWon() == -1:
            print("tie")
            break

        if pazaakGame.player == 1 and pazaakGame.P1stillPlaying == 1:
            pazaakGame.P1boardCards.append(nextCard)
            pazaakGame.P1setVal += nextCard
        if pazaakGame.player == 2 and pazaakGame.P2stillPlaying == 1:
            pazaakGame.P2boardCards.append(nextCard)
            pazaakGame.P2setVal += nextCard
        for event in pygame.event.get():
            run = quit_game(event)
        if pazaakGame.player == 2:
            player2_AI(pazaakGame, 0)
            run2 = False
        else:
            run2 = True
        draw_window(pazaakGame)
        for event in pygame.event.get():
            run = quit_game(event)
        pick_card = True

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

                    print(MOUSE_X, MOUSE_Y)


                    i = 0
                    if pazaakGame.P1stillPlaying == 1 and pick_card:
                        for card in SIDE_DECK_DIS:
                            if card[0] <= int(MOUSE_X) and int(MOUSE_X) <= card[0] + 52* SIZE:
                                if card[1] <= int(MOUSE_Y) and int(MOUSE_Y) <= card[1] + 60* SIZE:
                                    SIDE_DECK_DIS.pop(i)
                                    card = pazaakGame.P1sideCards.pop(i)
                                    pazaakGame.P1boardCards.append(card[0])
                                    print(pazaakGame.P1setVal, "   ", card[0])

                                    pazaakGame.P1setVal += card[0]
                                    print(pazaakGame.P1setVal)
                                    draw_window(pazaakGame)
                                    pick_card = False
                                    #run2 = False
                                    #break

                            i += 1
                    if int(MOUSE_X) <= 520* SIZE and int(MOUSE_X) >= 380* SIZE:
                        if int(MOUSE_Y) <= 300* SIZE and int(MOUSE_Y) >= 250* SIZE:
                            # print('wut')
                            if k == 1:
                                pazaakGame.P1stillPlaying = 0
                            run2 = False
                        if int(MOUSE_Y) <= 200* SIZE and int(MOUSE_Y) >= 150* SIZE:
                            run2 = False

        #time.sleep(2)
        draw_window(pazaakGame)
    draw_window(pazaakGame)
    #time.sleep(5)
    pygame.quit()

    return None

if __name__ == "__main__":
    main()
