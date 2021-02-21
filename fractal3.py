import turtle
import math
from setup import setup

screen = turtle.Screen()
screen.setup(1300, 800)


def draw_square(step):
    for _ in range(4):
        turtle.forward(step)
        turtle.left(90)


def draw_triangle(step):
    radius = math.sqrt(2 * (step ** 2)) / 2
    turtle.left(45)
    turtle.forward(radius)
    turtle.right(90)
    turtle.forward(radius)


def draw_circle(step):
    turtle.forward(step / 2)
    radius = math.sqrt(2 * (step ** 2)) / 2
    turtle.right(90)
    turtle.penup()
    turtle.forward(radius - (step / 2))
    turtle.pendown()
    turtle.left(90)
    turtle.circle(radius)
    turtle.left(90)
    turtle.penup()
    turtle.forward(radius - (step / 2))
    turtle.left(90)
    turtle.forward(step / 2)
    turtle.right(180)
    turtle.pendown()


def main():
    the_step = 250
    for _ in range(10):
        draw_square(the_step)
        draw_triangle(the_step)
        turtle.left(135)
        turtle.forward(the_step)
        turtle.left(90)
        draw_triangle(the_step)
        turtle.left(135)
        turtle.forward(the_step)
        turtle.left(90)
        draw_circle(the_step)

        the_step -= 25


if __name__ == '__main__':
    setup(speed=1000, start_position=(250, -300), hideturtle=True, color='red')
    for _ in range(4):
        main()
        turtle.left(90)

    turtle.done()
