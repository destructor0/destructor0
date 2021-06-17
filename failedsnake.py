import turtle
from random import randint as rn

wn = turtle.Screen()
wn.title("snake")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score = 0
#snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
#snake.shapesize(stretch_len=2, stretch_wid=2)
snake.penup()

#points
points = turtle.Turtle()
points.speed(0)
points.shape("square")
points.color("red")
points.penup()
points.goto(rn(-150, 150), rn(-200, 200))

def snake_up():
    
        y = snake.ycor()
        y += 5
        snake.sety(y)
def snake_down():
    y = snake.ycor()
    y -= 5
    snake.sety(y)
def snake_right():
    x = snake.xcor()
    x += 5
    snake.setx(x)
def snake_left():
    x = snake.xcor()
    x -= 5
    snake.setx(x)

wn.listen()
wn.onkeypress(snake_up, "w")
wn.onkeypress(snake_down, "s")
wn.onkeypress(snake_right, "d")
wn.onkeypress(snake_left, "a")
 


while True:
    wn.update()


    #eat
    if points.pos()==snake.pos():
        snake.shapesize(stretch_len=5)
