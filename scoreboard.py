from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 14, 'bold')
FONT2 = ('Courier', 24, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT2)

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def win_game(self):
        self.goto(0, 0)
        self.write("YOU WIN", align=ALIGNMENT, font=FONT2)
