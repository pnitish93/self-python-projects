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
        self.text = f'Level: {self.level}'
        self.write(arg=self.text, align='center', font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.text = f'Level: {self.level}'
        self.write(arg=self.text, align='center', font=FONT)

    def game_over_display(self):
        self.goto(0,10)
        self.write(arg="GAME OVER", align='center', font=FONT)