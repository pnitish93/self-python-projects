import time
from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.y_value = randint(-230, 230)
        self.x_value = randint(310, 9010)
        self.goto(self.x_value, self.y_value)
        self.car_color = choice(COLORS)
        self.color(self.car_color)
        self.resizemode("user")
        self.shapesize(stretch_len=2, stretch_wid=1)

    def move_car(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())