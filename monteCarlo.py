from my_pazaak import *

class RootKids:
    def __init__(self, pazaakGame: PazaakState, move: int) -> None :
        self.move = move
        self.state = pazaakGame
        self.wins = 0
        self.loses = 0

def monte_carlo_algorithm(pazaakGame: PazaakState) -> int:
    print("monteCarloAlgo")
    expansion(pazaakGame)
    simulation()
    backpropagation()
    return 0

def doMove(pazaakGame: PazaakState, move: int) -> PazaakState:
    print(move)
    childState: PazaakState = pazaakGame.makeChild()
# -------------------------------------------#
    if move == -10:
        childState.P2setVal += -5
        childState.P2stillPlaying == 0
        return childState
        
    elif move == -9: 
        childState.P2setVal += -4
        childState.P2stillPlaying == 0
        return childState
        
    elif move == -8:
        childState.P2setVal += -3
        childState.P2stillPlaying == 0
        return childState
        
    elif move == -7:
        childState.P2setVal += -2
        childState.P2stillPlaying == 0
        return childState
        
    elif move == -6:
        childState.P2setVal += -1
        childState.P2stillPlaying == 0
        return childState
        
# -------------------------------------------#
    elif move == -5:
        childState.P2setVal += -5
        return childState

    elif move == -4:
        childState.P2setVal += -4
        return childState

    elif move == -3:
        childState.P2setVal += -3
        return childState

    elif move == -2:
        childState.P2setVal += -2
        return childState

    elif move == -1: 
        childState.P2setVal += -1
        return childState

# -------------------------------------------#
    elif move == 1: 
        childState.P2setVal += 1
        return childState

    elif move == 2:
        childState.P2setVal += 2
        return childState

    elif move == 3:
        childState.P2setVal += 3
        return childState

    elif move == 4:
        childState.P2setVal += 4
        return childState

    elif move == 5:
        childState.P2setVal += 5
        return childState

# -------------------------------------------#
    elif move == 6: 
        childState.P2setVal += 1
        childState.P2stillPlaying == 0
        return childState
         
    elif move == 7:
        childState.P2setVal += 2
        childState.P2stillPlaying == 0
        return childState
        
    elif move == 8:
        childState.P2setVal += 3
        childState.P2stillPlaying == 0
        return childState
        
    elif move == 9:
        childState.P2setVal += 4
        childState.P2stillPlaying == 0
        return childState
        
    elif move == 10:
        childState.P2setVal += 5
        childState.P2stillPlaying == 0
        return childState
        

# -------------------------------------------#
    elif move == 11: 
        return childState
    elif move == 12:
        childState.P2stillPlaying == 0
        return childState
    #print(childState.player)
    
    return childState

#   Moves List:
#   move:   -10 -> -5 & Stand
#   move:    -9 -> -4 & Stand
#   move:    -8 -> -3 & Stand
#   move:    -7 -> -2 & Stand
#   move:    -6 -> -1 & Stand

#   move:    -5 -> -5 & End Turn
#   move:    -4 -> -4 & End Turn    
#   move:    -3 -> -3 & End Turn
#   move:    -2 -> -2 & End Turn
#   move:    -1 -> -1 & End Turn

#   move:     1 -> +1 & End Turn
#   move:     2 -> +2 & End Turn
#   move:     3 -> +3 & End Turn
#   move:     4 -> +4 & End Turn
#   move:     5 -> +5 & End Turn

#   move:     6 -> +1 & Stand
#   move:     7 -> +2 & Stand
#   move:     8 -> +3 & Stand
#   move:     9 -> +4 & Stand
#   move:    10 -> +5 & Stand

#   move:    11 -> End Turn
#   move:    12 -> Stand

# function to expand the root node and return a list of kids
def expansion(pazaakGame: PazaakState) -> List[RootKids]:
    print("expand")
    childs: List[RootKids] = []
    childs.append(RootKids(doMove(pazaakGame, 11), 11))
    childs.append(RootKids(doMove(pazaakGame, 12), 12))
    for card in pazaakGame.P2sideCards:
        childs.append(RootKids(doMove(pazaakGame, card[0]), card[0]))
        if card[0] == card[1]:
            continue
        childs.append(RootKids(doMove(pazaakGame, card[1]), card[1]))
        print(card)
    for kid in childs:
        print(kid.state.P2setVal)
    return childs

# function to simulate children and retur
def simulation() -> None:
    print("simulate")
    return None

def backpropagation() -> None:
    print("backpropagate")
    return None
