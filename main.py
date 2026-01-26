import math
from turtle import *

def hearta(k):
    return 16 * math.sin(k)**3

def heartb(k):
    return 13 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

speed(0)
bgcolor("Black")
color("#f73487")

penup()
goto(0, 0)
pendown()

for i in range(6000):
    goto(hearta(i) * 20, heartb(i) * 20)
    goto(0, 0)

done()
