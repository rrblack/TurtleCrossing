import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
turtle = Player()
new_x = 0
car_manager = CarManager()

screen.listen()
screen.onkey(turtle.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_level()
    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    if turtle.crossed_road() == True:
        turtle.reset_position()
        scoreboard.level_up()
        scoreboard.update_level()
        car_manager.car_level_up()

screen.exitonclick()