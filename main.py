from turtle import Screen
from snake import Snake
from art import logo
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME -                         🐍🐍🐍NOKIA")
user_input = screen.textinput(title="Snake and Turtle", prompt="Type 'START' - start, 'END' - end, 'GETTING READY' - "
                                                               "wait")
screen.tracer(0)
# Tracer() helps to make our snake's segments looks fantastic and smooth without delaying it;s segments with increasing
# its segments.

print(logo)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# for i in range(0, 3):
#     jim = Turtle(shape="square")
#     jim.color("white")
#     m = i * -20
#     jim.goto(x=m, y=0)
#     snake.append(jim)
"""KEY BINDING"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = False
if user_input == "START".lower():
    game_is_on = True
elif user_input == "WAIT".lower():
    time.sleep(5)
    game_is_on = True
elif user_input == "END".lower():
    game_is_on = False
else:
    game_is_on = False
    print("Invalid output from user.")

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # ⚠Detect collision with food.
    snake.move()
    if snake.head.distance(food) < 15:
        if scoreboard.score == 10:
            print(f"⚠Fuck that's Wack😲😲! 10.")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #  ⚠Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # ⚠Detect collision with tail
    # if head collides with any segment in the tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
print(f"Wow! {scoreboard.score} is your final score.")
