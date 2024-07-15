from turtle import Turtle as tmnt 

class Scoreboard(tmnt):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.update()
    
    def update(self):
        self.write(f"Score = {self.score}", align="center", font=("New York Times", 14, "normal"))
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("New York Times", 14, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()