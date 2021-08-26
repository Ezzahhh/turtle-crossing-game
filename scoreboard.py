from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.write_score()

    def add_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def reset_score(self):
        self.clear()
        self.score = 1
        self.write_score()

    def write_score(self):
        self.goto(-200, 250)
        self.write(arg=f"Level: {self.score}", align="center", font=FONT)
