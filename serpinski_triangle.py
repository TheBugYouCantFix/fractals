from turtle import *

left(60)
hideturtle()
speed(100)


def triangle(step, x, y):
    penup()
    goto(x, y)
    pendown()

    if step < 50:
        return

    # drawing triangle
    for _ in range(3):
        forward(step)
        right(120)

    return triangle(step / 2, x, y), \
        triangle(step / 2, x + step / 4, y + (step * 3**0.5) / 4), \
        triangle(step / 2, x + step / 2, y)


if __name__ == '__main__':
    triangle(500, -200, -200)
