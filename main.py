from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

file = open("highest_score.txt", "r")
highest_score = int(file.read())
file.close()


screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


sleep_time = 0.1
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(sleep_time)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 14:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        # This sets the new game speed.
        sleep_time /= 1.02

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

    # We have only 23 colors in our game that's why we reset the colors every 23 scores
    if scoreboard.score % 23 == 0 and scoreboard.score != 0:
        snake.reset_colors()

# This if checks the highest score at end of the game and update it if the condition is true.
if highest_score < scoreboard.score:
    highest_score = scoreboard.score
    scoreboard.update_highest_score(new_score=highest_score)

screen.exitonclick()
