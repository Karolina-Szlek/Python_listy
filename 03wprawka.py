import sys
import math
import random



# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
L = []
n = int(input())
for i in range(n):
    for j in input().split(): #wpisujesz całe wiersze
        c = int(j)
        L.append(c)



prze1 = 0
x = 0
while x < len(L):
    prze1 += L[x]
    x += n+1


prze2 = 0
z = 0
while z < len(L):
    prze2 += L[z]
    z += n+1


kolumnlist = []
for i in range(n):
    pion = 0
    y = i
    while y < len(L):
         pion += L[y]
         y += n
    kolumnlist.append(pion)



wiersze = []
w = 1
for w in range(n):
    w = w*n



# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(prze1)
print(prze2)
print(L)
print(kolumnlist)