from turtle import *
from local import *

def get_color_choice():
    '''Function to select the fill color of the hexagon'''
    while True:
        color_choice = input(COLOR_CHOICE_INPUT)
        try:
            if color_choice == RED:
                color_choice_user = 'red'
                break
            if color_choice == BLUE:
                color_choice_user = 'blue'
                break
            if color_choice == GREEN:
                color_choice_user = 'green'
                break
            if color_choice == YELLOW:
                color_choice_user = 'yellow'
                break
            if color_choice == ORANGE:
                color_choice_user = 'orange'
                break
            if color_choice == PURPLE:
                color_choice_user = 'purple'
                break
            if color_choice == PINK:
                color_choice_user = 'pink'
                break
            else:
                print("'{}'".format(color_choice), COLOR_CHOICE_WRONG)
        except Exception:
            print("'{}'".format(color_choice), COLOR_CHOICE_WRONG)
    return color_choice_user

def get_num_hexagons():
    '''Function to enter the number of hexagons'''
    while True:
        try:
            n = int(input(HEXAGONS_INPUT))
            if n < 4 or n > 20:
                print(HEXAGONS_INPUT_WRONG)
            else:
                break
        except Exception:
            print(HEXAGONS_INPUT_WRONG)
    return n

def draw_hexagon(x, y, side_len, coloruser):
    '''Hexagon drawing function'''
    begin_fill()
    for _ in range(6):
        forward(side_len)
        right(60)
    up()
    goto(x, y)
    down()
    fillcolor(coloruser)
    end_fill()

def color():
    '''Function to select the fill color of each hexagon'''
    if a % 2 == 0:
        coloruser = color_1
    else:
        coloruser = color_2
    return coloruser

print(COLORS)
print(" " + RED)
print(" " + BLUE)
print(" " + GREEN)
print(" " + YELLOW)
print(" " + ORANGE)
print(" " + PURPLE)
print(" " + PINK)

setup = 500, 500
x = -250
y = 250
a = 1
i = 1

color_1 = get_color_choice()
color_2 = get_color_choice()
import math
n = get_num_hexagons()
d = int(500 / n)
side_len = d / math.sqrt(3)
left(30)
up()
goto(x, y)
down()

for _ in range(n):
    if i % 2 == 1:
        for _ in range(n):
            x += d
            a += 1
            coloruser = color()
            draw_hexagon(x, y, side_len, coloruser)

        i += 1
        y -= side_len * 1.5
        x -= d / 2
        up()
        goto(x, y)
        down()
    else:
        for _ in range(n):
            coloruser = color()
            x -= d
            draw_hexagon(x, y, side_len, coloruser)
            a += 1
        a += 1
        i += 1
        y -= side_len * 1.5
        x += d / 2
        up()
        goto(x, y)
        down()

