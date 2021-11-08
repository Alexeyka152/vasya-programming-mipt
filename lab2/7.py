import turtle

turtle.shape('turtle')

z=0.1
for i in range(0, 100):
    turtle.forward(z)
    turtle.left(10)
    z=z+0.03