import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
player = Player()
screen.onkey(player.up, "Up")

car_manager = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    game_is_on = player.car_detect(car_manager.all_cars)
    if not game_is_on:
        scoreboard.game_over()
    if player.win():
        scoreboard.win_announce()
        time.sleep(1)
        scoreboard.clear()
        car_manager.cars_getting_faster()


screen.exitonclick()