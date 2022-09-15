'''NIE ZROBIONE'''


def pierwsze(limit):
    tab=[]       
    for i in range(2,limit):    
        for j in tab:            
            if i % j == 0: break 
        else: 
            yield i              
            tab.append(i) 



def szczesliwa(n):
   licz=0 
   L=[]   
   wynik=[]  
   for i in pierwsze(n):
      if '777' in str(i):
         L.append(i)
         licz+=1
   print(licz)
   for i in L:
      if len(L[i]) == 10:
         wynik.append(L[i])
   print(wynik)
   
szczesliwa(9999)
#########################3

