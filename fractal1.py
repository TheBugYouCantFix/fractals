# Fractal square

import turtle
import math
from setup import setup


def draw_square(step):
    for _ in range(4):
        turtle.forward(step)
        turtle.right(90)


def draw_fractal_square(step):
    draw_square(step)
    step /= 2
    turtle.forward(step)
    turtle.right(45)
    step = math.sqrt(2 * (step ** 2))  # Pythagorean theorem
    return step


def main():
    the_step = 500
    
    while the_step > 1:
        the_step = draw_fractal_square(the_step)


if __name__ == '__main__':
    setup(speed=100, start_position=(0, 0), hideturtle=True, color='red')
    main()
    turtle.done()
