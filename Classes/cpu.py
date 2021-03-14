import random

class CPU(object):

    def __init__(self,  difficulty):
        self.difficulty = difficulty

    def makemove(self, board):

        if self.difficulty == 1:
            return self.makeEasyMove(board)

        elif self.difficulty == 2:
            return self.makeMediumMove(board)

        else:
            return self.makeHardMove(board)

    def makeEasyMove(self, board): #arvutab praeguse käigu parima käigu ja käib selle

        (best_col, best_score) = self.findBestMove(board, 2, 2)

        if best_col is not None:
            return best_col
        
        x = 0
        while board[x][0] != False:
            x += 1
        return x
    
                                

    def makeMediumMove(self, board): #arvutab 2 käiguringi ette ja teeb selle põhjal parima käigu

        (best_col, best_score) = self.findBestMove(board, 2, 4)

        if best_col is not None:
            return best_col

        x = 0
        while board[x][0] != False:
            x += 1
        return x



    def makeHardMove(self, board): #Arvutab 3 käiguringi ette ja teeb selle põhjal parima käigu

        (best_col, best_score) = self.findBestMove(board, 2, 6)

        if best_col is not None:
            return best_col
        
        x = 0
        while board[x][0] != False:
            x += 1
        return x

    def findBestMove(self, board, player, turn_count): #tagastab parima käigu antud mängijale, rekursiivsusaste on turn_count


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

                    score = 100 * turn_count #mida sügavamal rekursiivsusredelil seda vähem punkte on väärt.

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
            
            
