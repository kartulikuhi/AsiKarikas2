import turtle
import easygui
from easygui import *
from turtle import *
global res
global tall
global wide
global gap
global gap2
global realg
def CreateGrid():
    choices = ['Small', 'Medium', 'Big']
    choice = easygui.choicebox('How big resolution do ya wanna?',choices=choices)

    if choice == 'Small':
        res = 400
    elif choice == 'Medium':
        res = 600
    elif choice == 'Big':
        res = 800
    else:
        print('no')
        sys.exit(0)

    wide = int(easygui.enterbox('How wide?'))
    tall = int(easygui.enterbox('How tall?'))

    if wide <= 3 or tall <= 3:
        print('no <3')
        sys.exit(0)

    choices = ['Player', 'CPU']
    opponent = easygui.choicebox('Who do you want to play against?',choices=choices)
    difficulty = 2
    if opponent == "CPU":

        choices = ['Medium', 'Hard']
        difficulty = easygui.choicebox('How hard CPU do you want to play against?',choices=choices)
        if difficulty == "Medium":
            difficulty = 1
        else:
            difficulty = 2
    screen = Screen().setup(res,res)
    speed(0)
    turtle.bgcolor('purple')
    def line(a, b, x, y):
        turtle.up()
        turtle.goto(a, b)
        turtle.down()
        turtle.goto(x, y)
        turtle.up()

    gap = round((res*0.95) / wide)
    start = -0.5 * res * 0.95
    turtle.Screen().tracer(0, 0)
    ht()
    for i in range(wide+1):
        pos = start + (i * gap)
        line(pos, 0.35 * res, pos, res * -0.5)

    gap2 = round((res*0.82) / tall)
    if gap2 > gap:
        realg = gap
    else:
        realg = gap2
    realg = realg * 0.8
    for x in range(wide):
        for y in range(tall):
            turtle.goto(-0.5 * res + (x * gap + 0.025 * res) + 0.5 * gap, -0.5 * res + (y * gap2 + 0.015 * res) + 0.5 * realg) 
            turtle.dot(realg, 'white')
    up()
    return tall, wide, realg, gap, res, gap2, opponent, difficulty