####################################################
# Spełnianie formuł logicznych
####################################################


def ciagi_binarne(N):
  if N == 0:
    return [ [] ]
  return [ [b] + c for b in [True, False] for c in ciagi_binarne(N-1)]  
    
# 2 --> [ [False, False], [False, True], [True, False], [True, True] ]    


def wartosciowania(zmienne):
  cb = ciagi_binarne(len(zmienne))
  return [ dict(zip(zmienne, ciag)) for ciag in cb]
  
def wartosc_formuly(F, wart):
  F = F.replace('*', ' and ')
  F = F.replace('+', ' or ')
  F = F.replace('-', ' not ')
  F = F.replace('T', 'True')#
  F = F.replace('F', 'False')#
  #print (F, wart)
  return eval(F, wart)


def spelnialna(F):
  L = F.split( )
  zmienne = set(L) - set('+*()-TF ')
  for wart in wartosciowania(zmienne):
    if wartosc_formuly(F, wart) == True:
      return True
  return False    
  
def tautologia(F):# tautologia
  L = F.split( )
  zmienne = set(L) - set('+*()-TF ')
  for wart in wartosciowania(zmienne):
    if wartosc_formuly(F, wart) == False:
      return False
  return True   
  
print (spelnialna(' pq *  ( - qe ) * rw'))
print(tautologia(' p * r'))



   
