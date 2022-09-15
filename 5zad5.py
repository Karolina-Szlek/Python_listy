
from random import randint

ilewygrana = 0
def kostka():
  return randint(1,6)
def gra():
	licznik = 0 
	dc = 0
	k2 = 0
	indeks = 0
	while True:
	  licznik += 1
	  k1 = kostka()
	  if k2 < k1:
	    dc+= 1
	  else :
	    dc = 1
	  k2 = k1
	  if dc== 5:
	    indeks = 50
	  if licznik== 100:
	    print (indeks)
	    break
	  if indeks == 50:
	    

if indeks == 50:
	ilewygrana += 1
	print(ilewygrana)


def sprawdzam(n):
  for i in range(n):
    gra()

sprawdzam(10)
    
