plik = open('slowa.txt','r')
slowa = plik.readlines()
imie = input('podaj imie ')
nazwisko = input('podaj nazwisko ')
 
def zliczLitery(s):
    wynik = {}
    for i in range(len(s)):
        if wynik.get(s[i]) == None:
            wynik[s[i]] = 0
        wynik[s[i]] += 1
    return wynik
 
def czyUKladalne(w, s):
    ileLiterek = zliczLitery(s)
    for i in range(len(w)):
        #print(w[i])
        if ileLiterek.get(w[i]) == None or ileLiterek.get(w[i])-1 < 0:
            return False
        ileLiterek[w[i]] -= 1
    return True
#print(czyUKladalne('wsprarł','rłsprw'))
 
def usunLitery(w, s):
    ileLiterek = zliczLitery(w)
    wynik = ''
    for i in range(len(s)):
        if ileLiterek.get(s[i]) != None and ileLiterek.get(s[i]) > 0:
            ileLiterek[s[i]] -= 1
            continue
        wynik = wynik + s[i]
    return wynik
 
def sklejWyrazy(imie, nazwisko):
    wynik = imie + nazwisko
    wynik = wynik.lower()
    #sprint(wynik)
    return wynik
 
def szukajParySlow(imienazwisko):
    daSieUlozyc = []
    for i in range(len(slowa)):
        s1 = slowa[i].strip()
        #print(s1)
        #print(s1, imienazwisko)
        if czyUKladalne(s1, imienazwisko):
            daSieUlozyc.append(s1)
            #print(s1)
    for i in range(len(daSieUlozyc)):
        s1 = daSieUlozyc[i]
        s2szukane = usunLitery(s1, imienazwisko)
        for j in range(i,len(daSieUlozyc)):
            s2 = daSieUlozyc[j]
            if len(s2) == len(s2szukane) and czyUKladalne(s2, s2szukane):
                print(s1, s2, ' = ', imie, nazwisko)
szukajParySlow(sklejWyrazy(imie, nazwisko))