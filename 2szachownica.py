def szachownica (n,k):
   for i in range(n):
     for l in range (k):
       for j in range(n):
          print (" "*k, "#"*k,end="")
       print()
     for l in range (k):
       for j in range(n):
         print ("#"*k, " "*k,end="")
       print()


szachownica (4,3)

	


