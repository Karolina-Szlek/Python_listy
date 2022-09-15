

n = int(input())
T = []
zmienna = 0

for i in range(n):
	T.append(-1)


def isfree( x, y):
	for i in range(x):
		if T[i]-i==y-x or T[i]+i==y+x or T[i]==y:
			return 0
	return 1



def szukaj():
	T[0] = 0
	k = 1
	zmienna = 0
	while k < n and k >= 0:
		T[k]+=1
		while T[k]<n and not isfree(k,T[k]):
			T[k]+=1

		if T[k]<n: 
			k+=1 
		else:
			T[k]=-1; k-=1 
		if k == n:
			zmienna+=1
			k-=1
			T[k] +=1
	return zmienna
print(szukaj())