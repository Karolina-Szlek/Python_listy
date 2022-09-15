###########################################################	
def only_one(L):
    wystapienia = []
    wynik = []
    pojedyncze = []
    for i in range(len(L)):
        wystapienia.append((L[i],i))
    wystapienia.sort()
 
    for i in range(len(wystapienia)):
        if i == 0 or wystapienia[i][0] != wystapienia[i-1][0]:
            pojedyncze.append((wystapienia[i][1],wystapienia[i][0]))
    pojedyncze.sort()
 
    for i in range(len(pojedyncze)):
        wynik.append(pojedyncze[i][1])
       
    return wynik
 
print(only_one([1,2,3,1,2,3,8,2,2,2,9,9,4]))
