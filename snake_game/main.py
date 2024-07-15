from turtle import *
import turtle as ninja
import time as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = ninja.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("Snake")
screen.tracer(0)

ts = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(ts.up, "w")#up
screen.onkey(ts.left, "a")#left
screen.onkey(ts.down, "s")#down
screen.onkey(ts.right, "d")#right

game_on = True
while game_on:
    screen.update()
    t.sleep(0.1)
    ts.move()
    
    if ts.head.distance(food) < 15: 
        food.create_food()
        ts.extend()
        scoreboard.increase_score()
    
    if ts.head.xcor() > 290 or ts.head.ycor() > 290 or ts.head.xcor() < -290 or ts.head.ycor() < -290:
        scoreboard.game_over()
        game_on = False
    
    for part in ts.body_parts:
        if part == ts.head:
            pass
        elif ts.head.distance(part) < 10:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()