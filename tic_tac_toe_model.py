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
        if '-' in listofBoardspaces:
            return False
        return True

    def isBoardaDraw(self):
        if not self.isBoardFull() or self.isBoardWinning():
            return False
        return True

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

def initalise_game():
    Current_Gamestate = Gamestate()
    print(f"\nPlayer One is Crosses (X) and Player Two is Noughts (0)\n")
    print(Current_Gamestate.Gameboard)
    print(f'Next marker: {Current_Gamestate.XOr0}')
    return Current_Gamestate

def change_board(Current_Gamestate, chosen_space):
    Current_Gamestate = Update_Gamestate(Current_Gamestate, chosen_space)
    print(Current_Gamestate.Gameboard)
    print(f'Is this a winning gameboard: {Current_Gamestate.Gameboard.isBoardWinning()}')
    print(f'Is board a draw: {Current_Gamestate.Gameboard.isBoardaDraw()}')
    print(f'Next marker: {Current_Gamestate.XOr0}')
    return Current_Gamestate


def main():
    Current_Gamestate = initalise_game()
    chosen_space = 'top_right'
    Current_Gamestate = change_board(Current_Gamestate, chosen_space)

    chosen_space = 'top_left'
    Current_Gamestate = change_board(Current_Gamestate, chosen_space)

    chosen_space = 'bottom_right'
    Current_Gamestate = change_board(Current_Gamestate, chosen_space)

    chosen_space = 'bottom_left'
    Current_Gamestate = change_board(Current_Gamestate, chosen_space)

    chosen_space = 'bottom_centre'
    Current_Gamestate = change_board(Current_Gamestate, chosen_space)

    chosen_space = 'top_centre'
    Current_Gamestate = change_board(Current_Gamestate, chosen_space)

    chosen_space = 'centre'
    Current_Gamestate = change_board(Current_Gamestate, chosen_space)

    chosen_space = 'middle_right'
    Current_Gamestate = change_board(Current_Gamestate, chosen_space)

    chosen_space = 'middle_left'
    Current_Gamestate = change_board(Current_Gamestate, chosen_space)

    


if __name__ == '__main__':

    main()
    

