import turtle

# screen
screen = turtle.Screen()
screen.title("Ping Pong")
screen.bgcolor(0.21,0.3,0.26)
screen.setup(width=800, height=600)
screen.tracer(0)
middle_line = turtle.Turtle()
middle_line.shape("square")
middle_line.color("white")
middle_line.shapesize(stretch_wid=100, stretch_len=0.25, outline=None)
middle_line.goto(0,300)

# scores
score_a = 0
score_b = 0

# rackets
racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape("square")
racket_a.color("white")
racket_a.shapesize(stretch_wid=6, stretch_len=1, outline=None)
racket_a.penup()
racket_a.goto(-350, 0)
racket_b = turtle.Turtle()
racket_b.speed(0)
racket_b.shape("square")
racket_b.color("white")
racket_b.shapesize(stretch_wid=6, stretch_len=1, outline=None)
racket_b.penup()
racket_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# statistics
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-350,250)
pen.write("Player A: {}".format(score_a), align="left", font=("Helvetica", 20, "normal"))
pen.goto(350,250)
pen.write("Player B: {}".format(score_b), align="right", font=("Helvetica", 20, "normal"))

# functions
def racket_a_up():
    y = racket_a.ycor()
    y += 20
    racket_a.sety(y)

def racket_a_down():
    y = racket_a.ycor()
    y -= 20
    racket_a.sety(y)

def racket_b_up():
    y = racket_b.ycor()
    y += 20
    racket_b.sety(y)

def racket_b_down():
    y = racket_b.ycor()
    y -= 20
    racket_b.sety(y)

# bindings
screen.listen()
screen.onkeypress(racket_a_up, "w")
screen.onkeypress(racket_a_down, "s")
screen.onkeypress(racket_b_up, "Up")
screen.onkeypress(racket_b_down, "Down")

# Main game
while True:
    screen.update()

    # Move  ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.goto(-350,250)
        pen.write("Player A: {}".format(score_a), align="left", font=("Helvetica", 20, "normal"))
        pen.goto(350,250)
        pen.write("Player B: {}".format(score_b), align="right", font=("Helvetica", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.goto(-350,250)
        pen.write("Player A: {}".format(score_a), align="left", font=("Helvetica", 20, "normal"))
        pen.goto(350,250)
        pen.write("Player B: {}".format(score_b), align="right", font=("Helvetica", 20, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() < racket_a.ycor() + 50 and ball.ycor() > racket_a.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 340 and ball.ycor() < racket_b.ycor() + 50 and ball.ycor() > racket_b.ycor() - 50:
        ball.dx *= -1
