from turtle import fd, bk, lt, rt, pu, pd, speed
from random import randint
speed('fastest')

def wykres(n):
	l = randint(20,150)
	for i in range(2):	
		fd(n)
		lt(90)
		fd(l)
		lt(90)
	pu()
	fd(2*n)
	pd()
	

def calosc(n):
	for i in range(n):
		wykres(10)

calosc(25)




x = input('Żeby dalej pracować wciśnij ENTER')
