import turtle
import random

Screen = turtle.screen()
sara = turtle.Turtle()
sara.speed(random.randint(1, 4))
sara.shape("turtle")
khris = sara.clone()
khris.speed(random.randint(1, 4))
x = False

Screen.title("Turtle Enclosure")

while x is False:
  if Screen.height() - sara.xcor() == 0 or Screen.height() - sara.xcor() == Screen.height():
    sara.heading(0, 0)
  sara.lt(random.randint(-45, 45))
  sara.fd(random.randint(0, 10))
  khris.lt(random.randint(-45, 45))
  khris.fd(random.randint(0, 10))
  
