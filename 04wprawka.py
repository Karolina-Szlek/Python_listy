#https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

maxpion = h - 1
minpion = 0
maxpoziom = w - 1
minpoziom = 0

x = x0
y = y0
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if bomb_dir == "U":
        maxpion = y - 1    
        y = (maxpion + minpion)//2    
        
    if bomb_dir == "D":
        minpion = y + 1
        y = (maxpion + minpion)//2 
        
    if bomb_dir == "R":
        minpoziom = x + 1 
        x = (maxpoziom + minpoziom)//2     
        
    if bomb_dir == "L":
        maxpoziom = x - 1
        x = (maxpoziom + minpoziom)//2
        
    if bomb_dir == "UR":
        maxpion = y - 1  
        minpoziom = x + 1 
        y = (maxpion + minpion)//2       
        x = (maxpoziom + minpoziom)//2 
        
    if bomb_dir == "DR":
        minpion = y + 1
        minpoziom = x + 1
        y = (maxpion + minpion)//2  
        x = (maxpoziom + minpoziom)//2 
        
    if bomb_dir == "DL":
        minpion = y + 1
        maxpoziom = x - 1
        y = (maxpion + minpion)//2  
        x = (maxpoziom + minpoziom)//2
        
    if bomb_dir == "UL":
        maxpion = y - 1 
        maxpoziom = x - 1
        y = (maxpion + minpion)//2   
        x = (maxpoziom + minpoziom)//2
  
  
     
    print(x,y)        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # the location of the next window Batman should jump to.
