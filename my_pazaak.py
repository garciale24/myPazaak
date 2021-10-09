import random

from typing import Callable, Optional, Tuple

class PazaakState:
    def __init__(self, player: int) -> None:
        self.player: int = player
        self.moves: Tuple[int] = None
        self.selected: int = -1
        self.display: Callable[[], PazaakState] = \
            lambda: PazaakState._display(\
                self.P1setVal, self.P2setVal, self.P1gamesWon, self.P2gamesWon,\
                     self.P1stillPlaying, self.P2stillPlaying, self.P1boardCards, self.P2boardCards, self.P1sideCards)
        self.P1gamesWon: int = 0
        self.P2gamesWon: int = 0
        self.P1stillPlaying: int = 1
        self.P2stillPlaying: int = 1
        self.P1boardCards: Tuple[int] = None
        self.P2boardCards: Tuple[int] = None
        self.P1sideCards: Tuple[int] = None
        self.P2sideCards: Tuple[int] = None
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
            return 1
        elif p1sp == 1 and p2sp == 0:
            return -1    
        return 2

    # util, p1 set val, p2 set val
    @staticmethod
    def _check_win(util: int, p1sv: int, p2sv) -> int:
        #print("okk")
        #print(util, p1sv, p2sv)
        if util == 2:
            if p2sv > 20:
                return -1
            if p1sv > 20:
                return 1
            if p1sv > p2sv:
                return -1
            if p1sv < p2sv:
                return 1
        if util == 0:
            # print("yo")
            if p2sv > 20:
                return -1
            if p1sv > 20:
                return 1
        if util == -1:
            if p2sv > 20:
                return -1
            if p1sv > 20:
                return 1
            if p1sv > p2sv:
                return -1
        if util == 1:
            if p2sv > 20:
                return -1
            if p1sv > 20:
                return 1
            if p1sv < p2sv:
                return 1
        return 0

def main() -> None:
    pazaakGame = PazaakState(1)
    print("My Pazaak")
    i: int = 0
    
    #while i < 10:
    #    print(pazaakGame.nextCard())
    #    i += 1
    
    pazaakGame.display()


if __name__ == "__main__":
    main()
