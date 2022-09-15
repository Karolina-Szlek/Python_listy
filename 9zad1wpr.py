############################################
#Wprawka 4 ( środa 6.12, PR)
#Napisz funkcję reprezentant(L), która dla niepustej listy liczb całkowitych dodatnich L
# znajduje najmniejszą liczbę k-cyfrową, gdzie k jest liczbą cyfr największej liczby.
############################################



def reprezentant(L):
    maks=0
    mala=0
    for i in L:
        if len(str(i))>maks:
            maks=len(str(i))
            mala=i
    for i in L:
        if len(str(i))==maks and i<mala:
            mala=i
    return mala
print(reprezentant([1,2,12,22,33]))