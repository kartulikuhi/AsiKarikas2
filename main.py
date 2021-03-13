from playstate import PlayState
from gameoverstate import GameOverState
import turtle
import sys
from turtle import *
import easygui
from easygui import *
from creategrid import *
import creategrid
play_again = True

while play_again:
    tall, wide, realg, gap, res, gap2, opponent, difficulty = CreateGrid()
    play = PlayState(tall, wide, realg, gap, res, gap2, opponent, difficulty)

    b = play.update()
    end = GameOverState(b[0], b[1])

    play_again = end.update()
    