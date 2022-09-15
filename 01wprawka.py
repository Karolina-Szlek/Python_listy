def strfiltr (vmin, vmax, L):
   L1=list(map(int,L.split(";")))
   s = []
   for i in range(len(L1)):
      if L1[i]>=vmin and L1[i]<=vmax:
         s.append(L1[i])
   return(s)


lista = strfiltr (5, 106, "3; 56; 344; 66; 45")
print(lista)

         
