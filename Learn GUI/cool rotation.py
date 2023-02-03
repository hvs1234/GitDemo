from turtle import *
from colorsys import *
bgcolor('black')
tracer(100)
pensize(1)
h = 0.5
delay(100)
for i in range(250):
    c = hsv_to_rgb(h,1,1)
    h = 0.0008
    fillcolor(c)
    begin_fill()
    fd(i)
    lt(100)
    circle(30)
    for j in range(2):
        fd(i*j)
        rt(109)
    end_fill()
