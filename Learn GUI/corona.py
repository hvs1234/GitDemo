from pickle import TRUE
from turtle import *
bgcolor('black')
speed(0)
hideturtle()
delay(50)
pencolor('slate grey')
penup()
goto(0,200)
pendown()
a=0; b=0;
while TRUE:
    forward(a)
    right(b)
    a+=3
    b+=1
    if(b==210):
        break;
done()
