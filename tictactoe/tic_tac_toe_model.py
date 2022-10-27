# Core game model here. Define your namedtuple to represent your game state.
# All functions should be pure i.e. no i/o, no global vars etc.

from collections import namedtuple
from tic_tac_toe_file_save import *

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

    def __dict__(self):
        dictionary = {"top_left" : self.top_left, "top_centre" : self.top_centre, "top_right" : self.top_right, "middle_left" : self.middle_left, "centre" : self.centre, "middle_right" : self.middle_right, "bottom_left" : self.bottom_left, "bottom_centre" : self.bottom_centre, "bottom_right" : self.bottom_right}
        return dictionary

    def changeBoard(self, attribute_to_change, piece):
        setattr(self, attribute_to_change, piece)

    def isBoardWinning(self):
        valid_pieces = ('❌', '⭕️')
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
        self.piece = '❌'

    def changemarker(self):
        if self.piece == '❌':
            setattr(self, 'piece', '⭕️')
        else:
            setattr(self, 'piece', '❌')
    
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

def initialise_new_game(Current_Gamestate, Spaces_Used, NoughtorCross):
    NoughtorCross = str(input('Would you like noughts or crosses? 0/X\n').upper().strip())
    if NoughtorCross == 'O':
        NoughtorCross = '0'

    if NoughtorCross == '0':
        NoughtorCross = '⭕️'
        piece = Current_Gamestate.XOr0
        piece.changemarker()
        Current_Gamestate = Current_Gamestate._replace(XOr0 = piece)
        print(Current_Gamestate.Gameboard)
        print(f"\nPlayer One is Noughts (⭕️) and Player Two is Crosses (❌)\n")
        return Current_Gamestate, Spaces_Used, NoughtorCross

    elif NoughtorCross == 'X':
        NoughtorCross = '❌'
        print(f"\nPlayer One is Crosses (❌) and Player Two is Noughts (⭕️)\n")
        print(Current_Gamestate.Gameboard)
        return Current_Gamestate, Spaces_Used, NoughtorCross

    else:
        print(f'Please enter ONLY a nought or a cross')
        Current_Gamestate, Spaces_Used, NoughtorCross = initalise_game()
        return Current_Gamestate, Spaces_Used, NoughtorCross

def shallWePickUpTheSaveFile(Current_Gamestate, Spaces_Used, NoughtorCross):
    newGameOrNot = input("Do you want to pick up your saved game? Y/N\n").upper()

    if newGameOrNot == 'Y':
        Current_Gamestate, Spaces_Used, NoughtorCross = callFileBack(Current_Gamestate, Spaces_Used, NoughtorCross)
        print(Current_Gamestate.Gameboard)
        return Current_Gamestate, Spaces_Used, NoughtorCross
    elif newGameOrNot == 'N':
        Current_Gamestate, Spaces_Used, NoughtorCross = initialise_new_game(Current_Gamestate, Spaces_Used, NoughtorCross)
        print(Current_Gamestate.Gameboard)
        return Current_Gamestate, Spaces_Used, NoughtorCross
    else:
        shallWePickUpTheSaveFile(Current_Gamestate, Spaces_Used, NoughtorCross)


def initalise_game():
    Current_Gamestate = Gamestate()
    Spaces_Used = []
    NoughtorCross = ''
    filename = "saved_game.txt"
    gameboardfile = "gameboard.json"
    f = None
    j = None
    try:
        f = open(filename, 'r')
        j = open(gameboardfile, 'r')
    except FileNotFoundError:
        Current_Gamestate, Spaces_Used, NoughtorCross = initialise_new_game(Current_Gamestate, Spaces_Used, NoughtorCross)
    else:
        f.close()
        j.close()
        Current_Gamestate, Spaces_Used, NoughtorCross = shallWePickUpTheSaveFile(Current_Gamestate, Spaces_Used, NoughtorCross)

    return Current_Gamestate, Spaces_Used, NoughtorCross


def change_board(Current_Gamestate, chosen_space):
    Current_Gamestate = Update_Gamestate(Current_Gamestate, chosen_space)
    print(Current_Gamestate.Gameboard)
    return Current_Gamestate

def player_number(Current_Gamestate, NoughtorCross):
    if Current_Gamestate.XOr0.piece == NoughtorCross:
        return 1
    else:
        return 2

