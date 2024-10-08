from turtle import Turtle
import time
INCREASE = 1.01

class Balls(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.speed("fastest")
        self.goto(0, 0)
        self.speed("normal")
        self.move_speed = 0.1
        self.bounce_x()
        time.sleep(0.8)

    def hit_paddle(self):
        self.bounce_x()
        self.move_speed *= 0.80

    def hit_wall(self):
        self.bounce_y()
        self.move_speed *= 0.85
