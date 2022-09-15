###LOSUJE RANDOMOWĄ PERMUTACJE 


from random import randint


def randperm(n):
	wynik = []
	while len(wynik) < n:
		for i in range(n):
			l = randint(0,n-1)
			if l not in wynik:
				wynik.append(l)
	return wynik
	

print(randperm(10))
print(randperm(10))
print(randperm(10))




###LOSUJE RANDOMOWĄ PERMUTACJE 
'''lepsza wersja, ale SPRAWDŹ czy działa, zamienia elementy miejscami'''

L = list(range(n))

for i in range(n):
	j = randint(0,n)
	L[i], L[j] = L[j], L[i]
