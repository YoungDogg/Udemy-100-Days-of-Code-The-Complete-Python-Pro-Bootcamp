from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.display()

        self.is_right_scored = False

    def plus_one(self):
        if self.is_right_scored:
            self.l_score += 1
        else:
            self.r_score += 1
        self.display()

    def display(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))