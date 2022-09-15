

def pierwszy_dzielnik(n):
	czypierwsze = 0
	pierwsze = []
	dzielnik = [] 
	razem =[]     
	for p in range(0, n+1):
		czypierwsze = 0
		for i in range(2, p):
			if p % i == 0:
				czypierwsze = 1
				break
		if czypierwsze == 0:
			pierwsze.append(p)
	for i in range(1,n+1):
		if n % i == 0:
			dzielnik.append(i)
	for i in pierwsze:
		if i in dzielnik:
			razem.append(i)
#	print(pierwsze)
#	print(dzielnik)
	print(razem)







pierwszy_dzielnik(65)
pierwszy_dzielnik(33)
pierwszy_dzielnik(27)
pierwszy_dzielnik(15)



