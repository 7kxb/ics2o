# Coding and Documentation by Kevin Xiang
# ICS201, Mr. Anandarajan 
# "Completion" on April 25, 2022
# -:importing:------------------ #
import turtle                   # imports turtle
import time                     # imports time
import os                       # imports os
import random                   # imports random
import math                     # imports math 
#import playsound               # imports playsound
os.system('cls')                # clears the console (only on windows and not unix-based systems)
turtle.setup(800, 800, 0, 0)    # setups the window size
window = turtle.Screen()        # defines variable window as the turtle's scren     
window.tracer(0)                # ensures drawings aren't show until update is called
window.bgcolor('black')         # sets the background color of the window to black
window.title('MAZE')            # sets the title of the window to MAZE
#playsound("audio.mp3")         # plays background music
# -:turtles:-------------------- #
main = turtle.Turtle()          # creates seperate turtle instance named main
introtext = turtle.Turtle()     # creates seperate turtle instance named introtext
player = turtle.Turtle()        # creates seperate turtle instance named player
level = turtle.Turtle()         # creates seperate turtle instance named level
raycaster = turtle.Turtle()     # creates seperate turtle instance named raycaster
color = turtle.Turtle()         # creates seperate turtle instance named color
pen = turtle.Turtle()           # creates seperate turtle instance named pen
goal = turtle.Turtle()          # creates seperate turtle instance named goal
playbutton = turtle.Turtle()    # creates seperate turtle instance named playbutton
cursor = turtle.Turtle()        # creates seperate turtle instance named cursor
# -:hiding:--------------------- #
player.ht()                     # hides the player turtle
level.ht()                      # hides the level turtle
raycaster.ht()                  # hides the raycaster turtle
color.ht()                      # hides the color turtle
pen.ht()                        # hides the pen turtle
goal.ht()                       # hides the goal turtle
playbutton.ht()                 # hides the playbutton turtle
cursor.ht()                     # hides the cursor turtle
# -:variables:------------------ #
CURSOR_SIZE = 20
walls = []
res = 4
ph = 90
x = res/2*240
fov = 103
dv = 240/(math.tan(fov/2))
drawIDX = 2
if res < 4:
  x = abs(x)
scanlines = 480/res
rh = ph-(240/(math.tan(fov/2)))
# -:functions:------------------ #
def Initialize():               # setting up turtles
  player.st()
  player.pu()
  player.shapesize(0.5)
  player.goto(290,230)
  player.seth(90)
  player.shape('turtle')
  player.color('dark green', 'green')
  player.penup()
                                                                            		
  level.speed(-1)
  level.pencolor('cyan')
  level.width(2)
  level.shape('square')
  level.ht()
  level.pd()
  level.shapesize(stretch_wid=1/CURSOR_SIZE)

  raycaster.ht()
  raycaster.pu()
  raycaster.shape('square')
  raycaster.shapesize(0.1)
                       		
  color.speed(-1)
  color.pencolor('blue')
  color.width(2)
  color.shape("square")
  color.ht()
  color.pd()
  color.shapesize(stretch_wid=1/CURSOR_SIZE)

  pen.ht()

  goal.shape('square')
  goal.shapesize(2.5/4)
  goal.color('red', 'black')
  goal.penup()
  goal.goto(290,370)
  goal.st()

def makeWall(turtle, distance): # making and defining the walls
  turtle.forward(distance / 2)
  clone = turtle.clone()
  clone.shapesize(stretch_len=distance/CURSOR_SIZE)
  clone.ht()
  turtle.forward(distance / 2)
  walls.append(clone)

