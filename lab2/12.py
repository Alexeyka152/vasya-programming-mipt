import turtle

def duga(r,l):
    turtle.circle(r, l)

turtle.shape('turtle')

turtle.speed(10)
turtle.penup()
turtle.goto(-250,0)
turtle.pendown()
turtle.right(90)
for i in range(1,10):
    duga(25, -180)
    duga(8,-180)