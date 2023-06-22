from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        shape = random.choice(["square", "circle", "triangle"])
        color = random.choice(["blue", "silver", "orange"])
        self.hideturtle()
        self.shape(shape)
        self.color(color)
        self.goto(random.randint(-300, 300), random.randint(-300, 300) )
        self.showturtle()