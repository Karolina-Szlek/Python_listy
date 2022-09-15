from turtle import fd, bk, lt, rt, pu, pd, speed

speed('fastest')

def rozeta(N, a, b):
  for i in range(N):
    fd(b)
    bk(b)
    rt (360 / N)

def rozeta1(N, a, b):
  for i in range(N):
    fd(b)
    rozeta(N, a//2, b//5)
    bk(b)
    rt (360 / N)

rozeta1(10, 30, 100)


x = input('Żeby dalej pracować wciśnij ENTER')


#####TURTLE RYSUJE PŁATEK ŚNIEGU
