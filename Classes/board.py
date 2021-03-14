class Board(object):
    def __init__(self, board_height, board_width):

        self.rows = board_height
        self.columns = board_width
        self.tileMap = self.generateBoard()
        self.coins = []
        

    def generateBoard(self): #tekitab listi False väärtustest. Kui tehakse käik, muudetakse vastaval kohal väärtuseks mängija, kes käigu tegi
        temp_lst = []
        for column in range(self.columns):
            temp_lst.append([])
            for row in range(self.rows):
                temp_lst[column].append(False)
        
        return temp_lst
    

    def calculateWins(self, player, coords): #kontrollib mingist positsioonist, kas antud mängija võitis
        
        counter = 0
        turn_column = coords[0]
        turn_row = coords[1]

        #vertikaalne kontroll
        counter = 0
        for row in range(turn_row, min(self.rows, turn_row + 4)):

            if self.tileMap[turn_column][row] == player:
                counter += 1
            else:
                counter = 0
            
            if counter >= 4:
                return True

        #horisontaalne kontroll
        counter = 0
        for column in range(max(0, turn_column - 3), min(self.columns, turn_column + 4)):

            if self.tileMap[column][turn_row] == player:
                counter += 1
            else:
                counter = 0

            if counter >= 4:
                return True

        #diagonaalne kontroll (paremale alla)

        counter = 0

        min_column = max(0, turn_column - 3)
        max_column = min(self.columns - 1, turn_column + 3)
        min_row = max(0, turn_row - 3)
        max_row = min(self.rows - 1, turn_row + 3)
        
        start_gap = min(turn_column - min_column, turn_row - min_row)
        start_column = turn_column - start_gap
        start_row = turn_row - start_gap

        end_gap = min(max_row - turn_row, max_column - turn_column)

        count_range = start_gap + end_gap + 1

        counter = 0
        for i in range(count_range):

            if self.tileMap[start_column + i][start_row + i] == player:
                counter += 1
            else:
                counter = 0

            if counter >= 4:
                return True

        
        #diagonaalne kontroll (paremale üles)
        counter = 0

        min_column = max(0, turn_column - 3)
        max_column = min(self.columns - 1, turn_column + 3)
        min_row = max(0, turn_row - 3)
        max_row = min(self.rows - 1, turn_row + 3)
        
        start_gap = min(turn_column - min_column, max_row - turn_row)
        start_column = turn_column - start_gap
        start_row = turn_row + start_gap

        end_gap = min(max_column - turn_column, turn_row - min_row)

        count_range = start_gap + end_gap + 1

        counter = 0
        for i in range(count_range):

            if self.tileMap[start_column + i][start_row - i] == player:
                counter += 1
            else:
                counter = 0

            if counter >= 4:
                return True
        
        return False


    def returnScore(self, player, coords): #tagastab mängija skoori mingi laua punkti suhtes.

        counter = 0
        turn_column = coords[0]
        turn_row = coords[1]
        score = 0

        #vertikaalne 
        current_longest = 0
        longest_counter = 0
        counter = 0
        for row in range(turn_row, min(self.rows, turn_row + 4)):

            if self.tileMap[turn_column][row] == player:
                counter += 1
            else:
                counter = 0
            
            
            if counter >= 4:
                score += 10
                current_longest = 0
                longest_counter = 0
                break
            elif counter > current_longest:
                current_longest = counter
                longest_counter = 0
            elif counter == current_longest:
                longest_counter += 1
        
        score += current_longest * (longest_counter + 1)

        #horisontaalne 
        counter = 0
        current_longest = 0
        longest_counter = 0
        for column in range(max(0, turn_column - 3), min(self.columns, turn_column + 4)):

            if self.tileMap[column][turn_row] == player:
                counter += 1
            else:
                counter = 0

            if counter >= 4:
                score += 10
                current_longest = 0
                longest_counter = 0
                break
            elif counter > current_longest:
                current_longest = counter
                longest_counter = 0
            elif counter == current_longest:
                longest_counter += 1
        
        score += current_longest * (longest_counter + 1)

        #diagonaalne (paremale alla)

        counter = 0
        current_longest = 0
        longest_counter = 0

        min_column = max(0, turn_column - 3)
        max_column = min(self.columns - 1, turn_column + 3)
        min_row = max(0, turn_row - 3)
        max_row = min(self.rows - 1, turn_row + 3)
        
        start_gap = min(turn_column - min_column, turn_row - min_row)
        start_column = turn_column - start_gap
        start_row = turn_row - start_gap

        end_gap = min(max_row - turn_row, max_column - turn_column)

        count_range = start_gap + end_gap + 1

        counter = 0
        for i in range(count_range):

            if self.tileMap[start_column + i][start_row + i] == player:
                counter += 1
            else:
                counter = 0

            if counter >= 4:
                score += 10
                current_longest = 0
                longest_counter = 0
                break
            elif counter > current_longest:
                current_longest = counter
                longest_counter = 0
            elif counter == current_longest:
                longest_counter += 1
        
        score += current_longest * (longest_counter + 1)

        
        #diagonaalne (paremale üles)
        counter = 0
        current_longest = 0
        longest_counter = 0

        min_column = max(0, turn_column - 3)
        max_column = min(self.columns - 1, turn_column + 3)
        min_row = max(0, turn_row - 3)
        max_row = min(self.rows - 1, turn_row + 3)
        
        start_gap = min(turn_column - min_column, max_row - turn_row)
        start_column = turn_column - start_gap
        start_row = turn_row + start_gap

        end_gap = min(max_column - turn_column, turn_row - min_row)

        count_range = start_gap + end_gap + 1

        counter = 0
        for i in range(count_range):

            if self.tileMap[start_column + i][start_row - i] == player:
                counter += 1
            else:
                counter = 0

            if counter >= 4:
                score += 10
                current_longest = 0
                longest_counter = 0
                break
            elif counter > current_longest:
                current_longest = counter
                longest_counter = 0
            elif counter == current_longest:
                longest_counter += 1
        
        score += current_longest * (longest_counter + 1)
        
        return score