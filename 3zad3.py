
L="ala ma kota (perskiego)!"

niezapisz=0
wynik=[]
for i in range(len(L)):
   if L[i]=="(":
      niezapisz=1
   if niezapisz==0:
      wynik.append(L[i])
   if L[i]==")":
      niezapisz=0 
wynik="".join(wynik)

   
print(wynik)
 

#####USÓWANIE NAWIASÓW I TEGO CO W NAWIASACH
