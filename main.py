import time
from turtle import Turtle,Screen
from snake_class import Snake
from food_class import Food
from scoreboard_class import Scoreboard
screen=Screen()
screen.colormode(1.0)
screen.bgcolor((0.3,0.5,0.3))
screen.tracer(0)
screen.title("Snake Game")
screen.setup(600,600)
snake=Snake()
food=Food()
scoreboard=Scoreboard()
game_is_on=True
snake.create_snake()
screen.listen()
screen.onkey(fun=snake.go_up,key="Up")
screen.onkey(fun=snake.go_down,key="Down")
screen.onkey(fun=snake.go_right,key="Right")
screen.onkey(fun=snake.go_left,key="Left")
sleep=0.15
while game_is_on:
    screen.update()
    time.sleep(sleep)
    snake.move_forward()
    if snake.head.distance(food)<20:
        food.refresh()
        snake.add_snake()
        scoreboard.score += 1
        scoreboard.update_highest_score()
        scoreboard.update_screen()
        sleep=sleep/1.1

    if  snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.update_highest_score()
        game_is_on=False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<5:
            scoreboard.update_highest_score()
            game_is_on=False