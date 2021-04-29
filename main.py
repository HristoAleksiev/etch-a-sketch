from turtle import Turtle, Screen

tur = Turtle()
scr = Screen()
scr.listen()


def move_forward():
    tur.forward(10)


def move_backward():
    tur.backward(10)


def move_left():
    tur.left(10)


def move_right():
    tur.right(10)


def clear_screen():
    tur.clear()


def reset_position():
    tur.penup()
    tur.home()
    tur.pendown()


def listen_for_input():
    scr.onkeypress(fun=move_forward, key="Up")
    scr.onkeypress(fun=move_left, key="Left")
    scr.onkeypress(fun=move_backward, key="Down")
    scr.onkeypress(fun=move_right, key="Right")
    scr.onkeypress(fun=clear_screen, key="c")
    scr.onkeypress(fun=reset_position, key="r")


listen_for_input()
scr.exitonclick()
