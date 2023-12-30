from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.goto(-200, 250)
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Level: {self.level}', align='center', font=FONT)

    def update_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over_display(self):
        self.goto(0,10)
        self.write(arg="GAME OVER", align='center', font=FONT)