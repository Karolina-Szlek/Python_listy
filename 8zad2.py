#The method get() returns a value for the given key. 
#If key is not available then returns default value None."INTERNET"

#def countLetter(s):
#    d = {}
#    L = []
#    for letter in s: 
#        d[letter] = s.count(letter)
#    for k in sorted(d):
#        L.append(k)
#        return (k + ': ' + str(d[k]))
#    print(L)

def countLetter(s):
    dic = {}
    for letter in s: 
        dic[letter] = s.count(letter)
    return dic


def czyUlozy(w, s):
    Litery = countLetter(s)
    for i in range(len(w)):
        if Litery.get(w[i]) == None or Litery.get(w[i])-1 < 0: # jeśli w miejscu litery z 2-go słowa nie ma nic lub jest mniej niż 1 (np.0) 
            return "Nie powstało"
        Litery[w[i]] -= 1
    return "Powstało"
  






print(czyUlozy('kajak','jakaj'))
print(czyUlozy('maram','ramam'))