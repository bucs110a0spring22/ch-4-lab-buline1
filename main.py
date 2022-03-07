import math
import turtle

#Part A
def drawSineCurve(dart):
  for i in range(-360,361):
    radian_degrees = math.sin(math.radians(i))
    dart.goto(i,radian_degrees)

#Part B
def setupWindow(wn):
  turtle.setworldcoordinates(-375,-1.25,375,1.25)
  wn.bgcolor("blue")
def setupAxis(dart):
  dart.goto(-375,0)
  dart.goto(375,0)
  dart.goto(0,0)
  dart.goto(0,1.25)
  dart.goto(0,-1.25)
  dart.goto(0,0)
  dart.goto(-360,0)


def drawCosineCurve(dart):
  dart.goto(-360,0)
  dart.goto(-360,1)
  for i in range(-360,361):
    radian_degrees2 = math.cos(math.radians(i))
    dart.goto(i,radian_degrees2)

def drawTangentCurve(dart):
  dart.goto(360,0)
  dart.goto(-360,0)
  for i in range(-360,361):
    radian_degrees3 = math.tan(math.radians(i))
    dart.goto(i,radian_degrees3)
    
##########  Do Not Alter Any Code Past Here ########
def main():
  #Part A
  wn = turtle.Screen()
  wn.tracer(5)
  dart = turtle.Turtle()
  dart.speed(0)
  drawSineCurve(dart)

    #Part B
  setupWindow(wn)
  setupAxis(dart)
  dart.speed(0)
  drawSineCurve(dart)
  drawCosineCurve(dart)
  drawTangentCurve(dart)
  wn.exitonclick()
main()
