from fileinput import filename
import json

def saveGame(current_game):
    filename = 'gameHistory.json'

    # load json for existing game history
    with open(filename, "r") as file:
        history = json.load(file)

    # load json for current game
    with open(current_game, "r") as game:
        curr_game = json.load(game)

    # add the current game records to the history
    game_name = 'Game ' + str(len(history) + 1)
    history[game_name] = curr_game
    file.close()
    game.close()

    with open(filename, "w") as file:
        json.dump(history, file)
    file.close()

    # clear 
    with open(current_game, "w") as game:
        pass
    game.close()