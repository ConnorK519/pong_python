from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

playing = True
speed = 0.1

while playing:
    time.sleep(speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        if speed > 0.05:
            speed -= 0.01

    if ball.xcor() > 400:
        ball.reset()
        scoreboard.l_score()
        speed = 0.1

    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_score()
        speed = 0.1


screen.exitonclick()

