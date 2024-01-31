from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.current_x = 10
        self.current_y = 10

    def move(self):
        new_x = self.xcor() + self.current_x
        new_y = self.ycor() + self.current_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.current_y *= -1

    def bounce_x(self):
        self.current_x *= -1

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()