def drawMaze():                 # drawing the maze
  level.pu()
  level.goto(300,300)
  level.left(180)
  level.forward(80)
  level.left(90)
  level.forward(80)
  level.left(90)
  level.pd()
  makeWall(level, 160)
  level.left(90)
  makeWall(level, 160)
  level.left(90)
  makeWall(level, 160)
  level.left(90)
  makeWall(level, 160)
  level.left(90)
  makeWall(level, 60)
  level.left(90)
  makeWall(level, 40)
  level.left(180)
  makeWall(level, 40)
  level.left(90)
  makeWall(level, 20)
  level.left(90)
  makeWall(level, 20)
  level.left(180)
  makeWall(level, 20)
  level.left(90)
  makeWall(level, 40)
  level.left(90)
  makeWall(level, 20)
  level.right(90)
  makeWall(level, 20)
  level.left(90)
  level.pu()
  level.forward(20)
  level.right(90)
  level.forward(20)
  level.right(180)
  level.pd()
  makeWall(level, 80)
  level.right(90)
  makeWall(level, 40)
  level.left(90)
  level.pu()
  level.forward(40)
  level.left(180)
  level.pd()
  makeWall(level, 20)
  level.right(90)
  makeWall(level, 20)
  level.left(90)
  makeWall(level, 20)
  level.pu()
  level.forward(60)
  level.left(90)
  level.pd()
  makeWall(level, 60)
  level.pu()
  level.forward(20)
  level.pd()
  makeWall(level, 20)
  level.left(90)
  makeWall(level, 20)
  level.left(90)
  level.pu()
  level.forward(20)
  level.pd()
  makeWall(level, 20)
  level.pu()
  level.forward(20)
  level.pd()
  makeWall(level, 60)
  level.right(90)
  makeWall(level, 20)
  level.left(90)
  makeWall(level, 20)
  level.right(90)
  level.pu()
  level.forward(60)
  level.pd()
  makeWall(level, 20)
  level.right(90)
  makeWall(level, 60)
  level.left(90)
  makeWall(level, 20)
  level.left(90)
  makeWall(level, 60)
  level.left(90)
  level.pu()
  level.forward(40)
  level.left(90)
  level.pd()
  makeWall(level, 20)
  level.pu()
  level.forward(20)
  level.pd()
  level.left(90)
  makeWall(level, 20)
  level.left(180)
  makeWall(level, 20)
  level.left(90)
  level.pu()
  level.forward(40)
  level.pd()
  makeWall(level, 40)
  level.left(90)
  makeWall(level, 40)
  level.right(180)
  level.pu()
  level.forward(60)
  level.pd()
  level.left(90)
  makeWall(level, 20)
  level.left(180)
  makeWall(level, 20)
  level.left(90)
  makeWall(level, 60)
  level.right(90)
  makeWall(level, 20)
  level.left(90)
  makeWall(level, 20)
  level.left(180)
  makeWall(level, 60)
  level.left(90)
  makeWall(level, 20)
  level.right(90)
  makeWall(level, 20)
  level.pu()
  level.forward(20)
  level.pd()
  makeWall(level, 20)
  level.right(90)
  makeWall(level, 20)
  level.right(90)
  level.pu()
  level.forward(20)
  level.pd()
  makeWall(level, 20)
  level.pu()
  level.forward(40)
  level.right(90)
  level.forward(40)
  level.pd()
  level.left(90)
  makeWall(level, 20)
  level.left(180)
  makeWall(level, 20)
  level.left(90)
  makeWall(level, 40)
  # switch #
  color.pu()
  color.goto(300,300)
  color.forward(2)
  color.left(180)
  color.forward(80)
  color.left(90)
  color.forward(80)
  color.left(90)
  color.pd()
  makeWall(color, 160)
  color.left(90)
  makeWall(color, 160)
  color.left(90)
  makeWall(color, 160)
  color.left(90)
  makeWall(color, 160)
  color.left(90)
  makeWall(color, 60)
  color.left(90)
  makeWall(color, 40)
  color.left(180)
  makeWall(color, 40)
  color.left(90)
  makeWall(color, 20)
  color.left(90)
  makeWall(color, 20)
  color.left(180)
  makeWall(color, 20)
  color.left(90)
  makeWall(color, 40)
  color.left(90)
  makeWall(color, 20)
  color.right(90)
  makeWall(color, 20)
  color.left(90)
  color.pu()
  color.forward(20)
  color.right(90)
  color.forward(20)
  color.right(180)
  color.pd()
  makeWall(color, 80)
  color.right(90)
  makeWall(color, 40)
  color.left(90)
  color.pu()
  color.forward(40)
  color.left(180)
  color.pd()
  makeWall(color, 20)
  color.right(90)
  makeWall(color, 20)
  color.left(90)
  makeWall(color, 20)
  color.pu()
  color.forward(60)
  color.left(90)
  color.pd()
  makeWall(color, 60)
  color.pu()
  color.forward(20)
  color.pd()
  makeWall(color, 20)
  color.left(90)
  makeWall(color, 20)
  color.left(90)
  color.pu()
  color.forward(20)
  color.pd()
  makeWall(color, 20)
  color.pu()
  color.forward(20)
  color.pd()
  makeWall(color, 60)
  color.right(90)
  makeWall(color, 20)
  color.left(90)
  makeWall(color, 20)
  color.right(90)
  color.pu()
  color.forward(60)
  color.pd()
  makeWall(color, 20)
  color.right(90)
  makeWall(color, 60)
  color.left(90)
  makeWall(color, 20)
  color.left(90)
  makeWall(color, 60)
  color.left(90)
  color.pu()
  color.forward(40)
  color.left(90)
  color.pd()
  makeWall(color, 20)
  color.pu()
  color.forward(20)
  color.pd()
  color.left(90)
  makeWall(color, 20)
  color.left(180)
  makeWall(color, 20)
  color.left(90)
  color.pu()
  color.forward(40)
  color.pd()
  makeWall(color, 40)
  color.left(90)
  makeWall(color, 40)
  color.right(180)
  color.pu()
  color.forward(60)
  color.pd()
  color.left(90)
  makeWall(color, 20)
  color.left(180)
  makeWall(color, 20)
  color.left(90)
  makeWall(color, 60)
  color.right(90)
  makeWall(color, 20)
  color.left(90)
  makeWall(color, 20)
  color.left(180)
  makeWall(color, 60)
  color.left(90)
  makeWall(color, 20)
  color.right(90)
  makeWall(color, 20)
  color.pu()
  color.forward(20)
  color.pd()
  makeWall(color, 20)
  color.right(90)
  makeWall(color, 20)
  color.right(90)
  color.pu()
  color.forward(20)
  color.pd()
  makeWall(color, 20)
  color.pu()
  color.forward(40)
  color.right(90)
  color.forward(40)
  color.pd()
  color.left(90)
  makeWall(color, 20)
  color.left(180)
  makeWall(color, 20)
  color.left(90)
  makeWall(color, 40)

