
#Szyfrowanie metodą Cezar

def cesar(s, k):
    alphabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
    k = k % 32 # jakby k było > 32
    shifted_alphabet = alphabet[k:] +alphabet[:k]
    encryption = dict(zip(alphabet, shifted_alphabet,))
    in_code = ''
    for letter in s:
        in_code += encryption[letter]
    return(in_code)



print(cesar(cesar('karolina',60), -60))
