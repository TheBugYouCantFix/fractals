# Fractal square

import turtle
import math
from fractals.setup import setup

step = 500


def draw_square():
    for _ in range(4):
        turtle.forward(step)
        turtle.right(90)


def draw_fractal_square():
    global step
    draw_square()
    step /= 2
    turtle.forward(step)
    turtle.right(45)
    step = math.sqrt(2 * (step ** 2))  # Pythagorean theorem


def main():
    for _ in range(15):
        draw_fractal_square()


if __name__ == '__main__':
    setup(speed=100, start_position=(0, 0), hideturtle=True, color='red')
    main()
    turtle.done()