def collision(turtle):          # detecting collision
    tx, ty = turtle.position()

    for wall in walls:

        if wall.distance(turtle) < CURSOR_SIZE / 4:
            wall.color('red')
            player.pencolor('red')
            window.update()
            return True

        wx, wy = wall.position()
        heading = wall.heading()
        _, stretch_len, _ = wall.shapesize()
        half_length = stretch_len * (CURSOR_SIZE + 1) / 4

        if heading in [0, 180]:  # horizontal wall

            if abs(ty - wy) < CURSOR_SIZE / 4 and abs(tx - wx) < half_length:
                wall.color('red')
                player.pencolor('red')
                window.update()
                return True

        elif heading in [90, 270]:  # vertical wall

            if abs(tx - wx) < CURSOR_SIZE / 4 and abs(ty - wy) < half_length:
                wall.color('red')
                player.pencolor('red')
                window.update()
                return True

    window.update()
    return False

'''                             # enrichment i didn't get to complete
def rayCast():
  for _ in range(int(scanlines)):
    raycaster.seth(ph+(math.atan(x/dv))) 
    singleRay()
    x += res
    rh -= res

def singleRay():
  raycaster.goto(player.xcor,player.ycor)
  while collision(raycaster) == False:
    raycaster.forward(2)
  while collision(raycaster) == True:
    raycaster.backward(1)
  dist = raycaster.distance(player)
  dist = dist*(math.cos(rh-ph))

def threeDimension():
  # code this part asap
'''

