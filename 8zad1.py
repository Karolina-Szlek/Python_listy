
def tlumacz(txt):
  wynik = []
  for p in txt.split():
    if p in pol_ang:
      wynik.append(pol_ang[p])
    else:
      wynik.append('?' + p + "?")
  return ' '.join(wynik)
     

pol_ang = {} # pusty słownik
 

popularnosc = {}
plik = open('korpusbrowna.txt').readlines()
 

for tekst in plik:
  x = tekst.split(' ')
  for slowo in x:
    if popularnosc.get(slowo) == None:
      popularnosc[slowo] = 0
    else:
      popularnosc[slowo] += 1



for x in open('pol_ang.txt'):
  x = x.strip()
  L = x.split('=')
  if len(L) != 2:
    continue
  pl, en = L # lista par np. ([1,3], [2,4]...)
  if pl not in pol_ang: 
    pol_ang[pl] = en 
  else:
    if popularnosc.get(pol_ang[pl]) == None:
      pol_ang[pl] = en
    if popularnosc.get(en) != None and popularnosc[pol_ang[pl]] < popularnosc[en]:
      pol_ang[pl] = en
 



zdanie = 'dziewczyna spotkać chłopiec i pójść do małe kino '

print (tlumacz(zdanie))



