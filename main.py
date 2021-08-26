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
    sleep(car_manager.car_speed)
    screen.update()
    for car in car_manager.car_list:
        if player.distance(car) < 20:
            # collision and then reset level, score and clear screen
            car_manager.reset_level()
            scoreboard.reset_score()
            player.reset_to_home()
    if player.ycor() > 200:
        # Player has passed to next level
        player.reset_to_home()
        car_manager.reset_level()
        scoreboard.add_score()
        car_manager.faster_speed()
    car_manager.add_cars()
    car_manager.move_cars()


screen.exitonclick()
