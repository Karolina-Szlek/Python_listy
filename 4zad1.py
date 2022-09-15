#####TURTLE RYSUJE KOLOROWĄ KOSTKE Z MAŁYCH KOLOROWYCH KOSTECZEK

from turtle import *
import random



tracer(0,1)

def kwadrat(bok, kolor):
  fillcolor(kolor)
  begin_fill()
  for i in range(4):
    fd(bok)
    rt(90)
  end_fill()

BOK = 30



for i in range(10):
  R = random.random()
  G = random.random()
  B = random.random()
  
  kwadrat(BOK, (R,G,B))
  fd(BOK)
lt(180)
for i in range(10):
  R = random.random()
  G = random.random()
  B = random.random()
  
  kwadrat(BOK, (R,G,B))
  fd(BOK)
rt(90)
fd(2*BOK)
rt(90)
for i in range(10):
  R = random.random()
  G = random.random()
  B = random.random()
  
  kwadrat(BOK, (R,G,B))
  fd(BOK)
lt(180)
for i in range(10):
  R = random.random()
  G = random.random()
  B = random.random()
  
  kwadrat(BOK, (R,G,B))
  fd(BOK)
rt(90)
fd(2*BOK)
rt(90)
for i in range(10):
  R = random.random()
  G = random.random()
  B = random.random()
  
  kwadrat(BOK, (R,G,B))
  fd(BOK)
lt(180)
for i in range(10):
  R = random.random()
  G = random.random()
  B = random.random()
  
  kwadrat(BOK, (R,G,B))
  fd(BOK)
rt(90)
fd(2*BOK)
rt(90)
for i in range(10):
  R = random.random()
  G = random.random()
  B = random.random()
  
  kwadrat(BOK, (R,G,B))
  fd(BOK)
lt(180)
for i in range(10):
  R = random.random()
  G = random.random()
  B = random.random()
  
  kwadrat(BOK, (R,G,B))
  fd(BOK)
rt(90)
fd(2*BOK)
rt(90)
for i in range(10):
  R = random.random()
  G = random.random()
  B = random.random()
  
  kwadrat(BOK, (R,G,B))
  fd(BOK)
lt(180)
for i in range(10):
  R = random.random()
  G = random.random()
  B = random.random()
  
  kwadrat(BOK, (R,G,B))
  fd(BOK)
rt(90)
fd(2*BOK)
rt(90)
input()  


