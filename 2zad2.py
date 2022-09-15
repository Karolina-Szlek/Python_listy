from random import randint

def kostka():
  return randint(1,6)

licznik = 0 
dc = 0
k2 = 0

while True:
  licznik += 1
  k1 = kostka()
  if k2 < k1:
    dc+= 1
  else :
    dc = 0
  k2 = k1
  if dc== 5:
    break
  print (licznik, k1)
  if licznik== 100:
    dc= 0
    k2= 0
    licznik = 0
    print ("KOLEJNA GRA")
if dc== 5 :
  print("Wygrana")
else :
  print("Przegrana")



########GRA ZE SMOKIEM
