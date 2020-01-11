#Simple Pong in Python 3 for Beginners
# Tutorial by @TokyoEdTech, Author: Kassy Pak

import turtle

window = turtle.Screen()
window.title("Pong by Kassy Pak")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


# Paddle A ---------------------------------------
pad_A = turtle.Turtle()

# sets paddle to possible maximum speed
pad_A.speed(0)
pad_A.shape("square")
pad_A.color("white")
pad_A.shapesize(stretch_wid=5, stretch_len=1)
pad_A.penup()

# sets paddle to left starting position
pad_A.goto(-350, 0)


# Paddle B ---------------------------------------
pad_B = turtle.Turtle()
pad_B.speed(0)
pad_B.shape("square")
pad_B.color("white")
pad_B.shapesize(stretch_wid=5, stretch_len=1)
pad_B.penup()

# sets paddle to right starting position
pad_B.goto(350, 0)


# Ball -------------------------------------------
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()


# Pen --------------------------------------------
score_A = 0
score_B = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))

# sets paddle to center starting position
ball.goto(0, 0)

# Moves balls by two pixels
ball.dx = 2
ball.dy = -2


# Function ---------------------------------------
def pad_A_up():  # Need to know the current y-coordinate to move paddle
    currentA_y = pad_A.ycor()
    currentA_y += 20
    pad_A.sety(currentA_y)


def pad_A_down():
    currentA_y = pad_A.ycor()
    currentA_y -= 20
    pad_A.sety(currentA_y)


def pad_B_up():  # Need to know the current y-coordinate to move paddle
    currentB_y = pad_B.ycor()
    currentB_y += 20
    pad_B.sety(currentB_y)


def pad_B_down():
    currentB_y = pad_B.ycor()
    currentB_y -= 20
    pad_B.sety(currentB_y)

# Keybord Binding --------------------------------
window.listen()  # Takes keyboard input
window.onkeypress(pad_A_up, "w")
window.onkeypress(pad_A_down, "s")
window.onkeypress(pad_B_up, "Up")
window.onkeypress(pad_B_down, "Down")


# Main game loop ---------------------------------
while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverses the direction of ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # Reverses the direction of ball

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_A += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_B += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_A, score_B), align="center",font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < pad_B.ycor() + 40 and ball.ycor() > pad_B.ycor() - 40):
        ball.setx(340)  # For right-side collision
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < pad_A.ycor() + 40 and ball.ycor() > pad_A.ycor() - 40):
        ball.setx(-340)  # For left-side collision
        ball.dx *= -1
