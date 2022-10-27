# Your code to implement the playing of the game here. Impure functions are allowed.
from tic_tac_toe_model import *
from tic_tac_toe_move_exception import InputNotInCorrectForm, SpaceAlreadyUsedError
from random import randint

def gameOver(Current_Gamestate):
    if Current_Gamestate.Gameboard.isBoardWinning() or Current_Gamestate.Gameboard.isBoardaDraw():
        print("\nGAME OVER")
        return True
    return False

def gameContinue(Current_Gamestate, Spaces_Used, NoughtorCross):
    chosen_space = input(f"Player {player_number(Current_Gamestate, NoughtorCross)} input which box: ").lower().strip().replace(' ', '_', 1).replace(' ', '')
    if chosen_space in Spaces_Used:
        print(SpaceAlreadyUsedError(f'\nThis space has already been scribled in! Try another space!'))
        return Current_Gamestate, Spaces_Used
    elif chosen_space == 'exit':
        callFileSave(Current_Gamestate, Spaces_Used, NoughtorCross)
        print('Game Saved: Exiting Python')
        quit()
    Current_Gamestate = change_board(Current_Gamestate, chosen_space)
    Spaces_Used.append(chosen_space)
    return Current_Gamestate, Spaces_Used

def playerVSplayer(Current_Gamestate, Spaces_Used, NoughtorCross):
        while not gameOver(Current_Gamestate):
            try:
                gameContinue(Current_Gamestate, Spaces_Used, NoughtorCross)
            except AttributeError:
                print(InputNotInCorrectForm(f"\nInput must be in one of the following forms:\n'top left', 'top centre', 'top right', 'middle left', 'centre', 'middle right', 'bottom left','bottom centre', 'bottom right'\n"))
            
        if Current_Gamestate.Gameboard.isBoardWinning() and Current_Gamestate.XOr0.piece == NoughtorCross:
            print(f'Player 2 won!')
        elif Current_Gamestate.Gameboard.isBoardWinning() and Current_Gamestate.XOr0.piece != NoughtorCross:
            print(f'Player 1 won!')
        else:
            print(f"No one won, it's a draw")

def randomAI(Current_Gamestate, Spaces_Used, NoughtorCross):
    all_possible_spaces = ['top_left', 'top_centre', 'top_right', 'middle_left', 'centre', 'middle_right', 'bottom_left','bottom_centre', 'bottom_right']
    chosen_space = all_possible_spaces[randint(0,8)]
    if chosen_space in Spaces_Used:
        randomAI(Current_Gamestate, Spaces_Used, NoughtorCross)
    else:
        Current_Gamestate = change_board(Current_Gamestate, chosen_space)
        Spaces_Used.append(chosen_space)
    return Current_Gamestate, Spaces_Used, NoughtorCross

def playerVSrandomAI(Current_Gamestate, Spaces_Used, NoughtorCross):
    while not gameOver(Current_Gamestate):
        if Current_Gamestate.XOr0.piece == NoughtorCross:
            gameContinue(Current_Gamestate, Spaces_Used, NoughtorCross)
        else:
            randomAI(Current_Gamestate, Spaces_Used, NoughtorCross)
            print(f'Computer chose {Spaces_Used[-1]}')

    if Current_Gamestate.Gameboard.isBoardWinning() and Current_Gamestate.XOr0.piece == NoughtorCross:
        print(f'The computer won!')
    elif Current_Gamestate.Gameboard.isBoardWinning() and Current_Gamestate.XOr0.piece != NoughtorCross:
        print(f'You won!')
    else:
        print(f"No one won, it's a draw")

def playAgainstAIQuestion(Current_Gamestate, Spaces_Used, NoughtorCross):
    againstcomputer = input('Would you like to play against the computer? Y/N\n').upper().strip().replace(' ', '')
    if againstcomputer == 'Y':
        playerVSrandomAI(Current_Gamestate, Spaces_Used, NoughtorCross)
    elif againstcomputer == 'N':
        playerVSplayer(Current_Gamestate, Spaces_Used, NoughtorCross)
    else:
        playAgainstAIQuestion(Current_Gamestate, Spaces_Used, NoughtorCross)



if __name__ == '__main__':

    Current_Gamestate, Spaces_Used, NoughtorCross = initalise_game()

    playAgainstAIQuestion(Current_Gamestate, Spaces_Used, NoughtorCross)

    
