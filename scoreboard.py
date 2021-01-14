from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"score:{self.score}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()
    def gameover(self):
        self.goto(0,0)
        self.write("Game over",align="center",font=("Arial",24,"normal"))

    def increase_scoe(self):
        self.score=self.score+1
        self.clear()
        self.write(f"score:{self.score}", align="center", font=("Arial", 24, "normal"))

