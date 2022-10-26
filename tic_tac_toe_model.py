# Core game model here. Define your namedtuple to represent your game state.
# All functions should be pure i.e. no i/o, no global vars etc.

from collections import namedtuple

class Board:

    def __init__(self):
        self.top_left = '-'
        self.top_centre = '-'
        self.top_right = '-'
        self.middle_left = '-'
        self.centre = '-'
        self.middle_right = '-'
        self.bottom_left = '-'
        self.bottom_centre = '-'
        self.bottom_right = '-'

    def changeBoard(self, attribute_to_change, piece):
        setattr(self, attribute_to_change, piece)

    def isBoardWinning(self):
        pass

    def __str__(self):
        return f'\nGamestate: \n \n {self.top_left} {self.top_centre} {self.top_right} \n {self.middle_left} {self.centre} {self.middle_right} \n {self.bottom_left} {self.bottom_centre} {self.bottom_right} \n'

class Xor0:

    def __init__(self):
        self.piece = 'X'

    def changemarker(self):
        if self.piece == 'X':
            setattr(self, 'piece', '0')
        else:
            setattr(self, 'piece', 'X')
    
    def __str__(self):
        return self.piece

def Gamestate():
    Gamestate = namedtuple('Gamestate', ['XOr0', 'Gameboard'])
    piece = Xor0()
    board = Board()
    Current_Gamestate = Gamestate(piece, board)

    return Current_Gamestate

def Update_Gamestate(Current_Gamestate, chosen_space):
    board = Current_Gamestate.Gameboard
    piece = Current_Gamestate.XOr0
    piece_to_put_in_board = piece.piece
    board.changeBoard(chosen_space, piece_to_put_in_board)
    piece.changemarker()
    Current_Gamestate = Current_Gamestate._replace(Gameboard = board)
    Current_Gamestate = Current_Gamestate._replace(XOr0 = piece)
    return Current_Gamestate


if __name__ == '__main__':

    Current_Gamestate = Gamestate()
    print(f"\nPlayer One is Crosses (X) and Player Two is Noughts (0)\n")
    print(Current_Gamestate.Gameboard)
    print(f'Next marker: {Current_Gamestate.XOr0}')

    chosen_space = 'top_right'
    Current_Gamestate = Update_Gamestate(Current_Gamestate, chosen_space)
    print(Current_Gamestate.Gameboard)
    print(f'Next marker: {Current_Gamestate.XOr0}')
    
    chosen_space = 'top_left'
    Current_Gamestate = Update_Gamestate(Current_Gamestate, chosen_space)
    print(Current_Gamestate.Gameboard)
    print(f'Next marker: {Current_Gamestate.XOr0}')