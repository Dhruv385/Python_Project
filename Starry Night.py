import turtle as t
from random import randint.random

def draw_star(points,size,col,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    angle=180-(180/points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

t.Screen().bgcolor('dark blue')
while True:
    ranpts=randint(2,5)*2+1
    ransize=randint(10,50)
    rancol=(random(),random(),random())
    ranx=randint(-350,300)
    rany=randint(-250,250)
    draw_star(ranpts,ransize,rancol,ranx,rany)
