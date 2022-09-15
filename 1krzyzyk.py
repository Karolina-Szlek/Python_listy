
def krzyzyk(n):   
   for i in range(n):
       print (" "*(n-1), "*"*n, " "*n),
   for i in range(n):
       print ("*"*n, "*"*n, "*"*n, sep=""),
   for i in range(n):
       print (" "*(n-1), "*"*n, " "*n)

krzyzyk(3)

 
