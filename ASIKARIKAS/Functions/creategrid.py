import turtle
import easygui
from easygui import *
from turtle import *
import sys

def CreateGrid(): #Loob mängulaua graafiliselt kasutates turtle't
    resolution_choices = ['Medium (600x600)', 'Big (800x800)']
    resolution_choice = easygui.choicebox('Choose Your resolution', choices = resolution_choices) #akna suuruse valimine

    if resolution_choice == 'Medium (600x600)':
        resolution = 600
    elif resolution_choice == 'Big (800x800)':
        resolution = 800
    else:
        sys.exit(0)

    #Laua suuruse valimine
    board_choices = ['default (6x7)', 'custom']
    board_choice = easygui.choicebox('Choose your board preference', choices = board_choices)

    if board_choice == 'default (6x7)':
        width = 7
        height = 6
    else:

        while True:
            #veergude arvu valimine
            while True:

                loop_again = False
                width = easygui.enterbox('How many columns (more than 8 is not recommended for playing against hard difficulty CPU)?')

                for i in width:

                    if i not in '1234567890':
                        loop_again = True
                        break
                    
                if loop_again:
                    continue

                width = int(width)
                break
                        
            #ridade arvu valimine
            while True:

                loop_again = False
                height = easygui.enterbox('How many rows?')

                for i in height:

                    if i not in '1234567890':
                        loop_again = True
                        break
                    
                if loop_again:
                    continue

                height = int(height)
                break


            if width <= 3 or height <= 3:
                print('Please choose a valid board for connect 4')
            else:
                break

    #Vastase valimine
    opponent_choices = ['Player', 'CPU']
    opponent = easygui.choicebox('Who do You want to play against?', choices = opponent_choices)
    difficulty = None

    if opponent == 'CPU':

        difficulty_choices = ['Easy', 'Medium', 'Hard']
        difficulty = easygui.choicebox('Please choose the difficulty of the CPU', choices = difficulty_choices)

        if difficulty == 'Easy':
            difficulty = 1

        elif difficulty == 'Medium':
            difficulty = 2

        elif difficulty == 'Hard':
            difficulty = 3
    
    screen = Screen().setup(resolution, resolution)
    clearscreen()
    ht()

    turtle.bgcolor('blue')
    def line(a, b, x, y):

        turtle.up()
        turtle.goto(a, b)

        turtle.down()
        turtle.goto(x, y)
        
        turtle.up()

    #pallide joonistamiseks vajalike parameetrite arvutamine
    horizontal_gap = round((resolution*0.95) / width)
    start = -0.5 * resolution * 0.95
    turtle.Screen().tracer(0, 0)

    for i in range(width+1):
        position = start + (i * horizontal_gap)
        line(position, 0.35 * resolution, position, resolution * -0.5)

    vertical_gap = round((resolution*0.82) / height)

    if vertical_gap > horizontal_gap:
        ball_size = horizontal_gap
    else:
        ball_size = vertical_gap

    ball_size = ball_size * 0.8

    for x in range(width):
        for y in range(height):
            turtle.goto(-0.5 * resolution + (x * horizontal_gap + 0.025 * resolution) + 0.5 * horizontal_gap, -0.5 * resolution + (y * vertical_gap + 0.015 * resolution) + 0.5 * ball_size) 
            turtle.dot(ball_size, 'white') #joonistab tühjad ringid, kuhu käia saab
    up()
    
    return height, width, ball_size, horizontal_gap, resolution, vertical_gap, opponent, difficulty, screen