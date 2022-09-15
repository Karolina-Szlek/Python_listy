from math import *
from turtle import *

tracer(0,1)
def start_z(x,y):
  pu()
  goto(x,y)
  pd()

def kwadrat(bok, color):
  fillcolor(color)
  begin_fill()
  for i in range(4):
    fd(bok)
    rt(90)
  end_fill()
  fd(bok)
  # dopisz , żeby schodził na początek kolejnej linii
  

colormode(255)

elementy = open("lala.txt")

linie= list(elementy)
start_z(-250,300)

for x in linie:
  pixels = x.split()
  for pix in pixels:
    kwadrat(10,eval(pix))
  fd(-10*len(pixels))
  rt(90)
  fd(10)
  lt(90)
#   pix = linia.split()
#   print(pix)
   

# for line in elementy:
#   print(line)
	# for j in (line):
  #   listy[i]
		# kwadrat(10,eval(listy[i][j]))



# kwadrat(10, eval((lista[i][j])))
	




input()

 

