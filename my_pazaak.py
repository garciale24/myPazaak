import random
import time
from typing import Callable, Optional, Tuple

class PazaakState:
    def __init__(self, player: int) -> None:
        self.player: int = player
        self.moves: list[int] = None
        self.selected: int = -1
        self.display: Callable[[], PazaakState] = \
            lambda: PazaakState._display(\
                self.P1setVal, self.P2setVal, self.P1gamesWon, self.P2gamesWon,\
                     self.P1stillPlaying, self.P2stillPlaying, self.P1boardCards, self.P2boardCards, self.P1sideCards)
        self.P1gamesWon: int = 0
        self.P2gamesWon: int = 0
        self.P1stillPlaying: int = 1
        self.P2stillPlaying: int = 1
        self.P1boardCards: list[int] = []
        self.P2boardCards: list[int] = []
        self.P1sideCards: list[int] = []
        self.P2sideCards: list[int] = []
        self.P1setVal: int = 0
        self.P2setVal: int = 0
        self.util: Callable[[int, int], PazaakState] = \
            lambda: PazaakState._get_utility(self.P1stillPlaying, self.P2stillPlaying)
        self.traverse: Callable[[int], PazaakState] = \
            lambda index: PazaakState._performMove(player, index)
        self.whoWon: Callable[[], PazaakState] = \
            lambda: PazaakState._check_win(\
                PazaakState._get_utility(self.P1stillPlaying, self.P2stillPlaying), self.P1setVal, self.P2setVal)
        self.nextCard: Callable[[], PazaakState] = \
            lambda: PazaakState._next_card()

    @staticmethod
    def _display(p1sval: int, p2sval: int, p1gwon: int, p2gwon: int,\
         p1splay: int, p2splay: int, p1bcards: int, p2bcards: int, p1scards: int) -> str:
        print("-------DISPLAY-------")
        print("p1set val: ", p1sval)
        print("p2set val: ", p2sval)
        print("p1games won: ", p1gwon)
        print("p2games won: ", p2gwon)
        print("p1still playing: ", p1splay)
        print("p2still playing: ", p2splay)
        print("p1board cards: ", p1bcards)
        print("p1board cards: ", p2bcards)
        print("p1side cards: ", p1scards)
        print("-------DISPLAY-------")
        return ""

    @staticmethod
    def _next_card() -> int:
        return random.randrange(1, 10)

    @staticmethod
    def _performMove(player: int, index: int) -> None:
        return None

    @staticmethod
    def _get_utility(p1sp: int, p2sp: int) -> int:
        if p1sp == 1 and p2sp == 1:
            return 0
        elif p1sp == 0 and p2sp == 1:
            return 2
        elif p1sp == 1 and p2sp == 0:
            #print("yyo")
            return 1    
        return 3

    # util, p1 set val, p2 set val
    @staticmethod
    def _check_win(util: int, p1sv: int, p2sv) -> int:
        #print("okk")
        #print(util, p1sv, p2sv)
        if util == 3:
            if p2sv > 20:
                return 1
            if p1sv > 20:
                return 2
            if p1sv > p2sv:
                return 1
            if p1sv < p2sv:
                return 2
            if p1sv == p2sv:
                return -1
            #print("util3", p1sv, p2sv)
        elif util == 0:
            # print("yo")
            if p2sv > 20:
                return 1
            if p1sv > 20:
                return 2
            #print("util0", p1sv, p2sv)
        elif util == 1:
            if p1sv > 20:
                return 2
            if p2sv > 20:
                return 1
            if p1sv > p2sv:
                return 1
            
            #print("util1", p1sv, p2sv)
        elif util == 2:
            if p2sv > 20:
                return 1
            if p1sv > 20:
                return 2
            if p1sv < p2sv:
                return 2
            #print("util2", p1sv, p2sv)
        #print("returns")
        return 0

def main() -> None:
    j: int = 0
    i: int = 0
    k: int = 1
    p1wins: int = 0
    p2wins: int = 0
    ties: int = 0
    while j < 10000:
        if k == 1:
            k = 2
        elif k == 2:
            k = 1
        pazaakGame = PazaakState(k)
        while i < 4:
            pazaakGame.P1sideCards.append(random.randrange(-5, 5))
            i += 1
        i = 0
        while i < 4:
            pazaakGame.P2sideCards.append(random.randrange(-5, 5))
            i += 1
        #print(pazaakGame.P1sideCards)
        #print(pazaakGame.P2sideCards)

        #print("My Pazaak")
        #i: int = 0
        
        #while i < 10:
        #    print(pazaakGame.nextCard())
        #    i += 1
        
        #pazaakGame.display()
        endCond: int = pazaakGame.whoWon()


        while endCond == 0:
            #print(pazaakGame.player, pazaakGame.P1setVal, pazaakGame.P2setVal, pazaakGame.util())


            nextCard: int = pazaakGame.nextCard()


            if pazaakGame.player == 1:
                if pazaakGame.P1stillPlaying == 1:
                    
                    pazaakGame.P1boardCards.append(nextCard)
                    pazaakGame.P1setVal += nextCard
                    if pazaakGame.P1setVal >= 20:
                        pazaakGame.P1stillPlaying = 0
                    #print("p1: ", pazaakGame.P1setVal)
                    #print("p1: ", pazaakGame.P1boardCards)

                pazaakGame.player = 2

                

            elif pazaakGame.player == 2:
                if pazaakGame.P2stillPlaying == 1:
                    pazaakGame.P2boardCards.append(nextCard)
                    pazaakGame.P2setVal += nextCard
                    #print("p2: ", pazaakGame.P2setVal)
                    #print("p2: ", pazaakGame.P2boardCards)
                    if pazaakGame.P2setVal >= 20:
                        pazaakGame.P2stillPlaying = 0
                        
                        i = 0
                        val: int = 0
                        lencond: int = len(pazaakGame.P2sideCards)
                        while i < lencond:
                            val = pazaakGame.P2sideCards[i] + pazaakGame.P2setVal
                            if val >= 19 and val <= 20:
                                #print(pazaakGame.P2setVal + pazaakGame.P2sideCards[i])

                                pazaakGame.P2setVal += pazaakGame.P2sideCards[i]
                                pazaakGame.P2sideCards.pop(i)
                                i = lencond
                                #print(pazaakGame.P2setVal)
                                #time.sleep(10)
                                pazaakGame.P2stillPlaying = 0

                            i += 1
                        
                        
                    if pazaakGame.P2setVal >= 17:
                        pazaakGame.P2stillPlaying = 0
                pazaakGame.player = 1        
                

            endCond = pazaakGame.whoWon()
        #print(endCond)
            if endCond == 1:
                p1wins += 1
                #print(pazaakGame.P1setVal, pazaakGame.P1boardCards, "  |  ", pazaakGame.P2setVal, pazaakGame.P2boardCards, pazaakGame.P2sideCards)

            elif endCond == 2:
                #print(pazaakGame.P1setVal, pazaakGame.P1boardCards, "  |  ", pazaakGame.P2setVal, pazaakGame.P2boardCards, pazaakGame.P2sideCards)

                p2wins += 1
            elif endCond == -1:
                ties += 1
        #print(pazaakGame.P1setVal, pazaakGame.P1boardCards, "  |  ", pazaakGame.P2setVal, pazaakGame.P2boardCards, pazaakGame.P2sideCards)
        i = 0
        j += 1
    print("p1wins: ", p1wins)
    print("p2wins: ", p2wins)
    print("ties: ", ties)



if __name__ == "__main__":
    main()
