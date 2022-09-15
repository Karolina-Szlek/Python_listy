
plik = open('slowa.txt')
linie = plik.read()
slowa = linie.split()
#print(slowa)


#def riddle(word1, word2):
 #   num1 =[]
 #   num2 = []
    #w1 = list(word1)
    #w2 = list(word2)
 #   for i in word1:
 #       x = ord(i)
 #       num1.append(x)
 #   for j in word2:
 #       y = ord(j)
 #       num2.append(y)
 #   print(num1, num2)

#riddle('ala', 'ola')

def rozwiaz(zadanie):
    nowezadanie
    litery = ()
    litery = set(zadanie) - set('+-=*/ ')
    if len(litery) > 10:
        return {}
    napis = zadanie