from pickle import FALSE
from turtle import *
bgcolor('black')
resizemode()
speed(0)
hideturtle()
for i in range(120):
    color('yellow')
    circle(i)
    color('red')
    delay(30)
    circle(i*0.8)
    right(3)
    forward(3)
done()
