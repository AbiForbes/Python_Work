# Your code to implement the playing of the game here. Impure functions are allowed.
from tic_tac_toe_model import *
from tic_tac_toe_move_exception import InputNotInCorrectForm, SpaceAlreadyUsedError

def gameOver(Current_Gamestate):
    if Current_Gamestate.Gameboard.isBoardWinning() or Current_Gamestate.Gameboard.isBoardaDraw():
        print("\n GAME OVER")
        return True
    return False

def gameContinue(Current_Gamestate, Spaces_Used, NoughtorCross):
    chosen_space = input(f"Player {player_number(Current_Gamestate, NoughtorCross)} input which box: ").lower().strip().replace(' ', '_', 1).replace(' ', '')
    if chosen_space in Spaces_Used:
        print(SpaceAlreadyUsedError(f'\nThis space has already been scribled in! Try another space!'))
        return Current_Gamestate, Spaces_Used
    Current_Gamestate = change_board(Current_Gamestate, chosen_space)
    Spaces_Used.append(chosen_space)
    return Current_Gamestate, Spaces_Used

def playerVSplayer(Current_Gamestate, Spaces_Used, NoughtorCross):
        while not gameOver(Current_Gamestate):
            try:
                gameContinue(Current_Gamestate, Spaces_Used, NoughtorCross)
            except AttributeError as e:
                print(InputNotInCorrectForm(f"\nInput must be in one of the following forms:\n'top left', 'top centre', 'top right', 'middle left', 'centre', 'middle right', 'bottom left','bottom centre', 'bottom right'\n"))

def playAgainstAIQuestion(Current_Gamestate, Spaces_Used, NoughtorCross):
    againstcomputer = input('Would you like to play against the computer? Y/N\n').upper().strip().replace(' ', '')
    if againstcomputer == 'Y':
        #do something here
        pass
    elif againstcomputer == 'N':
        playerVSplayer(Current_Gamestate, Spaces_Used, NoughtorCross)
    else:
        playAgainstAIQuestion(Current_Gamestate, Spaces_Used, NoughtorCross)




if __name__ == '__main__':

    Current_Gamestate, Spaces_Used, NoughtorCross = initalise_game()

    playAgainstAIQuestion(Current_Gamestate, Spaces_Used, NoughtorCross)

    
