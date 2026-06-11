import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

width= 600
height = 600

screen = Screen()
screen.setup(width,height)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake(screen)
food = Food()
screen.listen()

game = True

while game:

    if snake.snake_blocks[0].xcor() > 290 or snake.snake_blocks[0].xcor() < -290 or snake.snake_blocks[0].ycor() < -290 or snake.snake_blocks[0].ycor() > 290:
        scoreboard.gameover()
        game=False
    else:
        screen.update()
        time.sleep(.1)
        snake.move()

        if snake.snake_blocks[0].distance(food) < 15:
            food.refresh()
            snake.grow()
            scoreboard.increase()

        for pieces in snake.snake_blocks:
            if pieces == snake.snake_blocks[0]:
                pass
            elif snake.snake_blocks[0].distance(pieces) < 10:
                scoreboard.gameover()
                game = False

screen.exitonclick()