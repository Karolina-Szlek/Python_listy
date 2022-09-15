
elementy = open("7zad3tekst.txt" , encoding="utf-8").read()
elementy.replace(",", "") # nie działa
la = elementy.split()
secik = set(la)
najwiekszy=max(secik, key=len)
wynik = []
for x in secik:
	if len(x)==len(najwiekszy):
		wynik.append(x) 


print(sorted(wynik))


#######################
#wlicza znaki do długości wyrazu :/
#######################
elementy = open("7zad3tekst.txt" , encoding="utf-8").read().split( )
secik = set(elementy)#a chce ty elementy.split
najwiekszy=max(secik, key=len)
wynik = []
for x in secik:
	if len(x)==len(najwiekszy):
                wynik.append(x) 

print(elementy)
#print(sorted(wynik))




