

#LISTA 1 ZADANIE 2

#SUMA LICZB W WYNIKU SILNI 4-100


def silnia(n):
    res = 1
    for i in range(n):
        res = res * (i+1)
    return res


def silnia1(n):
	wynik = 1
	if n < 0:
	  return False
	elif n == 0:
	  return 1
	else:
	  return n * silnia(n-1)


#def suma(L):
	#wynik =0
	#for j in range (len(L)):
	    #wynik==len(L[j])
	#return wynik




print

for i in range(4,101):
    print (i, "!", "ma", len(str(silnia1(i))), end= " ")
    
   # for j in range (len(L)):
       #print (L[j] , end=" ")
    print ("cyfry", end=" ")
    print()    



