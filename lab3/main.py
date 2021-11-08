import turtle
from math import radians, sin, cos

V = 50
phi = radians(60)
k = 0.7
dt = 0.1
g = -9.8

x, y = 0, 0
Vx = V * cos(phi)
Vy = V * sin(phi)

turtle.shape('circle')
turtle.turtlesize(0.1)

while y > 10 or Vx**2 + Vy**2 > 1:
    if y < 0 and Vy < 0:
        Vx = k*Vx
        Vy = -k*Vy
    x += Vx*dt
    y += Vy*dt + g*dt**2/2
    Vy += g*dt
    turtle.goto(x, y)
