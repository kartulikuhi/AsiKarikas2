from functions import quit, pressed, play
import time

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
    
    def render(self):
        pass