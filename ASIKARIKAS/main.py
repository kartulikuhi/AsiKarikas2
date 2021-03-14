from States.playstate import PlayState
from States.gameoverstate import GameOverState
from turtle import *
from easygui import *
from Functions.creategrid import *
from Functions.functions import play

play_again = True


while play_again:

    height, width, ball_size, horizontal_gap, resolution, vertical_gap, opponent, difficulty, screen = CreateGrid()
    game = PlayState(height, width, ball_size, horizontal_gap, resolution, vertical_gap, opponent, difficulty)
    play('start-up')

    result, turn_count = game.update()
    GameOverState.writeResults(result, turn_count, opponent, difficulty, width, height, resolution)


    goto(0,0)

    while True:

        onscreenclick(goto)
        if xcor() >= 0.1 * resolution and ycor() >= 0.36 * resolution:
            break

        update()