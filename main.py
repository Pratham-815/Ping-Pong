from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))

r_paddle = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()
scoreboard.update_score()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y_axis()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_axis()

    # Detect when right paddle misses
    if ball.xcor() > 380 and ball.distance(r_paddle) > 50:
        ball.reset_position()
        time.sleep(1)
        ball.bounce_x_axis()
        scoreboard.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -380 and ball.distance(l_paddle) > 50:
        ball.reset_position()
        time.sleep(1)
        ball.bounce_x_axis()
        scoreboard.r_point()

screen.exitonclick()