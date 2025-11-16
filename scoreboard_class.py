from turtle import Turtle,Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-20,250)
        self.update_screen()
    def update_screen(self):
        self.clear()
        self.write(f"Score:{self.score}   High Score:{self.high_score}",align="center",font=("Courier",20,"normal"))
    def update_highest_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                text=str(self.high_score)
                data.write(f"{text}")
        self.update_screen()
