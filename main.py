from turtle import Screen,Turtle
import time
from snake import Snake
snake =Snake()
screen =Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")


game=1
while game:
    screen.update()
    time.sleep(.1)
    snake.move()
    screen.listen()
    screen.onkey(snake.up,"Up")

    screen.onkey(snake.down,"Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.update()


screen.exitonclick()