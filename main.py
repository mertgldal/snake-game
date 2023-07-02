from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# import numpy as np
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

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
        score.update_score_board()
        snake.extend()
        sleep_time -= 0.001

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        score.game_over()

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()
    # Shorter version of above code. But there are some error.
    # arr = np.array(snake.segments)
    # for segment in arr[1:]:
        # if snake.head.distance(segment) < 10:
        #     is_game_on = False
        #     score.game_over()

    if score.score == 23:
        is_game_on = False
        score.update_score_board()
        score.win_game()

screen.exitonclick()
