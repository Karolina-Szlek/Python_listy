from turtle import *
import random


kolory = ['purple', 'blue','green', 'yellow',  'pink', 'magenta', 'cyan', 'indigo']

def kwadrat(bok):
   begin_fill()
   for i in range(4):
     fd(bok)
     rt(90)
   end_fill()

c = 0  
def murek(s,bok):
  global c
  for a in s:
    color('black', kolory[c])
    if a == 'f':
       kwadrat(bok)
       fd(bok)
       c = (c + 1) % len(kolory) #kolory kostek jak w kolory i powtarzają się po koleii
    elif a == 'b':
       kwadrat(bok)
       fd(bok)  
       c = random.randint(0, 7)   
    elif a == 'l':
       bk(bok)
       lt(90)
    elif a == 'r':
      rt(90)
      fd(bok)

      


ht()
tracer(0,0) 

#tracer(0,0) # szybkie rysowanie    
#murek('fffffffffrfffffffffflfffffffffrfffffl',10)   
#murek(4 * 'fffffr', 14)   





#d_kwadrat(4)
#murek("f", 15)
#murek("ffrfrf",15)
#murek("ffrfrffrffrff", 15)
#murek("ffrfrffrffrfffrfffrfff", 15)



#Kostka
murek("bbrbrbbrbbrbbbrbbbrbbbbrbbbbrbbbb", 20)



#Spiralka 
#murek("fffffffffrffffffffffrffffffffrfffffffrfffffrffffrffrf",30)
     

update() # uaktualnienie rysunku

input()
