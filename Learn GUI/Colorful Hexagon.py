from pickle import TRUE
from turtle import *
bgcolor('black')
speed(0)
hideturtle()
delay(10)
Pen()
colors = ['red','indigo','cyan','yellow','orange','lime']
title('Colorful Hexagon')
for i in range(120):
    pencolor(colors[i%6])
    width(i//100+1)
    forward(i)
    left(59)
done()
