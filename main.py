from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.penup()
paddle.goto(x=350, y=0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(fun=go_up, key="Up")
screen.onkey(fun=go_down, key="Down")

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()