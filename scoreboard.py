from food import Food
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
class Scoreboard(Food):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 269)
        self.color("white")
        self.score = 0
        self.increase_score()
    def increase_score(self):
        self.clear()
        self.write(arg=f"Score:{self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game over", align=ALIGNMENT, font=FONT)






