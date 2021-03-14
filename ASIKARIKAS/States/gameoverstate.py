from turtle import *
from datetime import datetime
import os

class GameOverState(object):

    def writeResults(result, turn_count, opponent, difficulty, resolution): #Kirjutab mängu lõppedes mängu tulemuse ekraanile ning lisab ka nupu mida vajutades saab uuesti mängida.
        
        CPU_difficulty = {1: 'easy', 2: 'medium', 3: 'hard'}
        result_to_save = datetime.now().strftime(' on %d/%m/%Y at %H:%M')

        turn_count -= 1
        
        if result == 'tie':
            text = "It's a tie!"

            if opponent == 'CPU':
                result_to_save = 'The game ended in a draw VS ' + CPU_difficulty[difficulty] + ' CPU' + result_to_save
            else:
                result_to_save = 'The game ended in a draw' + result_to_save

        elif result == 1:
            text = 'Red won!'

            if opponent == 'CPU':
                result_to_save = 'The player won against ' + CPU_difficulty[difficulty] + ' CPU on move ' + str(turn_count) + result_to_save
            else:
                result_to_save = 'Red player won on move ' + str(turn_count) + result_to_save
            
        else:
            text = 'Yellow won!'

            if opponent == 'CPU':
                result_to_save = 'The ' + CPU_difficulty[difficulty] + ' CPU won against the player on move ' + str(turn_count) + result_to_save
            else:
                result_to_save = 'Yellow player won on move ' + str(turn_count) + result_to_save


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

        file_location = os.getcwd() + '/results.txt'
        result_file = open(file_location, 'a')
        result_file.write(result_to_save + '\n')
        result_file.close()