def drawBorder():               # draws the border
    main.pu()
    main.goto(-320-4,240+4)
    main.fillcolor('black')
    main.begin_fill()
    main.goto(-320-4,-240-4)
    main.goto(-400-4,-240-4)
    main.goto(-400-4,240+4)
    main.goto(-320-4,240+4)
    main.end_fill()
    main.goto(320+4,240+4)
    main.width(8)
    main.pencolor('#ffffff')
    main.pd()
    main.goto(320+4,-240-4)
    main.goto(-320-4,-240-4)
    main.goto(-320-4,240+4)
    main.goto(320+4,240+4)
    
def stripeBG():                 # draws the background
    main.pu()
    main.goto(-320,240)
    main.fillcolor('#040404') # 1
    main.begin_fill()
    main.goto(-320,240) # origin 1
    main.goto(-320,240) # origin 2
    main.goto(-320,160) # go
    main.goto(-260,240) # draw
    main.end_fill()
    main.fillcolor('#080808') # 2
    main.begin_fill()
    main.goto(-260,240) # origin 1
    main.goto(-320,160) # origin 2
    main.goto(-320,80) # go
    main.goto(-200,240) # draw
    main.end_fill()
    main.fillcolor('#0c0c0c') # 3
    main.begin_fill()
    main.goto(-200,240) # origin 1
    main.goto(-320,80) # origin 2
    main.goto(-320,0) # go 
    main.goto(-140,240) # draw
    main.end_fill()
    main.fillcolor('#101010') # 4
    main.begin_fill()
    main.goto(-140,240) # origin 1
    main.goto(-320,0) # origin 2
    main.goto(-320,-80) # go
    main.goto(-80,240) # draw
    main.end_fill()
    main.fillcolor('#141414') # 5
    main.begin_fill()
    main.goto(-80,240) # origin 1
    main.goto(-320,-80) # origin 2
    main.goto(-320,-160) # go
    main.goto(-20,240) # draw
    main.end_fill()
    main.fillcolor('#181818') # 6
    main.begin_fill()
    main.goto(-20,240) # origin 1
    main.goto(-320,-160) # origin 2
    main.goto(-320,-240) # go
    main.goto(40,240) # draw
    main.end_fill()
    #
    main.goto(-40,-240)
    main.fillcolor('#181818') # 1
    main.begin_fill()
    main.goto(-40,-240) # go
    main.goto(320,240) # draw
    main.goto(320,160) # origin 1
    main.goto(20,-240) # origin 2
    main.end_fill()
    main.fillcolor('#141414') # 2
    main.begin_fill()
    main.goto(20,-240) # go
    main.goto(320,160) # draw
    main.goto(320,80) # origin 1
    main.goto(80,-240) # origin 2
    main.end_fill()
    main.fillcolor('#101010') # 3
    main.begin_fill()
    main.goto(80,-240) # go
    main.goto(320,80) # draw
    main.goto(320,0) # origin 1
    main.goto(140,-240) # origin 2
    main.end_fill()
    main.fillcolor('#0c0c0c') # 4
    main.begin_fill()
    main.goto(140,-240) # go
    main.goto(320,0) # draw
    main.goto(320,-80) # origin 1
    main.goto(200,-240) # origin 2
    main.end_fill()
    main.fillcolor('#080808') # 5
    main.begin_fill()
    main.goto(200,-240) # go
    main.goto(320,-80) # draw
    main.goto(320,-160) # origin 1
    main.goto(260,-240) # origin 2
    main.end_fill()
    main.fillcolor('#040404') # 6
    main.begin_fill()
    main.goto(260,-240) # go
    main.goto(320,-160) # draw
    main.goto(320,-240) # origin 1
    main.goto(320,-240) # origin 2
    main.end_fill()
    #
    main.fillcolor('#1c1c1c') # X
    main.begin_fill()
    main.goto(-320,-240) # go
    main.goto(40,240) # draw
    main.goto(320,240) # origin 1
    main.goto(-40,-240) # origin 2
    main.end_fill()

