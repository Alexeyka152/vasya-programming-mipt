import turtle
from random import *

turtle.shape('turtle')
turtle.color('red')
i = 1
while i > 0:
    turtle.forward(randint(10, 30))
    turtle.left(randint(0, 360))