from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car_Manager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.car_list = []

    def add_cars(self):
        if randint(0, 100) < 25:
            self.car_list.append(Car())

    def move_cars(self) -> None:
        for car in self.car_list:
            if car.xcor() < -300:
                car.clear()
                car.ht()
                self.car_list.remove(car)
            else:
                car.forward(MOVE_INCREMENT)


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.setheading(180)
        self.setpos(300, randint(-250, 250))
