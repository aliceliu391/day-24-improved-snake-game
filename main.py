from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.go_right, "Right")
screen.onkey(snake.go_left, "Left")

screen.update()


def restart_game():
    scoreboard.reset()
    snake.reset_snake()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.04)
    snake.move()

    if snake.head.distance(food) < 20:
        food.move()
        scoreboard.add_point()
        snake.extend()

    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        restart_game()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            restart_game()

screen.exitonclick()
