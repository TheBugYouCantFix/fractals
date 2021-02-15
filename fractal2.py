# Fractal triangle

import turtle
from fractals.setup import setup

step = 500


def draw_triangle():
    for _ in range(3):
        turtle.forward(1)
        turtle.forward(step)
        turtle.left(120)


def draw_fractal_triangle():
    global step
    draw_triangle()
    step /= 2
    turtle.forward(step)
    turtle.left(60)


def main():
    for _ in range(10):
        draw_fractal_triangle()


if __name__ == '__main__':
    setup(speed=100, start_position=(0, -500), hideturtle=True, color='red')
    main()
    turtle.done()
