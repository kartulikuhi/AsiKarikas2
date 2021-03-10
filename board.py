#Eelnevalt tuleb tagada, et laua laius >= 4 ja pikkus >= 4 kuna siin seda ei kontrollita.
class Board(object):
    def __init__(self, board_height, board_width):

        self.rows = board_height
        self.columns = board_width
        self.tileMap = self.generateBoard()
        self.coins = []
        

    def generateBoard(self):
        temp_lst = []
        for column in range(self.columns):
            temp_lst.append([])
            for row in range(self.rows):
                temp_lst[column].append(False)
        
        return temp_lst
    
    def calculateWins(self, player):
        
        counter = 0
        win = False

        #vertikaalne kontroll
        for column in range(self.columns):
            counter = 0
            for row in range(self.rows):

                if self.tileMap[column][row] == player:
                    counter += 1
                else:
                    counter = 0
                
                if counter >= 4:
                    win = True
                    break
            
            if win:
                break
        
        #horisontaalne kontroll
        for row in range(self.rows):
            counter = 0
            for column in range(self.columns):

                if self.tileMap[column][row] == player:
                    counter += 1
                else:
                    counter = 0

                if counter >= 4:
                    win = True
                    break

            if win:
                break

        #diagonaalne kontroll (vasakult paremale)
        for row in range(self.rows - 1, self.rows - 4, -1):
            for column in range(self.columns - 3):
                counter = 0

                for i in range(4):

                    if self.tileMap[column + i][row - i] == player:
                        counter += 1
                    else:
                        counter = 0

                    if counter >= 4:
                        win = True
                        break
                
                if win:
                    break
            if win:
                break
        
        #diagonaalne kontroll (paremalt vasakule)
        for row in range(self.rows - 1, self.rows - 4, -1):
            for column in range(self.columns - 1, 2, -1):
                counter = 0
                
                for i in range(4):

                    if self.tileMap[column - i][row - i] == player:
                        counter += 1
                    else:
                        counter = 0
                    
                    if counter >= 4:
                        win = True
                        break
                
                if win:
                    break
            if win:
                break
        
        return win


    def returnLongestStraight(self, player):

        counter = 0
        largest_counter = [0]

        #vertikaalne kontroll
        for column in range(self.columns):
            counter = 0
            for row in range(self.rows):

                if self.tileMap[column][row] == player:
                    counter += 1
                else:
                    counter = 0
                
                if counter > largest_counter[0]:
                    largest_counter = [counter]
                elif counter == largest_counter:
                    largest_counter.append(counter)
            
        
        #horisontaalne kontroll
        for row in range(self.rows):
            counter = 0
            for column in range(self.columns):

                if self.tileMap[column][row] == player:
                    counter += 1
                else:
                    counter = 0

                if 4 > counter > largest_counter[0]:
                    largest_counter = [counter]
                elif counter == largest_counter:
                    largest_counter.append(counter)

        #diagonaalne kontroll (vasakult paremale)
        for row in range(self.rows - 1, self.rows - 3, -1):
            for column in range(self.columns - 3):
                counter = 0

                for i in range(4):

                    if self.tileMap[column + i][row - i] == player:
                        counter += 1
                    else:
                        counter = 0

                    if 4 > counter > largest_counter[0]:
                        largest_counter = [counter]
                    elif counter == largest_counter:
                        largest_counter.append(counter)
                
        
        #diagonaalne kontroll (paremalt vasakule)
        for row in range(self.rows - 1, self.rows - 3, -1):
            for column in range(self.columns - 1, 2, -1):
                counter = 0
                
                for i in range(4):

                    if self.tileMap[column - i][row - i] == player:
                        counter += 1
                    else:
                        counter = 0
                    
                    if 4 > counter > largest_counter[0]:
                        largest_counter = [counter]
                    elif counter == largest_counter:
                        largest_counter.append(counter)
        
        return largest_counter

    def calculateWinCount(self, player):
        
        counter = 0
        win = 0

        #vertikaalne kontroll
        for column in range(self.columns):
            counter = 0
            for row in range(self.rows):

                if self.tileMap[column][row] == player:
                    counter += 1
                else:
                    counter = 0
                
                if counter >= 4:
                    win += 1
        
        #horisontaalne kontroll
        for row in range(self.rows):
            counter = 0
            for column in range(self.columns):

                if self.tileMap[column][row] == player:
                    counter += 1
                else:
                    counter = 0

                if counter >= 4:
                    win += 1


        #diagonaalne kontroll (vasakult paremale)
        for row in range(self.rows - 1, self.rows - 4, -1):
            for column in range(self.columns - 3):
                counter = 0

                for i in range(4):

                    if self.tileMap[column + i][row - i] == player:
                        counter += 1
                    else:
                        counter = 0

                    if counter >= 4:
                        win += 1
                
        
        #diagonaalne kontroll (paremalt vasakule)
        for row in range(self.rows - 1, self.rows - 4, -1):
            for column in range(self.columns - 1, 2, -1):
                counter = 0
                
                for i in range(4):

                    if self.tileMap[column - i][row - i] == player:
                        counter += 1
                    else:
                        counter = 0
                    
                    if counter >= 4:
                        win += 1
            
        return win