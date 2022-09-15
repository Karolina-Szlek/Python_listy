#########################
#Nie oddawaj      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##############################


plik = open('slowa.txt','r')
slowa = plik.readlines()
imie = input('podaj imie ')
nazwisko = input('podaj nazwisko ')
 
podlugosci = []
wszystkieUkl = []
for i in range(20):
    s = set()
    podlugosci.append(s)
def powstawiajWyrazy(imienazw):
    Literki = zliczLitery(imienazw)
    for i in range(len(slowa)):
        s1 = slowa[i].strip()
        if czyUKladalne(s1, Literki):
            wszystkieUkl.append(s1)
            podlugosci[len(s1)].add(s1)
 
def zliczLitery(s):
    wynik = {}
    for i in range(len(s)):
        if wynik.get(s[i]) == None:
            wynik[s[i]] = 0
        wynik[s[i]] += 1
    return wynik
 
def czyUKladalne(w,Literki):
    #czy moge ulozyc wyraz w
    #ileLiterek = zliczLitery(s)
    ileLiterek = Literki.copy()
    for i in range(len(w)):
        #print(w[i])
        if ileLiterek.get(w[i]) == None or ileLiterek.get(w[i])-1 < 0:
            return False
        ileLiterek[w[i]] -= 1
    return True
#print(czyUKladalne('wsprarł','rłsprw'))
 
def usunLitery(w, s):
    #usuwa z wyrazu s litery wyrazu w
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
    return wynik
 
def szukajTrojek(imienazw):
    for i in range(len(wszystkieUkl)):
 
        drugieSlowo = usunLitery(wszystkieUkl[i],imienazw)
        Literki = zliczLitery(drugieSlowo)
        for j in range(i+1, len(wszystkieUkl)):
 
            if czyUKladalne(wszystkieUkl[j], Literki):
                trzecieSlowo = usunLitery(wszystkieUkl[j], drugieSlowo)
                Literki3 = zliczLitery(trzecieSlowo)
                for e in podlugosci[len(trzecieSlowo)]:
 
                    if czyUKladalne(e, Literki3):
                        print(wszystkieUkl[i], wszystkieUkl[j], e)
sklejone = sklejWyrazy(imie,nazwisko)
powstawiajWyrazy(sklejone)
szukajTrojek(sklejone)