def aRock():                    # draws the rock on the bottom right
    main.pu()
    main.goto(-160,-240)
    main.pd()
    main.fillcolor('#000000') 
    main.begin_fill()
    main.seth(30)
    main.forward(50)
    main.right(20)
    main.forward(40)
    main.left(30)
    main.forward(50)
    main.right(20)
    main.forward(40)
    main.left(30)
    main.forward(50)
    main.right(30)
    main.forward(40)
    main.left(20)
    main.forward(50)
    main.right(20)
    main.forward(40)
    main.right(30)
    main.forward(20)
    main.left(40)
    main.forward(40)
    main.left(10)
    main.forward(20)
    main.left(10)
    main.forward(40)
    main.right(30)
    main.forward(20)
    main.left(20)
    main.forward(20)
    main.left(30)
    main.forward(40)
    main.right(40)
    main.forward(20)
    main.left(50)
    main.forward(20)
    main.right(40)
    main.forward(20)
    main.goto(320,-240)
    main.goto(-160,-240)
    main.end_fill()

def theBridge():                # draws the bridge
    main.pu()
    main.goto(-280,-240)
    main.seth(95)
    main.width(8)
    main.pencolor('#ffffff')
    main.fillcolor('#000000')
    main.begin_fill()
    main.pd()
    main.forward(200)
    main.left(75)
    main.forward(40)
    main.left(105)
    main.forward(200)
    main.left(90)
    main.forward(40)
    main.end_fill()
    main.left(90)
    main.forward(200)
    main.left(75)
    main.forward(40)
    main.right(180)
    main.fillcolor('#000000')
    main.begin_fill()
    main.forward(560)
    main.left(90)
    main.forward(80)
    main.left(90)
    main.forward(560)
    main.left(90)
    main.forward(80)
    main.end_fill()
    #
    main.pu()
    main.goto(230,-15)
    main.seth(160)
    main.pd()
    main.forward(80)
    main.seth(270)
    main.forward(40)
    main.seth(90)
    main.forward(40)
    main.seth(180)
    main.right(3)
    main.forward(74)
    main.seth(270)
    main.forward(30)
    main.seth(90)
    main.forward(30)
    main.seth(180)
    main.right(6)
    main.forward(68)
    main.seth(270)
    main.forward(25)
    main.seth(90)
    main.forward(25)
    main.seth(180)
    main.right(9)
    main.forward(62)
    main.seth(270)
    main.forward(25)
    main.seth(90)
    main.forward(25)
    main.seth(180)
    main.right(12)
    main.forward(56)
    main.seth(270)
    main.forward(25)
    main.seth(90)
    main.forward(25)
    main.seth(180)
    main.right(15)
    main.forward(50)
    main.seth(270)
    main.forward(30)
    main.seth(90)
    main.forward(30)
    main.seth(180)
    main.right(18)
    main.forward(50)
    main.seth(270)
    main.forward(40)
    main.seth(90)
    main.forward(40)
    main.seth(180)
    main.right(21)
    main.forward(50)
    main.seth(270)
    main.forward(50)
    main.seth(90)
    main.forward(50)
    main.seth(180)
    main.right(24)
    main.forward(50)
    main.seth(270)
    main.forward(60)
    main.seth(90)
    main.forward(60)
    main.seth(180)
    main.right(27)
    main.forward(50)
    #
    main.pu()
    main.goto(165,-70)
    main.seth(160)
    main.pd()
    main.forward(80)
    main.seth(270)
    main.forward(50)
    main.seth(90)
    main.forward(50)
    main.seth(180)
    main.right(3)
    main.forward(74)
    main.seth(270)
    main.forward(40)
    main.seth(90)
    main.forward(40)
    main.seth(180)
    main.right(6)
    main.forward(68)
    main.seth(270)
    main.forward(40)
    main.seth(90)
    main.forward(40)
    main.seth(180)
    main.right(9)
    main.forward(62)
    main.seth(270)
    main.forward(40)
    main.seth(90)
    main.forward(40)
    main.seth(180)
    main.right(12)
    main.forward(56)
    main.seth(270)
    main.forward(40)
    main.seth(90)
    main.forward(40)
    main.seth(180)
    main.right(15)
    main.forward(50)
    main.seth(270)
    main.forward(40)
    main.seth(90)
    main.forward(40)
    main.seth(180)
    main.right(18)
    main.forward(50)
    main.seth(270)
    main.forward(50)
    main.seth(90)
    main.forward(50)
    main.seth(180)
    main.right(21)
    main.forward(50)
    main.seth(270)
    main.forward(60)
    main.seth(90)
    main.forward(60)
    main.seth(180)
    main.right(24)
    main.forward(50)

