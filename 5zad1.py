
def F(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1



def energia(m):
    indeks = 0
    while m != 1:
        m = F(m)
        indeks += 1
    return indeks



def analizaCollatza(a, b):
    suma = 0			# przyda się do policzenia średniej energii
    Lenergii = []		#lista z energiami liczb z [a,b]
    for i in range(a,b):
        e = energia(i)
        suma = suma + e
        Lenergii.append(e)
    if len(Lenergii) % 2 != 0:
        mediana = sorted(Lenergii)[len(Lenergii)//2] # sorted posortuje enerdie rosnąco, bo tak z medianą trzeba
    else:
        mediana = (sorted(Lenergii)[len(Lenergii)//2] + sorted(Lenergii)[len(Lenergii)//2-1])//2.0
        
    print("Srednia energia: " , suma/len(Lenergii))
    print("Mediana energii: ", mediana)
    print("Maksymalna energia: ", max(Lenergii))
    print("Mininalna energia: ", min(Lenergii))
 
analizaCollatza(1,11)






















