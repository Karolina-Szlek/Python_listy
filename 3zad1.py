#######PIERWSZE LICZBY SZCZĘŚLIWE


def pierwsze(limit):
    tab=[]       
    for i in range(2,limit):    
        for j in tab:            
            if i % j == 0: break 
        else: 
            yield i              
            tab.append(i)  
licz=0      

for i in pierwsze(100000):
	if '777' in str(i):
             licz+=1
             print(i)

print("było ich:", licz)




##################################################
#tłumaczenie co się tu dziej
#####################################





def pierwsze(limit):
    tab=[]       # robocza lista liczb pierwszych, poniewaz jest to generator to sie zachowuje miedzy wywolaniami
    for i in range(2,limit):     #  rozwazamy liczby od 2 w górę ale mniejsze niż limit
        for j in tab:            # dla wszystkich do tej pory znalezionych liczb pierwszych
            if i % j == 0: break # sprawdzamy czy ktoras jest dzielnikiem, jesli jest to i nie jest liczba pierwsza
        else: # a jesli nie ma mniejszej od i liczby pierwszej z tab ktora jest jej dzielnikiem to i jest liczba pierwsza
            yield i              
            tab.append(i)  
licz=0      

for i in pierwsze(100000):
	if '777' in str(i):
             licz+=1
             print(i)

print("było ich:", licz)







