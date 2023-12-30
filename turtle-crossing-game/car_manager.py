import time
from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.seth(180)
        car.y_value = randint(-230, 230)
        car.goto(310, car.y_value)
        car.car_color = choice(COLORS)
        car.color(car.car_color)
        car.resizemode("user")
        car.shapesize(stretch_len=2, stretch_wid=1)
        self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance = self.move_distance + MOVE_INCREMENT


    def detect_collision_with_turtle(self, player):
        for car in self.all_cars:
            if player.distance(car) <= 20:
                return True