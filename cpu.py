import random
from sys import call_tracing

class CPU(object):

    def __init__(self,  difficulty):
        self.difficulty = difficulty
        self.defensiveMove = 1
        self.offensiveMove = 2

    def makemove(self, board):
        if self.difficulty == 1:
            return self.makeEasyMove(board)
        elif self.difficulty == 2:
            return self.makeMediumMove(board)
        else:
            return self.makeHardMove(board)

    def makeEasyMove(self, board):

        board_copy = board.tileMap
        score = 0
        return_vals = []

        for column in range(board.columns):
            for row in range(board.rows - 1, -1, -1):

                if board_copy[column][row] == False:

                    board_copy[column][row] = 2

                    temp_score = board.returnLongestStraight(2)[0]

                    if temp_score == score:
                        score = temp_score
                        return_vals.append(column)
                    elif temp_score > score:
                        score = temp_score
                        return_vals = [column]

                    if board.calculateWins(2, [column, row]):
                        board_copy[column][row] = False
                        return column

                    board_copy[column][row] = 1

                    if board.calculateWins(1, [column, row]):
                        board_copy[column][row] = False
                        return column

                    board_copy[column][row] = False

                    break
        
        return random.choice(return_vals)
    
                                

    def makeMediumMove(self, board): 

        (best_col, best_score) = self.findBestMove(board, 2, 4)

        if best_col is not None:
            return best_col

        x = 0
        while board[x][0] != False:
            x += 1
        return x



    def makeHardMove(self, board):

        (best_col, best_score) = self.findBestMove(board, 2, 6)

        if best_col is not None:
            return best_col
        
        x = 0
        while board[x][0] != False:
            x += 1
        return x

    def findBestMove(self, board, player, turn_count):


        other_player = 1 if player == 2 else 2

        best_score = None

        best_col = None

        for column in range(board.columns):

            for row in range(board.rows - 1, -1, -1):

                if board.tileMap[column][row]:

                    continue



                score = None

                board.tileMap[column][row] = player

                if board.calculateWins(player, [column, row]):

                    score = 100 * turn_count

                else:

                    if turn_count == 1:

                        score = board.returnScore(player, [column, row])

                    else:

                        (col_other, score_other) = self.findBestMove(board, other_player, turn_count - 1)

                        if col_other is not None:

                            score = -score_other

                board.tileMap[column][row] = False



                if score is not None and (best_score is None or best_score <= score):

                    if best_score == score:
                        if random.randrange(3) == 1:

                            best_score = score

                            best_col = column
                    else:
                        best_score = score

                        best_col = column

                break

            if best_score is not None and best_score >= 1000:

                break
        
        return best_col, best_score
            
            
