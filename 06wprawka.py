#KÓŁKO KRZYŻYK
from random import *

####Kółko i krzyżyk


def tic_tac_toe():
    plansza = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(plansza[0], plansza[1], plansza[2])
        print(plansza[3], plansza[4], plansza[5])
        print(plansza[6], plansza[7], plansza[8])
        print()

    def p1():
        n = wybierz_pole()
        if plansza[n] == "X" or plansza[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:
            plansza[n] = "X"
    def p2():
        n = randint(1, 9)
        if plansza[n] == "X" or plansza[n] == "O":
            p2()
        else:
            plansza[n] = "O"


    def wybierz_pole():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nPOZA PLANSZĄ! spróbuj ponownie")
                        continue
                except ValueError:
                   print("\nTO NIE LICZBA")
                   continue

    def check_board():
        ruchy_liczba = 0
        for a in win_commbinations:
            if plansza[a[0]] == plansza[a[1]] == plansza[a[2]] == "X":
                print("WYGRAŁEŚ! :)\n")
                print("GRATULACJE!\n")
                return True

            if plansza[a[0]] == plansza[a[1]] == plansza[a[2]] == "O":
                print("PRZEGFAŁEŚ :(\n")
                return True
        for x in range(9):
            if plansza[x] == "X" or plansza[x] == "O":
                ruchy_liczba += 1
            if ruchy_liczba == 9:
                print("REMIS \n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("wybierz, gdzie wpisać krzyżyk..... no wpisz go :)")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        p2()
        print()

    if input("A może NOWA GRA ? (tak/nie)\n") == "tak":
        print()
        tic_tac_toe()

tic_tac_toe()




