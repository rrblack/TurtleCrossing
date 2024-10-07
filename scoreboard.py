from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-280, 250)
        self.write("Level:", font=FONT)
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-280, 250)
        self.write("Level:", font=FONT)
        self.goto(-150, 250)
        self.write(self.level, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font= ("ComicSans", 50, "normal"))