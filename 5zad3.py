def only_one(L):
	wynik = []
	for element in L:
		if element not in wynik:
			wynik.append(element)
	return wynik

L = [1,2,3,1,2,3,8,2,2,2,9,9,4]

print(only_one(L))












