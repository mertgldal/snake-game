from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Comic Sans', 16, 'normal')
FONT2 = ('Courier', 24, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.highest_score = 0
        self.read_highest_score()
        self.write(f"Score: {self.score}        Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT2)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}        Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # This function set the highest score according to file.
    def read_highest_score(self):
        file = open("highest_score.txt", "r")
        self.highest_score = int(file.read())
        file.close()

    @staticmethod
    def update_highest_score(new_score):
        file = open("highest_score.txt", "w")
        file.write(str(new_score))
        file.close()
