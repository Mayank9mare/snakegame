from turtle import Screen,Turtle
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard
score=Scoreboard()
snake =Snake()
food=Food()
screen =Screen()

screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


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
    if snake.head.distance(food)<15:
        food.refresh()
        score.increase_scoe()
        snake.extend()
        screen.update()

    print(snake.head.xcor())
    if abs(snake.head.xcor())>=290 or abs(snake.head.ycor())>=290 :
        game=0
        score.gameover()
    for i in snake.segment[1:]:
        if snake.head.distance(i)<10:
            game=0
            score.gameover()
    # if snake.head.xcor()==290 or snake.head.ycor()==290:
    #     game=0


screen.exitonclick();