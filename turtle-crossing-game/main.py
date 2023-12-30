import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
timmy = Player()
manage_car = CarManager()

screen.listen()
screen.onkeypress(fun=timmy.move, key="Up")

game_is_on = True
board = Scoreboard()
cars = []
loops_number = 0
while game_is_on:
    #Generates a new car after every 6th iteration
    if manage_car.detect_collision_with_turtle(timmy):
        game_is_on = False
        board.game_over_display()
    if loops_number % 6 == 0:
        manage_car.create_car()
    time.sleep(0.1)
    manage_car.move_cars()
    # Promotion of turtle to next level and increment of car speeds
    if timmy.is_at_finish_line():
        board.update_level()
        timmy.reset_position()
        manage_car.increase_speed()
    screen.update()
    loops_number += 1
    screen.update()
    loops_number += 1


screen.exitonclick()