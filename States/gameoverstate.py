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
    

    def writeResults(result, resolution): #Kirjutab mängu lõppedes mängu tulemuse ekraanile ning lisab ka nupu mida vajutades saab uuesti mängida.

        if result == 'tie':
            text = "It's a tie!"
        else:
            text = 'Player ' + str(result) + ' won!'

        goto(resolution * -0.45, resolution * 0.37)
        color('White')
        write(text, font=('Comic Sans', int(resolution * 0.05), 'normal'))

        goto(resolution * 0.1, resolution * 0.48)
        fillcolor('purple')

        color('purple')
        down()
        begin_fill()
        goto(resolution * 0.47, resolution * 0.48)
        goto(resolution * 0.47,resolution * 0.36)
        goto(resolution * 0.1, resolution * 0.36)
        goto(resolution * 0.1, resolution * 0.48)
        end_fill()
        up()

        color('white')
        goto(resolution * 0.115, resolution * 0.37)
        write('Play again', font = ('Comic Sans', int(resolution * 0.05), 'normal'))
        update()
