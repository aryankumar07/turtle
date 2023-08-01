from turtle import Turtle,Screen
from my_turtle import Character
from cars import Cars
import random
import time
from score import Score


screen=Screen()
screen.bgcolor("white")
screen.setup(width=800,height=800)
screen.tracer(0)

my_turtle = Character()
score = Score()
car1 = Cars((random.randint(-400,400),random.randint(-250,250)))
car2 = Cars((random.randint(-400,400),random.randint(-250,250)))
car3 = Cars((random.randint(-400,400),random.randint(-250,250)))
car4 = Cars((random.randint(-400,400),random.randint(-250,250)))
car5 = Cars((random.randint(-400,400),random.randint(-250,250)))
car6 = Cars((random.randint(-400,400),random.randint(-250,250)))
car7 = Cars((random.randint(-400,400),random.randint(-250,250)))
car8 = Cars((random.randint(-400,400),random.randint(-250,250)))
car9 = Cars((random.randint(-400,400),random.randint(-250,250)))
car10 = Cars((random.randint(-400,400),random.randint(-250,250)))
car11 = Cars((random.randint(-400,400),random.randint(-250,250)))




screen.listen()
screen.onkey(my_turtle.go_up,'w')
screen.onkey(my_turtle.go_down,'s')
screen.onkey(my_turtle.go_right,'d')
screen.onkey(my_turtle.go_left,'a')

game_is_on=True

while game_is_on:
    # car speed control
    time.sleep(0.2)

    # car movement
    car1.move()
    car2.move()
    car3.move()
    car4.move()
    car5.move()
    car6.move()
    car7.move()
    car8.move()
    car9.move()
    car10.move()
    car11.move()


    # collison
    if my_turtle.distance(car1)<30 or my_turtle.distance(car2)<30 or my_turtle.distance(car3)<30 or my_turtle.distance(car4)<30 or my_turtle.distance(car5)<30 or my_turtle.distance(car6)<30 or my_turtle.distance(car7)<30 or my_turtle.distance(car8)<30 or my_turtle.distance(car9)<30 or my_turtle.distance(car10)<30 or my_turtle.distance(car11)<30 :
        print("collided")
        score.lose()
        game_is_on=False
        

    # win
    if my_turtle.ycor() > 260:
        print("won")
        my_turtle.goto(0,-300)
        score.win()
        game_is_on=False

    # car reset
    if car1.xcor() < -400 :
        car1.reset()
    if car2.xcor() < -400 :
        car2.reset()
    if car3.xcor() < -400 :
        car3.reset()
    if car4.xcor() < -400 :
        car4.reset()
    if car5.xcor() < -400 :
        car5.reset()
    if car6.xcor() < -400 :
        car6.reset()
    if car7.xcor() < -400 :
        car7.reset()
    if car8.xcor() < -400 :
        car8.reset()
    if car9.xcor() < -400 :
        car9.reset()
    if car10.xcor() < -400 :
        car10.reset()
    if car11.xcor() < -400 :
        car11.reset()

    screen.update()


screen.exitonclick()