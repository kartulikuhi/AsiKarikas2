import easygui
import turtle
from turtle import *
from board import Board
from coin import Coin
from functions import play
from cpu import CPU
import time

class PlayState(object):
    def __init__(self, board_height, board_width, realg, gap, res, gap2, opponent, CPU_difficulty):
        self.board = Board(board_height, board_width)
        self.player = 1
        self.activeCoin = Coin(0, 0, 1)
        self.turnCount = 1
        self.realg = realg
        self.gap = gap
        self.gap2 = gap2
        self.res = res
        self.opponent = opponent
        self.CPU = CPU(CPU_difficulty)
        self.x = 0

    def update(self):
        if self.opponent == 'Player':
            while True:
                turtle.Screen().onclick(self.WhatRow)
                update()
        else:
            while True:
                turtle.Screen().onclick(self.WhatRowCPU)
                update()

    def WhatRow(self, x, y):
        goto(x,y)
        self.activeCoin.x = int(((self.res*0.95 * -0.5) + xcor())//self.gap) + self.board.columns
        self.doMove()

    def WhatRowCPU(self, x, y):
        goto(x, y)
        self.activeCoin.x = int(((self.res*0.95 * -0.5) + xcor())//self.gap) + self.board.columns
        self.doMove()
        self.doMoveCPU()
            
    def doMove(self):
        error_beep = True

        for board_y in range(self.board.rows - 1, -1, -1):

            if self.board.tileMap[self.activeCoin.x][board_y] == False:
                self.activeCoin.y = board_y
                self.board.tileMap[self.activeCoin.x][board_y] = self.activeCoin.player

                self.board.coins.append(self.activeCoin)
                turtle.goto(-0.5 * self.res + (self.activeCoin.x * self.gap + 0.025 * self.res) + 0.5 * self.gap, -0.5 * self.res + ((self.board.rows - self.activeCoin.y - 1) * self.gap2 + 0.015 * self.res) + 0.5 * self.realg)
                if self.activeCoin.player == 1:
                    dot(self.realg, 'red')
                else:
                    dot(self.realg, 'yellow')

                error_beep = False
                self.turnCount += 1

                self.activeCoin.y = board_y

                if self.board.calculateWins(self.player):
                    play('winsound')
                    return [self.player, self.board]
                else:
                    if self.turnCount > self.board.rows * self.board.columns:
                        play('tiesound')
                        return [0, self.board]
                    else:

                        self.player = 2 if self.player == 1 else 1

                        previousX = self.activeCoin.x
                        self.activeCoin = Coin(previousX, 0, self.player)
                        play('newturnsound')
            
                break
            
        if error_beep:
            play('errorsound')

    def doMoveCPU(self):
        self.activeCoin.x = self.CPU.makemove(self.board)
        self.doMove()