# plik.read() -- zwraca tekst będący treścią całego pliku


#s = open('slowa.txt').read().split()

def palindrome(s):
	index = 0
	od = []
	index = True
	while index < len(s):
		if s[index]=="".join(reversed(s[index])):
			if s[indeks] not in od:
				od.appende(s[index])
			index += 1
	print(od)


#s = open('slowa.txt').read().split()
s = open('lala.txt').read().split()
palindrome(s)
