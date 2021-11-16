import turtle
import random

screen = turtle.Screen()
screen.title('Turtle livestream')
screen.mode("logo")


first = turtle.Turtle()
box = first.clone()
first.speed(random.randint(1, 3))
first.penup()
first.color('green')
first.shape("turtle")
second = first.clone()
x = False
b = 0
fangle = first.towards(0, 0)
sangle = second.towards(0, 0)

box.penup()
box.ht()
box.goto(-220, -220)
box.pendown()
while b != 4:
    box.fd(440)
    box.rt(90)
    b += 1

# navigation is pick random
# can you use turtle.Turtle() to control all of the turtles?
# increase and decrease the number of turtles
# make senary?, write on the screen?,
# senary - most is pond, add log, add rock/s
# make player involved -> choose attributes -> 

first.lt(random.randint(0, 359))
second.lt(random.randint(0, 359))

while x is False:
    # must find how to turn turtles around
    if first.xcor() >= 200 or first.xcor() <= -200:
        fangle == first.towards(0, 0)
        first.lt(fangle)
        first.fd(10)
    if first.ycor() >= 200 or first.ycor() <= -200:
        fangle == first.towards(0, 0)
        first.lt(fangle)
        first.fd(10)
    if second.xcor() >= 200 or second.xcor() <= -200:
        sangle == second.towards(0, 0)
        second.lt(sangle)
        second.fd(10)
    if second.ycor() >= 200 or second.ycor() <= -200:
        sangle == second.towards(0, 0)
        second.lt(sangle)
        second.fd(10)
    first.fd(random.randint(0, 6))
    first.lt(random.randint(-40, 40))
    first.speed(random.randint(1, 2))
    second.fd(random.randint(0, 8))
    second.lt(random.randint(-30, 30))
    second.speed(random.randint(1, 4))