def moonRiver():                # draws the moon and the river
    main.pu()
    main.goto(-320,0)
    main.fillcolor('#141414')
    main.begin_fill()
    main.goto(320,-80)
    main.goto(320,-240)
    main.goto(-320,-240)
    main.goto(-320,0)
    main.end_fill()
    main.goto(80,40)
    main.fillcolor('#808080')
    main.begin_fill()
    main.circle(70)
    main.end_fill()
    main.goto(70,40)
    main.fillcolor('#141414')
    main.begin_fill()
    main.circle(60)
    main.end_fill()

def sixtySeven():               # ignore, was supposed to be extra
    main.pu()
    main.goto(140,-140)
    main.seth(0)
    main.fillcolor('#ffffff')
    main.begin_fill()
    for __ in range(6):
        main.right(60)
        main.forward(60)
    main.end_fill()
    main.fillcolor('#000000')
    main.begin_fill()
    main.right(60)
    main.forward(60)
    main.right(120)
    main.forward(60)
    main.right(120)
    main.forward(60)
    main.end_fill()
    
def ninetyThree():              # ignore, was supposed to be extra
    main.pu()
    main.goto(280,-220)
    main.pd()
    main.circle(40)
    main.pu()
    main.seth(90)
    main.forward(30)
    main.left(90)
    main.forward(20)
    main.right(180)
    main.pd()
    main.pencolor('#ff0000')
    main.forward(50)
    main.left(90)
    main.forward(30)
    main.left(120)
    main.forward(58.31)
    main.right(30)
    main.pu()
    main.forward(30)
    main.pd()
    main.pencolor('#0000ff')
    main.forward(50)
    main.right(135)
    main.forward(35)
    main.right(90)
    main.forward(35)

def bb(x,y):                    # creates loading screen function
    # Creating Ball #
    ball = turtle.Turtle()
    ball.ht()
    ball.speed(0)
    colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
    hit = 0
    ball.fillcolor('grey')
    ball.pu()
    ball.goto(0,0)
    ball.dx = random.randint(10,20)/100   # dx = x change
    ball.dy = random.randint(10,20)/100   # dy = y change

    while hit < 10:
        # Moving Ball
        ball.setx(ball.xcor() + ball.dx)    # xcor = x coordinate
        ball.sety(ball.ycor() + ball.dy)    # ycor = y coordinate
        ball.begin_fill()
        for _ in range(2):
            ball.circle(20,90)
            ball.circle(20/2,90)
        ball.end_fill()
        window.update()
        ball.clear()
        # Border checking
        if ball.xcor() > x or ball.xcor() < x*-1:
            ball.fillcolor(colors[hit % 6])
            ball.dx *= -1
            hit += 1
        if ball.ycor() > y or ball.ycor() < y*-1:
            ball.fillcolor(colors[hit % 6])
            ball.dy *= -1
            hit += 1

def left():                     # upon user input to turn left
  player.left(90)
  #ph += 90
  #rayCast()
  window.update()

def right():                    # upon user input to turn right
  player.right(90)
  #ph -= 90
  #rayCast()
  window.update()

def move():                     # upon user input to move forward
  if player.distance(goal) < 20:
    window.update()
    window.bye()  # program ends if turtle enters square
  elif collision(player):
    window.title('Collision!')
    introtext.write('Collision!', move=False, align="center", font=("Times New Roman", 18, "bold"))
    print('Collision!')
    window.update()
  else:
    player.forward(10)
    #rayCast()
    window.update()

def cont(x,y):                  # continuation after user presses play
  cursor.goto(x, y)
  if cursor.distance(playbutton) < 30:
    os.system('cls')
    playbutton.ht()
    playbutton.goto(-1000,-1000)
    introtext.clear()
    main.clear()
    time.sleep(0.5)
    introtext.seth(270)
    introtext.forward(180)
    introtext.write('loading...', move=False, align="center", font=("Times New Roman", 18, "bold"))
    bb(40,40)
    introtext.clear()
    Initialize()
    drawMaze()
    window.update()
    window.onkey(left, 'a')
    window.onkey(right, 'd')
    window.onkey(move, 'w')
    window.listen()
    window.mainloop()

