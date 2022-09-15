def merge(L1, L2):
	wynik = []	
	l1 = 0
	l2 = 0
	while l1 < len(L1) or l2 < len(L2):
		if l1 >= len(L1):
			wynik.append(L2[l2])
			l2 = l2+1
		elif l2 >= len(L2):
			wynik.append(L1[l1])
			l1 = l1+1
		elif L1[l1] < L2[l2]:
			wynik.append(L1[l1])
			l1 = l1+1
		elif L2[l2] < L1[l1]:
			wynik.append(L2[l2])
			l2 = l2+1
	return wynik


L1 = [1,3,4,6,6,6,7]
L2 = [0,2,5,8,8,8,9,9,9,9,9,9,9,9]

print(merge(L1, L2))
