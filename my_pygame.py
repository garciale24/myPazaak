from typing import Any, Tuple
import pygame
import os
import time
from my_pazaak import *

from draw_stuff import *
from typing import List



def quit_game(event: pygame) -> bool:
    if event.type == pygame.QUIT:
        return False
    return True

def player2_AI(pazaakGame: PazaakState, nextCard: int) -> bool:
    i: int = 0
    poppedCard: int = 0
    index: int = 0
    lencond: int = len(SIDE_DECK_DIS2)
    if pazaakGame.P2stillPlaying == 1:
        if pazaakGame.P2setVal == 20: 
            pazaakGame.P2stillPlaying = 0
            return True
        if monte_carlo_algorithm(pazaakGame) != 1:
            if pazaakGame.P2setVal >= 18 and pazaakGame.P2setVal <= 20: 
                pazaakGame.P2stillPlaying = 0
            if pazaakGame.P2setVal > pazaakGame.P1setVal:
                if pazaakGame.P1stillPlaying == 0: 
                    pazaakGame.P2stillPlaying == 0
                    return True
            i = 0
            best = -1
            bestidx = 0
            lencond = len(SIDE_DECK_DIS2)
            while i < lencond:
                i += 1
                if player2_playSideCard(pazaakGame, i-1, index) == 1: 
                    if pazaakGame.P2setVal > best:
                        best = pazaakGame.P2setValTemp
                        bestidx = i
                index = 1
                if pazaakGame.P2sideCards[i-1][0] == pazaakGame.P2sideCards[i-1][index]: continue
                if player2_playSideCard(pazaakGame, i-1, index) == 1: 
                    if pazaakGame.P2setVal > best:
                        best = pazaakGame.P2setValTemp
                        bestidx = i
            if best != -1:
                if pazaakGame.P1stillPlaying == 0:
                    if best > pazaakGame.P1setVal:
                        poppedCard = pazaakGame.P2sideCards.pop(bestidx-1)
                        SIDE_DECK_DIS2.pop(bestidx-1)
                        pazaakGame.P2boardCards.append(poppedCard[index])
                        pazaakGame.P2setVal = best
                        pazaakGame.P2stillPlaying = 0
                        if wait_timer(1) == False:
                            return False
                else:
                    poppedCard = pazaakGame.P2sideCards.pop(bestidx-1)
                    SIDE_DECK_DIS2.pop(bestidx-1)
                    pazaakGame.P2boardCards.append(poppedCard[index])
                    pazaakGame.P2setVal = best
                    pazaakGame.P2stillPlaying = 0
                    if wait_timer(1) == False:
                        return False
    #pazaakGame.player = 1 
    return True

def wait_timer(multiplier: int) -> bool:
    run3: bool = True
    run3= True
    st = pygame.time.get_ticks()
    while run3:
        for event in pygame.event.get():
            if quit_game(event) == False: 
                return False
        et = pygame.time.get_ticks()
        if et - st >= 1000*multiplier:
            run3 = False
    return True


def main() -> None:
    clock: pygame = pygame.time.Clock()
    i: int = 0
    exxxit: bool = True
    run: bool = True
    run2: bool = True

    pick_card: bool = True
    et: int = 0
    st: int = 0
    j: int = 0
    k: int = 2
    p1wins: int = 0
    p2wins: int = 0
    pazaakGame = PazaakState(k)
    pazaakGame.createSideDeck(pazaakGame.P1sideCards)
    pazaakGame.createSideDeck(pazaakGame.P2sideCards)
    draw_window(pazaakGame)
    k = 2
    rounds_checker = 1
    rounds_flag = 0
    ties: int = 0

    #pazaakGame.P1gamesWon = 3
    while (pazaakGame.P1gamesWon < 3) and (pazaakGame.P2gamesWon < 3) and exxxit:
        pazaakGame.reset()
        i = 0
        pazaakGame.P2setVal = 19

        run = run2 = pick_card = True

        pazaakGame.player = k
        for event in pygame.event.get():
            exxxit = quit_game(event)


        while run:
            clock.tick(FPS)
            #draw_window(pazaakGame)
            x = wait_timer(1) 
            if x == False: break
            draw_window(pazaakGame)

            nextCard: int = pazaakGame.nextCard()
            print(k)
            if rounds_flag == 0:
                if k == 1: 
                    k = 2
                elif k == 2: 
                    k = 1
                pazaakGame.player = k
            else:
                rounds_flag = 0
                pazaakGame.player = rounds_checker
            print(pazaakGame.player, "playerrr")

            # time.sleep(3)a
            if pazaakGame.whoWon() == 1:
                pazaakGame.P1gamesWon += 1
                print("p1 won")
                #draw_winner(1)
                if rounds_checker == 1: 
                    rounds_checker = 2
                elif rounds_checker == 2: 
                    rounds_checker = 1
                pazaakGame.player = rounds_checker
                rounds_flag=1
                break
            if pazaakGame.whoWon() == 2:
                pazaakGame.P2gamesWon += 1
                print("p2 won")
                #draw_winner
                if rounds_checker == 1: 
                    rounds_checker = 2
                elif rounds_checker == 2: 
                    rounds_checker = 1
                pazaakGame.player = rounds_checker
                rounds_flag = 1
                break
            if pazaakGame.whoWon() == -1:
                print("tie")
                if rounds_checker == 1: 
                    rounds_checker = 2
                elif rounds_checker == 2: 
                    rounds_checker = 1
                pazaakGame.player = rounds_checker
                rounds_flag =1 
                break

            if pazaakGame.player == 1 and pazaakGame.P1stillPlaying == 1:
                pazaakGame.P1boardCards.append(nextCard)
                pazaakGame.P1setVal += nextCard
            if pazaakGame.player == 2 and pazaakGame.P2stillPlaying == 1:
                pazaakGame.P2boardCards.append(nextCard)
                pazaakGame.P2setVal += nextCard
            for event in pygame.event.get():
                exxxit = run = quit_game(event)
            if pazaakGame.player == 2:
                run = run2= exxxit = player2_AI(pazaakGame, 0)
                run2 = False
            else:
                run2 = True
            draw_window(pazaakGame)

            for event in pygame.event.get():
                exxxit = run = quit_game(event)
            pick_card = True

            while run2: 
                
                for event in pygame.event.get():
                    #time.sleep(1)
                    exxxit = run = run2 = quit_game(event)
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
                                        #print(pazaakGame.P1setVal, "   ", card[0])

                                        pazaakGame.P1setVal += card[0]
                                        #print(pazaakGame.P1setVal)
                                        draw_window(pazaakGame)
                                        pick_card = False
                                        if pazaakGame.P1setVal >= 20: 
                                            pazaakGame.P1stillPlaying = 0
                                            #run2= False
                                            break
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
                                if pazaakGame.P1setVal >= 20: 
                                    pazaakGame.P1stillPlaying = 0
                                run2 = False
            draw_window(pazaakGame)
        draw_window(pazaakGame)
    draw_window(pazaakGame)
    if pazaakGame.P1gamesWon == 3:
        print('yo')
        draw_winner(1)
        wait_timer(5)
    elif pazaakGame.P2gamesWon == 3:
        draw_winner(2)
        wait_timer(5)

    pygame.quit()

    return None

if __name__ == "__main__":
    main()
