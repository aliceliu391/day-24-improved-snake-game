from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.ht()
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}; High Score: {self.highscore}", align="center", font=('Courier', 24, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_high_score()
        self.draw_score()

    def add_point(self):
        self.score += 1
        self.draw_score()

    def get_highscore(self):
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())

    def update_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.highscore))
