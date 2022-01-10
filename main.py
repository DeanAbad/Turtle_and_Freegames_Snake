# Modules used: Turtle, Random, and Freegames module

# Note: I added the following features considering that there's more time before deadline:
# 1. The head color (first index from array), lines 59-60;
# 2. An arrow pointing at food (gonna change the background color is the intent,
#    but turns out its an arrow with coordinates, so used it like that instead),
#    lines 65-67;
# 3. A title and a live scoring, line 70;
# 4. A "GAME OVER!" status, line 38;
# 5. Background color and its changes, line 37 (game over) and 78 (still alive)

# Update: Still have to figure out about the overriding/conflicting colors of the
# head from the body (the blue and lime color sometimes wrongly update).

from turtle import *
from random import randrange
from freegames import square, vector

food_pointer = Turtle()
food_pointer.color("White")
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "red")

        # Background color, title, and status when the game is over
        bgcolor("red")
        title("Snake Game | Snake Size: " + str(len(snake)) + " | GAME OVER!")

        update()
        return

    snake.append(head)

    if head == food:
        print('Snake size: ', len(snake))
        food.x = randrange(-15, 15)*10
        food.y = randrange(-15, 15)*10

    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, "blue")

    # If 1st in index, which is head, then color green
    if body[0]:
        square(body.x, body.y, 9, "lime")

    square(food.x, food.y, 9, "red")

    # Food pointer coordinates
    food_pointer.pu()
    food_pointer.goto(food.x - 4.5, food.y + 4.5)
    food_pointer.pd()
    
    # Title and status when game is still running
    title("Snake Game | Snake Size: " + str(len(snake)))
    
    update()
    ontimer(move, 100)

setup(420, 420, 480, 0)

# Background color when the game is still running
bgcolor("black")

hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
