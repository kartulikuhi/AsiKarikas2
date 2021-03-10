import random

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

                    if board.calculateWins(2):
                        board_copy[column][row] = False
                        return column

                    board_copy[column][row] = 1

                    if board.calculateWins(1):
                        board_copy[column][row] = False
                        return column

                    board_copy[column][row] = False

                    break
        
        return random.choice(return_vals)
        
            
            

    def makeMediumMove(self, board):
        board_copy = board.tileMap
        score = 0
        return_vals = []

        for column in range(board.columns):
            for row in range(board.rows - 1, -1, -1):

                if board_copy[column][row] == False:
                    
                    board_copy[column][row] = 2

                    if board.calculateWins(2):
                        board_copy[column][row] = False
                        return column
                    
                    board_copy[column][row] = 1

                    if board.calculateWins(1):
                        board_copy[column][row] = False
                        return column
                    
                    board_copy[column][row] = 2

                    for column2 in range(board.columns):
                        temp_score1 = 0
                        for row2 in range(board.rows - 1, -1, -1):

                            if board_copy[column2][row2] == False:

                                board_copy[column2][row2] = 1

                                if board.calculateWins(1):
                                    board_copy[column][row] = False
                                    board_copy[column2][row2] = False
                                    break

                                enemy_straight = board.returnLongestStraight(1)
                                if enemy_straight[0] == 3:
                                    temp_score1 += 4 * len(enemy_straight)


                                for column3 in range(board.columns):
                                    temp_score2 = 0
                                    for row3 in range(board.rows):

                                        if board_copy[column3][row3] == False:

                                            board_copy[column3][row3] = 2

                                            CPU_wins = board.calculateWinCount(2)

                                            temp_score2 += 10 * CPU_wins
                                            
                                            CPU_straight = board.returnLongestStraight(2)
                                            if CPU_straight[0] == 3:
                                                temp_score2 += 4 * len(CPU_straight)

                                            score_diff = temp_score2 - temp_score1
                                            if score_diff > score:
                                                score = score_diff
                                                return_vals = [column]
                                            elif score_diff == score:
                                                return_vals.append(column)
                                            
                                            board_copy[column3][row3] = False
                                            break
                                            

                                board_copy[column2][row2] = False
                    board_copy[column][row] = False

        if len(return_vals) == 0:
            while True:
                x = random.randrange(board.columns)
                if board_copy[x][0] == False:
                    return x
        return random.choice(return_vals)
                                

    def makeHardMove(self, board):
        pass