def Title():                    # title screen / main menu
  main.ht()
  introtext.ht()
  introtext.pu()
  introtext.seth(90)
  introtext.forward(90)
  introtext.pencolor('white')
  arg = "M     A     Z     E"
  window.title("M     A     Z     E")
  print("M     A     Z     E")
  stripeBG()
  drawBorder()
  introtext.write(arg, move=False, align="center", font=("Times New Roman", 64, "bold"))
  window.update()
  introtext.clear()
  time.sleep(0.2)
  os.system('cls')
  arg = "M    A    Z    E"
  window.title("M    A    Z    E")
  print("M    A    Z    E")
  moonRiver()
  drawBorder()
  introtext.write(arg, move=False, align="center", font=("Times New Roman", 64, "bold"))
  window.update()
  introtext.clear()
  time.sleep(0.2)
  os.system('cls')
  arg = "M   A   Z   E"
  window.title("M   A   Z   E")
  print("M   A   Z   E")
  aRock()
  drawBorder()
  introtext.write(arg, move=False, align="center", font=("Times New Roman", 64, "bold"))
  window.update()
  introtext.clear()
  time.sleep(0.2)
  os.system('cls')
  arg = "M  A  Z  E"
  window.title("M  A  Z  E")
  print("M  A  Z  E")
  theBridge()
  aRock()
  drawBorder()
  introtext.write(arg, move=False, align="center", font=("Times New Roman", 64, "bold"))
  window.update()
  introtext.clear()
  time.sleep(0.2)
  os.system('cls')
  arg = "M A Z E"
  window.title("M A Z E")
  print("M A Z E")
  sixtySeven()
  ninetyThree()
  drawBorder()
  introtext.write(arg, move=False, align="center", font=("Times New Roman", 64, "bold"))
  window.update()
  introtext.clear()
  time.sleep(0.2)
  os.system('cls')
  arg = "MAZE"
  window.title("MAZE")
  print("MAZE")
  drawBorder()
  introtext.write(arg, move=False, align="center", font=("Times New Roman", 64, "bold"))
  window.update()
  playbutton.shape('square')
  playbutton.shapesize(2.5)
  playbutton.color('white', 'white')
  playbutton.pu()
  playbutton.goto(-150, -150)
  playbutton.st()
  window.update()
  window.onclick(cont)
  introtext.forward(200)
  introtext.write('Click on the white button to play!', move=False, align="center", font=("Times New Roman", 18, "bold"))
  introtext.seth(270)
  introtext.forward(20)
  introtext.write('Or, Enter 0-6 in the console to see each individual layer.', move=False, align="center", font=("Times New Roman", 18, "bold"))
  print('Click on the white button to play!')
  print('Or, Enter 0-6 in the console to see each individual layer.')
  user = str(input())
  os.system('cls') 
  print('If you wish to continue, please restart this program.')
  if user == '0':
    main.clear()
    introtext.clear()
    playbutton.ht()
    drawBorder()
    window.update()
  elif user == '1':
    main.clear()
    introtext.clear()
    playbutton.ht()
    stripeBG()
    window.update()
  elif user == '2':
    main.clear()
    introtext.clear()
    playbutton.ht()
    moonRiver()
    window.update()
  elif user == '3':
    main.clear()
    introtext.clear()
    playbutton.ht()
    theBridge()
    window.update()
  elif user == '4':
    main.clear()
    introtext.clear()
    playbutton.ht()
    aRock()
    window.update()
  elif user == '5':
    main.clear()
    introtext.clear()
    playbutton.ht()
    sixtySeven()
    window.update()
  elif user == '6':
    main.clear()
    introtext.clear()
    playbutton.ht()
    ninetyThree()
    window.update()
  else:
    time.sleep(1)
# -:main:----------------------- #
Title()
window.exitonclick()