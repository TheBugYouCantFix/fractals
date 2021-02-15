
import turtle
import math
from fractals.setup import setup

step = 500


def draw_rect():
    for _ in range(4):
        turtle.forward(step)
        turtle.right(90)


def draw_rect_fractal():
    global step
    draw_rect()
    step /= 2
    turtle.forward(step)
    turtle.right(45)
    step = math.sqrt(2 * (step ** 2))  # Pythagorean theorem


def main():
    for _ in range(15):
        draw_rect_fractal()


if __name__ == '__main__':
    setup(speed=100, start_position=(0, 0), hideturtle=True, color='red')
    main()
    turtle.done()
