# Core game model here. Define your namedtuple to represent your game state.
# All functions should be pure i.e. no i/o, no global vars etc.

from collections import namedtuple
from tic_tac_toe_move_exception import SpaceAlreadyUsedError, InputNotInCorrectForm

class Board:

    __slots__ = ('top_left', 'top_centre', 'top_right', 'middle_left', 'centre', 'middle_right', 'bottom_left','bottom_centre', 'bottom_right')

    def __init__(self):
        self.top_left = ' '
        self.top_centre = ' '
        self.top_right = ' '
        self.middle_left = ' '
        self.centre = ' '
        self.middle_right = ' '
        self.bottom_left = ' '
        self.bottom_centre = ' '
        self.bottom_right = ' '

    def changeBoard(self, attribute_to_change, piece):
        setattr(self, attribute_to_change, piece)

    def isBoardWinning(self):
        valid_pieces = ('X', '0')
        if self.centre in valid_pieces:
            if self.middle_left == self.centre == self.middle_right:
                return True
            elif self.top_centre == self.centre == self.bottom_centre:
                return True
            elif self.top_left == self.centre == self.bottom_right:
                return True
            elif self.bottom_left == self.centre == self.top_right:
                return True
        if self.top_left in valid_pieces:
            if self.top_left == self.top_centre == self.top_right:
                return True
            if self.top_left == self.middle_left == self.bottom_left:
                return True
        if self.bottom_right in valid_pieces:
            if self.bottom_left == self.bottom_centre == self.bottom_right:
                return True
            if self.top_right == self.middle_right == self.bottom_right:
                return True
        return False

    def isBoardFull(self):
        listofBoardspaces = [self.top_left, self.top_centre, self.top_right, self.middle_left, self.centre, self.middle_right, self.bottom_left, self.bottom_centre, self.bottom_right]
        if ' ' in listofBoardspaces:
            return False
        return True

    def isBoardaDraw(self):
        if not self.isBoardFull() or self.isBoardWinning():
            return False
        return True

    def __str__(self):
        return f'\nGamestate: \n \n {self.top_left} | {self.top_centre} | {self.top_right} \n-----------\n {self.middle_left} | {self.centre} | {self.middle_right} \n-----------\n {self.bottom_left} | {self.bottom_centre} | {self.bottom_right} \n'

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

def initalise_game():
    Current_Gamestate = Gamestate()
    Spaces_Used = []
    print(f"\nPlayer One is Crosses (X) and Player Two is Noughts (0)\n")
    print(Current_Gamestate.Gameboard)
    print(f'Next marker: {Current_Gamestate.XOr0}')
    return Current_Gamestate, Spaces_Used

def change_board(Current_Gamestate, chosen_space):
    Current_Gamestate = Update_Gamestate(Current_Gamestate, chosen_space)
    print(Current_Gamestate.Gameboard)
    print(f'Is this a winning gameboard: {Current_Gamestate.Gameboard.isBoardWinning()}')
    print(f'Is board a draw: {Current_Gamestate.Gameboard.isBoardaDraw()}')
    print(f'Next marker: {Current_Gamestate.XOr0}')
    return Current_Gamestate

def gameOver(Current_Gamestate):
    if Current_Gamestate.Gameboard.isBoardWinning() or Current_Gamestate.Gameboard.isBoardaDraw():
        return True
    return False

def gameContinue(Current_Gamestate, Spaces_Used):
    chosen_space = input("Input space: ").lower() #########################no i/o
    if chosen_space in Spaces_Used:
        print(SpaceAlreadyUsedError(f'\nThis space has already been scribled in! Try another space!'))
        return Current_Gamestate, Spaces_Used
    Current_Gamestate = change_board(Current_Gamestate, chosen_space)
    Spaces_Used.append(chosen_space)
    return Current_Gamestate, Spaces_Used


if __name__ == '__main__':

    Current_Gamestate, Spaces_Used = initalise_game()

    while not gameOver(Current_Gamestate):
        try:
            gameContinue(Current_Gamestate, Spaces_Used)
        except AttributeError as e:
            print(f'\n{e}')
            print(InputNotInCorrectForm(f"Input must be in one of the following forms:\n'top_left', 'top_centre', 'top_right', 'middle_left', 'centre', 'middle_right', 'bottom_left','bottom_centre', 'bottom_right'"))
    
    print("\n GAME OVER")

    

