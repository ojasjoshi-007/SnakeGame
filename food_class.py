from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(0.5,0.5)
        self.color("white")
        self.x_cor=0
        self.y_cor=0
        self.refresh()

    def refresh(self):
        self.x_cor = random.randint(-250, 250)
        self.y_cor = random.randint(-250, 250)
        self.goto(self.x_cor, self.y_cor)


