from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.right = 0
        self.left = 0
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"{self.left} : {self.right}", False, "center", ('Arial', 24, 'normal'))

    def r_score(self):
        self.right += 1
        self.update()

    def l_score(self):
        self.left += 1
        self.update()
