import turtle

symbols = {
    '0': [(0, 0), (1, 0), (1, -2), (0, -2), (0, 0)],
    '1': [(0, -1), (1, 0), (1, -2)],
    '2': [(0, 0), (1, 0), (1, -1), (0, -2), (1, -2)],
    '3': [(0, 0), (1, 0), (0, -1), (1, -1), (0, -2)],
    '4': [(0, 0), (0, -1), (1, -1), (1, 0), (1, -2)],
    '5': [(1, 0), (0, 0), (0, -1), (1, -1), (1, -2), (0, -2)],
    '6': [(1, 0), (0, -1), (0, -2), (1, -2), (1, -1), (0, -1)],
    '7': [(0, 0), (1, 0), (0, -1), (0, -2)],
    '8': [(0, -1), (1, -1), (1, -2), (0, -2), (0, 0), (1, 0), (1, -2)],
    '9': [(1, -1), (0, -1), (0, 0), (1, 0), (1, -1), (0, -2)]
}

def draw_symbol(s, scale=10):
    x0, y0 = turtle.xcor(), turtle.ycor()
    turtle.up()
    turtle.goto(x0 + symbols[s][0][0] * scale, y0 + symbols[s][0][1] * scale)
    turtle.down()
    for x, y in symbols[s]:
        turtle.goto(x0 + x * scale, y0 + y * scale)


def draw_number(n, scale = 10):
    x0, y0 = turtle.xcor(), turtle.ycor()
    delta_x = 0
    for i in str(n):
        draw_symbol(i, 10)
        delta_x += scale * 2
        turtle.up()
        turtle.goto(x0 + delta_x, y0)


turtle.color('blue')
draw_number(141700)
turtle.done()