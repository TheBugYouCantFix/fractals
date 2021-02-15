import turtle


def setup(speed=0, start_position=(), color='', hideturtle=False):

    if hideturtle:
        turtle.hideturtle()

    if speed:
        turtle.speed(speed)

    if start_position:
        turtle.penup()
        turtle.goto(start_position[0] - 300, start_position[1] + 300)
        turtle.pendown()

    if color:
        turtle.color(color)
