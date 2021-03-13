from functions import quit, pressed, play
import time
import turtle
from turtle import *
class GameOverState(object):
    def __init__(self, player, board):
        self.player = player
        self.board = board
        self.tie = False
        if self.player == 0:
            self.tie = True
        else:
            self.winner = 'Player ' + str(self.player)
    
    def update():
        while True:
            if pressed('enter') or pressed('return'):
                play('startsound')
                return True
            
            if pressed('escape'):
                quit()
                
            time.sleep(0.05)
    def writeResults(b, res):
        if b == 'tie':
            text = 'It is a tie!'
        else:
            text = 'Player ' + str(b) + ' won!'
        goto(res* -0.45, res * 0.37)
        color('White')
        write(text, font=("Comic Sans", int(res * 0.05), "normal"))
        goto(res * 0.1, res * 0.48)
        fillcolor("purple")
        color('purple')
        down()
        begin_fill()
        goto(res * 0.47, res * 0.48)
        goto(res * 0.47,res * 0.36)
        goto(res * 0.1, res * 0.36)
        goto(res * 0.1, res * 0.48)
        end_fill()
        up()
        color('white')
        goto(res * 0.115, res * 0.37)
        write('Play again', font=("Comic Sans", int(res * 0.05), "normal"))
        update()
    def render(self):
        pass