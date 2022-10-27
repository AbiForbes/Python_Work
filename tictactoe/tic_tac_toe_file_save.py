
import os
import json


def callFileSave(Current_Gamestate, Spaces_Used, NoughtsorCrosses):
    filename = "saved_game.txt"
    gameboardfile = "gameboard.json"
    f = None
    j = None
    try:
        f = open(filename, "x")
        f.write(f'{Current_Gamestate.XOr0}\n{Spaces_Used}\n{NoughtsorCrosses}')
        j = open(gameboardfile, "x")
        j.write(json.dumps(Current_Gamestate.Gameboard.__dict__()))
    except FileExistsError:
        print (f'FileExistsAlready: You already have a game saved, this game was not saved')
    finally:
        if f != None:
            f.close()
        if j != None:
            j.close()

def callFileBack(Current_Gamestate, Spaces_Used, NoughtorCross):
    filename = "saved_game.txt"
    gameboardfile = "gameboard.json"
    f = None
    j = None
    try:
        f = open(filename, 'r')
        j = open(gameboardfile, 'r')
    except FileNotFoundError:
        print(f'You have no saved games')
    else:
        Current_Gamestate.XOr0.piece = f.readline()
        GameboardAttributes = json.load(j)
        attributeNames = list(GameboardAttributes.keys())
        attributeValues = list(GameboardAttributes.values())
        for item in range(len(GameboardAttributes)):
            attributeName = attributeNames[item]
            attributeValue = attributeValues[item]
            Current_Gamestate.Gameboard.changeBoard(attributeName, attributeValue)
        Spaces_Used = f.readline()
        NoughtorCross = f.readline()
        return Current_Gamestate, Spaces_Used, NoughtorCross
    finally:
        if f != None:
            os.remove(filename)
        if j != None:
            os.remove(gameboardfile)
        


if __name__ == "__main__":
    Current_Gamestate, Spaces_Used, NoughtorCross = initalise_game()
    print(Current_Gamestate.XOr0)
    Current_Gamestate, Spaces_Used = gameContinue(Current_Gamestate, Spaces_Used, NoughtorCross)
    print(Current_Gamestate)
    callFileSave(Current_Gamestate, Spaces_Used, NoughtorCross)
    
    Current_Gamestate = Gamestate()
    Spaces_Used = []
    NoughtorCross = ''
    Current_Gamestate, Spaces_Used, NoughtorCross = callFileBack(Current_Gamestate, Spaces_Used, NoughtorCross)
    print(Current_Gamestate)
    print(Current_Gamestate.XOr0)
    print(Current_Gamestate.Gameboard)
    print(Spaces_Used)
    print(NoughtorCross)
    Current_Gamestate, Spaces_Used = gameContinue(Current_Gamestate, Spaces_Used, NoughtorCross)