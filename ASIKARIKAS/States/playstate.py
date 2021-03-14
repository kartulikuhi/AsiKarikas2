import turtle
from turtle import *
from Classes.board import Board
from Functions.functions import play
from Classes.cpu import CPU

class PlayState(object):
    def __init__(self, board_height, board_width, ball_size, horizontal_gap, resolution, vertical_gap, opponent, CPU_difficulty):

        #Laua ja CPU initsialiseerimine
        self.board = Board(board_height, board_width)
        self.CPU = CPU(CPU_difficulty)

        #back-end parameetrite defineerimine
        self.player = 1
        self.turnCount = 1
        self.move = 0
        self.winner = 0
        self.opponent = opponent
        self.canInput = True
        self.error_beep = True

        #renderdamiseks vajalike parameetrite defineerimine
        self.ball_size = ball_size
        self.horizontal_gap = horizontal_gap
        self.vertical_gap = vertical_gap
        self.resolution = resolution

        
    #Üldine funktsioon, mis jooksutab mängu
    def update(self):

        if self.opponent == 'Player':

            while True:

                if self.winner != 0:
                    return self.winner, self.turnCount
                else:
                    turtle.Screen().onclick(self.WhatRow)
                update()


        else:

            while True:

                if self.winner != 0:
                    return self.winner, self.turnCount
                else:
                    turtle.Screen().onclick(self.WhatRowCPU)
                update()


    #Inimene VS Inimene käik
    def WhatRow(self, x, y):
        if self.canInput:
            goto(x,y)
            if abs(x) <= self.resolution / 2 - 25:
                self.move = int(((self.resolution*0.95 * -0.5) + xcor())//self.horizontal_gap) + self.board.columns

                self.doMove()
            else:
                play('error')
        
        
    #Inimene VS Arvuti käik
    def WhatRowCPU(self, x, y):
        if self.canInput:
            goto(x, y)
            if abs(x) <= self.resolution / 2 - 25:
                self.move = int(((self.resolution*0.95 * -0.5) + xcor())//self.horizontal_gap) + self.board.columns

                self.doMove()
                if not self.error_beep and self.winner == 0:
                    self.doMoveCPU()

            else:
                play('error')

            

    #Üldine käigu tegemine
    def doMove(self):
        
        self.canInput = False
        self.error_beep = True

        for board_y in range(self.board.rows - 1, -1, -1): #Laua kõige ülemine koordinaat on 0 (y-telje positiivne suund allapoole)

            if self.board.tileMap[self.move][board_y] == False: #Käib esimesse vabasse ritta

                self.board.tileMap[self.move][board_y] = self.player

                #joonistab mündi
                turtle.goto(-0.5 * self.resolution + (self.move * self.horizontal_gap + 0.025 * self.resolution) + 0.5 * self.horizontal_gap, -0.5 * self.resolution + ((self.board.rows - board_y - 1) * self.vertical_gap + 0.015 * self.resolution) + 0.5 * self.ball_size)

                if self.player == 1:
                    dot(self.ball_size, 'red')
                else:
                    dot(self.ball_size, 'yellow')

                update()
                play('move')

                self.error_beep = False
                self.turnCount += 1

                #Kontrollib, kas viimati käidud käiguga võideti või tekib viik, kui ei, siis on teise mängija kord
                if self.board.calculateWins(self.player, [self.move, board_y]):
                    play('win')
                    self.winner = self.player
                    return
                else:
                    if self.turnCount > self.board.rows * self.board.columns:
                        play('tie')
                        self.winner = 'tie'
                        return
                    else:

                        self.player = 2 if self.player == 1 else 1
            
                break
            
        if self.error_beep:
            play('error')
            self.canInput = True

        else:
            if not self.opponent == 'CPU':
                self.canInput = True
            elif self.player == 1:
                self.canInput = True

    #Arvuti käik
    def doMoveCPU(self):
        self.move = self.CPU.makemove(self.board)
        self.doMove()