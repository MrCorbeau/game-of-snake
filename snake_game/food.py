from turtle import Turtle as tmnt
import random

class Food(tmnt):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.create_food()
        
    def create_food(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 265)
        self.goto(rand_x, rand_y)