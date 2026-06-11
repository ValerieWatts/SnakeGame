from turtle import Turtle
import snake

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 21, "normal"))

    def increase(self):
        self.score += 1
        self.update()

    def gameover(self):
        self.goto(0,0)
        self.write(arg=f"Game Over", align="center", font=("Courier", 21, "normal"))


    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 21, "normal"))