import turtle
import random

screen = turtle.Screen()
sara = turtle.Turtle()
sara.speed(random.randint(0, 4))
sara.shape("turtle")
khris = sara.clone()
khris.speed(random.randint(0, 4))
x = False

screen.title("Turtle Enclosure")
screen.setup(width = 450, height = 450)

while x is False:
  if x is True:
    sara.heading(0, 0)
  sara.lt(random.randint(-45, 45))
  sara.fd(random.randint(0, 10))
  khris.lt(random.randint(-45, 45))
  khris.fd(random.randint(0, 10))
  
