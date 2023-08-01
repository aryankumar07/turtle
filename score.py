from turtle import Turtle

class Score(Turtle):
    

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")


    def win(self):
        self.goto(0,0)
        self.write("WON",align="center",font=("Arial","18","normal"))

    def lose(self):
        self.goto(0,0)
        self.write("GAME_OVER",align="center",font=("Arial","18","normal"))