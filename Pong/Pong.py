from turtle import Screen
from pad import Paddle
from balls import Balls
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
#screen.tracer(0)

score = Score()
pad_1 = Paddle((-350, 0))
pad_2 = Paddle((350, 0))
ball = Balls()

game_is_on = True

screen.listen()
screen.onkeypress(pad_1.go_up, "w")
screen.onkeypress(pad_1.go_down, "s")
screen.onkeypress(pad_2.go_up, "Up")
screen.onkeypress(pad_2.go_down, "Down")

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #Wall collision detection
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit_wall()
    #Paddle collision detection
    if ball.distance(pad_2) < 50 and ball.xcor() > 320 or ball.distance(pad_1) < 50 and ball.xcor() < -320:
        ball.hit_paddle()
    #Score detection
    if ball.xcor() > 380:
        score.l_point()
        pad_1.restart_pad()
        pad_2.restart_pad()
        ball.reset_position()
    elif ball.xcor() < -380:
        score.r_point()
        pad_1.restart_pad()
        pad_2.restart_pad()
        ball.reset_position()

    if score.l_score == 10 or score.r_score == 10:
        score.game_over()
        game_is_on = False

screen.exitonclick()
