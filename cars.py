from turtle import Turtle
import random


class Cars(Turtle):

    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2,stretch_wid=1)
        self.color("black")
        self.goto(position)

    def move(self):
        new_x = self.xcor()-20
        self.goto(new_x,self.ycor())

    def reset(self):
        print("car reset")
        self.goto(430,random.randint(-250,250))
