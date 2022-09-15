from turtle import *
import random
colormode(255)
speed(1)
limit = 5
wsp = (2 ** 0.5) * 0.5
kolory = ['purple','cyan', 'fuchsia','indigo', 'blue','aquamarine', 'aqua']
#kolory = [ 'red', 'yellow', 'green', 'orange', 'black', 'pink', 'blue']
def kwadrat(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(bok)
        lt(90)
    end_fill()

def drzewo(bok, glebokosc):
    
    cl = 0
    kwadrat(bok, kolory[(cl + glebokosc) % 7])
    
    if glebokosc +1 <= limit:
        pu()
        lt(90)
        fd(bok)
        rt(45)
        pd()
        drzewo(bok*wsp, glebokosc + 1)
        pu()
        fd(bok*wsp)
        rt(90)
        pd()
        drzewo(bok*wsp, glebokosc + 1)
        pu()
        lt(90)
        bk(bok*wsp)
        lt(45)
        bk(bok)
        rt(90)
        pd()

pu()
goto(-100, -350)
pd()
drzewo(180, 0)

input()





















#colours = [(255,0,0),(205,87,0),(255,128,0),(255,191,0), (254,254,51),(124,252,0),(51,204,102),(48,213,200),(0,255,255),(0,180,247),(0,127,255),(0,39,194),(0,0,255)]
