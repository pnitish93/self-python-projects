import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
timmy = Player()
sleep_time = 0.1

screen.listen()
screen.onkeypress(fun=timmy.move, key="Up")

game_is_on = True
board = Scoreboard()
cars = []
loops_number = 0
while game_is_on:
    #Generates a new car after every 6th iteration
    if loops_number % 6 == 0:
        for i in range(1):
            cars.append(CarManager())
    time.sleep(sleep_time)
    for car in cars:
        # collision
        if timmy.distance(car) <= 31:
            game_is_on = False
            board.game_over_display()
        car.move_car()
    # Promotion of turtle to next level and increment of car speeds
    if timmy.ycor() >= 280:
        board.update_level()
        timmy.reset_position()
        sleep_time *= 0.5

    screen.update()
    loops_number += 1


screen.exitonclick()