from turtle import Screen
from player import Player
from car_manager import Car_Manager
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.tracer(0)
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)

player = Player()
car_manager = Car_Manager()
scoreboard = Scoreboard()

is_gaming_running = True

screen.listen()
screen.onkeypress(key="Up", fun=player.move_forward)
while is_gaming_running:
    sleep(0.1)
    screen.update()
    car_manager.add_cars()
    car_manager.move_cars()


screen.exitonclick()
