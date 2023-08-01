from turtle import Turtle

class Character(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0,-300)  
        self.left(90)


    # movements

    def go_up(self):
        new_y=self.ycor()+10
        self.goto(self.xcor(),new_y)
    
    def go_down(self):
        new_y=self.ycor()-10
        self.goto(self.xcor(),new_y)

    def go_right(self):
        new_x=self.xcor()+10
        self.goto(new_x,self.ycor())

    def go_left(self):
        new_x=self.xcor()-10
        self.goto(new_x,self.ycor())