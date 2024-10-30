from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(-50, 270)
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.goto(-50, 0)
        self.write("GAME OVER", font=FONT)

    def increase_score(self):
        self.score += 1
