from turtle import *
goto(0,0)
pensize(5)
speed(0)
ht()
for i in range(4):
    fd(270)
    lt(90)
goto(0,0)
pensize(1)
for j in range(9):
    for g in range(9):
        for k in range(4):
            pendown()
            fd(30)
            lt(90)
        penup()
        goto(j*30,g*30)
goto(0,0)
pensize(3)
for a in range(3):
    for b in range(3):
        for k in range(4):
            pendown()
            fd(90)
            lt(90)
        penup()
        goto(a*90,b*90)
mainloop()
