from playstate import PlayState
from gameoverstate import GameOverState
import turtle
import sys
from turtle import *
import easygui
from easygui import *
from creategrid import *
import creategrid
import time
play_again = True

while play_again:
    tall, wide, realg, gap, res, gap2, opponent, difficulty, screen = CreateGrid()
    play = PlayState(tall, wide, realg, gap, res, gap2, opponent, difficulty)
    b = play.update()
    GameOverState.writeResults(b,res)
    goto(0,0)
    while True:
        onscreenclick(goto)
        if xcor() >= 0.1 * res and ycor() >= 0.36 * res:
            break
        update()
