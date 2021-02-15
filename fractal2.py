# Fractal triangle

import turtle
from fractals.setup import setup


def draw_triangle(step):
    for _ in range(3):
        turtle.forward(1)
        turtle.forward(step)
        turtle.left(120)


def draw_fractal_triangle(step):
    draw_triangle(step)
    step /= 2
    turtle.forward(step)
    turtle.left(60)
    return step


def main():
    the_step = 500

    while the_step > 1:
        the_step = draw_fractal_triangle(the_step)


if __name__ == '__main__':
    setup(speed=100, start_position=(0, -500), hideturtle=True, color='red')
    main()
    turtle.done()
