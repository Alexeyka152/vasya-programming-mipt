import turtle

n=12
for i in range(0, n):
    turtle.shape('turtle')
    turtle.forward(100)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(180)
    turtle.left(360//n)