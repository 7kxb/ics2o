##########################################################################################
# Author: Kevin Xiang                       #                                            #
# Class: TEJ2O1                             #                                            #
# Teacher: Jey Anandarajan                  #                                            #
# Submitted: 10 June 2022                   #                                            #
#                                           #                                            #
# MAIN                                      #                                            #
# 142 Lines                                 #                                            #
#                                           #                                            #
# packages #                                #                                            #
import turtle                               # imports package turtle                     #
import os                                   # imports package os                         #
#                                           #                                            #
# initializing #                            #                                            #
width = 800                                 # sets variable width to 800                 #
height = 600                                # sets variable height to 600                #
window = turtle.Screen()                    # sets variable window to turtle.Screen()    #
window.setup(width,height,0,0)              # sets window dimensions to width and height #
window.bgcolor('#404040')                   # sets window background color to #404040    #
window.tracer(0)                            # sets window tracer to manual               #
#                                           #                                            #
# turtles #                                 #                                            #
main = turtle.Turtle()                      # sets variable main to turtle.Turtle()      #
main.ht()                                   # hides turtle with name 'main'              #
main.pu()                                   # lifts pen up from turtle with name 'main'  #
maze = turtle.Turtle()                      # sets variable maze to turtle.Turtle()      #
maze.ht()                                   # hides turtle with name 'maze'              #
maze.pu()                                   # lifts pen up from turtle with name 'maze'  #
dui = turtle.Turtle()                       # sets variable dui to turtle.Turtle()       #
dui.ht()                                    # hides turtle with name 'dui'               #
dui.pu()                                    # lifts pen up from turtle with name 'dui'   #
#                                           #                                            #
# functions / methods #                     #                                            #
def cursor(x,y):                            #                                            #
    main.goto(x,y)                          #                                            #
    if main.distance(dui) < 50:             #                                            #
        window.bye()                        #                                            #
        os.system('python ./dui/scene0.py') #                                            #
    elif main.distance(maze) < 50:          #                                            #
        window.bye()                        #                                            #
        os.system('python ./old/reptile.py')#                                            #
#                                           #                                            #
def options():                              #                                            #
    main.goto(-200,50)                      #                                            #
    main.fillcolor('#ffffff')               #                                            #
    main.begin_fill()                       #                                            #
    main.goto(-200,-50)                     #                                            #
    main.goto(-100,-50)                     #                                            #
    main.goto(-100,50)                      #                                            #
    main.goto(-200,50)                      #                                            #
    main.end_fill()                         #                                            #
    main.goto(200,50)                       #                                            #
    main.begin_fill()                       #                                            #
    main.goto(200,-50)                      #                                            #
    main.goto(100,-50)                      #                                            #
    main.goto(100,50)                       #                                            #
    main.goto(200,50)                       #                                            #
    main.end_fill()                         #                                            #
    main.goto(0,200)                        #                                            #
    main.pencolor('#ffffff')                #                                            #
    main.pd()                               #                                            #
    main.write('ICS201'                     #                                            #
    , align='center'                        #                                            #
    , font=('Courier', 24, 'bold'))         #                                            #
    #                                       #                                            #
    maze.pencolor('#ffffff')                #                                            #
    maze.goto(-150,100)                     #                                            #
    maze.write('25 April 2022'              #                                            #
    , align='center'                        #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    maze.seth(270)                          #                                            #
    maze.forward(200)                       #                                            #
    maze.write('Requires:', align='center'  #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    maze.forward(20)                        #                                            #
    maze.write('Turtle', align='center'     #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    maze.forward(20)                        #                                            #
    maze.write('Time', align='center'       #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    maze.forward(20)                        #                                            #
    maze.write('OS', align='center'         #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    maze.forward(20)                        #                                            #
    maze.write('Random', align='center'     #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    maze.forward(20)                        #                                            #
    maze.write('Math', align='center'       #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    #                                       #                                            #
    dui.pencolor('#ffffff')                 #                                            #
    dui.goto(150,100)                       #                                            #
    dui.write('10 June 2022'                #                                            #
    , align='center'                        #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    dui.seth(270)                           #                                            #
    dui.forward(200)                        #                                            #
    dui.write('Requires:', align='center'   #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    dui.forward(20)                         #                                            #
    dui.write('Turtle', align='center'      #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    dui.forward(20)                         #                                            #
    dui.write('Time', align='center'        #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    dui.forward(20)                         #                                            #
    dui.write('OS', align='center'          #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    dui.forward(20)                         #                                            #
    dui.write('Datetime', align='center'    #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    dui.forward(20)                         #                                            #
    dui.write('Playsound 1.2.2*'            #                                            #
    , align='center'                        #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    dui.forward(20)                         #                                            #
    dui.write('Pygame', align='center'      #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    dui.forward(20)                         #                                            #
    dui.write('Math', align='center'        #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    dui.forward(20)                         #                                            #
    dui.write('Random', align='center'      #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    #                                       #                                            #
    maze.pencolor('#000000')                #                                            #
    maze.goto(-150,0)                       #                                            #
    maze.write('MAZE', align='center'       #                                            #
    , font=('Courier', 24, 'bold'))         #                                            #
    dui.pencolor('#000000')                 #                                            #
    dui.goto(150,0)                         #                                            #
    dui.write('DUI', align='center'         #                                            #
    , font=('Courier', 24, 'bold'))         #                                            #
    #                                       #                                            #
    print('pip install playsound==1.2.2 ')  #                                            #
    window.update()                         #                                            #
    window.onclick(cursor)                  #                                            #
#                                           #                                            #
# main #                                    #                                            #
options()                                   #                                            #
wait = input()                              #                                            #
########################################################################################## 