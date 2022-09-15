

def PPN(s):
    litery = []
    numery = []
    wynik = []
    ilość = 0
    slowo = {}
    for l in s:
        if l != "":
         litery.append(l)
    for i in litery:
        if i not in slowo:
            ilość += 1  # dla każdej nowej litery będzie podawać wartość o 1 więcej od poprzedniej
            slowo[i] = str(ilość)
        numery.append(slowo[i])
    wynik = '-'.join(numery)
    print(s, wynik)



PPN("bla bpa")
PPN("kakalilo")