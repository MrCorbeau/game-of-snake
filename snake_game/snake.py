from turtle import *
import turtle as tmnt

starting_positions = [(0,0), (-20,0), (-40,0)]

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

screen = tmnt.Screen()

class Snake:
    
    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]
    
    def create_snake(self):
        for position in starting_positions:
            self.add_part(position)
    
    def add_part(self, position):
        snake_part = Turtle(shape="circle")
        snake_part.penup()
        snake_part.goto(position)
        self.body_parts.append(snake_part)
        screen.update()
    
    def extend(self):
        self.add_part(self.body_parts[-1].position())
    
    def move(self):
        for body_num in range(len(self.body_parts) - 1, 0, -1):
            newX = self.body_parts[body_num - 1].xcor()
            newY = self.body_parts[body_num - 1].ycor()
            self.body_parts[body_num].goto(x=newX, y=newY)
        self.body_parts[0].forward(20)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.body_parts[0].setheading(LEFT)
    
    def down(self):
        if self.head.heading() != UP:
            self.body_parts[0].setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.body_parts[0].setheading(RIGHT)