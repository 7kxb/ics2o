##########################################################################################
# Author: Kevin Xiang                       #                                            #
# Class: TEJ2O1                             #                                            #
# Teacher: Jey Anandarajan                  #                                            #
# Submitted: 10 June 2022                   #                                            #
#                                           #                                            #
# DUI                                       #                                            #
# 114 Lines                                 #                                            #
#                                           #                                            #
# packages #                                #                                            #
import turtle                               # imports package turtle                     #
import os                                   # imports package os                         #
#                                           #                                            #
# initializing #                            #                                            #
width = 480                                 # sets variable width to 800                 #
height = 360                                # sets variable height to 600                #
window = turtle.Screen()                    # sets variable window to turtle.Screen()    #
window.setup(width,height,0,0)              # sets window dimensions to width and height #
window.bgcolor('#404040')                   # sets window background color to #404040    #
window.tracer(0)                            # sets window tracer to manual               #
#                                           #                                            #
# turtles #                                 #                                            #
main = turtle.Turtle()                      # sets variable main to turtle.Turtle()      #
main.ht()                                   # hides turtle with name 'main'              #
main.pu()                                   # lifts pen up from turtle with name 'main'  #
newgame = turtle.Turtle()                   # sets variable newgame to turtle.Turtle()   #
newgame.ht()                                # hides turtle with name 'newgame'           #
newgame.pu()                                # lift pen up from turtle with name 'newgame'#
cont = turtle.Turtle()                      # sets variable cont to turtle.Turtle()      #
cont.ht()                                   # hides turtle with name 'cont'              #
cont.pu()                                   # lifts pen up from turtle with name 'cont'  #
back = turtle.Turtle()                      # sets variable back to turtle.Turtle()      #
back.ht()                                   # hides turtle with name 'back'              #
back.pu()                                   # lifts pen up from turtle with name 'back'  #
#                                           #                                            #
# functions / methods #                     #                                            #
def cursor(x,y):                            #                                            #
    main.goto(x,y)                          #                                            #
    if main.distance(cont) < 50:            #                                            #
        file = open('./data/desktop.json'   #                                            #
        , 'r')                              #                                            #
        code = int(file.read())             #                                            #
        file.close()                        #                                            #
        window.bye()                        #                                            #
        if code != 1009:                    #                                            #
            os.system(                      #                                            #
                'python ./dui/scene2.py')   #                                            #
        else:                               #                                            #
            os.system(                      #                                            #
                'python ./dui/scene1.py')   #                                            #
    elif main.distance(newgame) < 50:       #                                            #
        file = open('./data/desktop.json'   #                                            #
        , 'w')                              #                                            #
        file.write('1009')                  #                                            #
        file.close()                        #                                            #
        window.bye()                        #                                            #
        os.system('python ./dui/scene1.py') #                                            #
    elif main.distance(back) < 50:          #                                            #
        window.bye()                        #                                            #
        os.system('python ./main.py')       #                                            #
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
    main.goto(-50,50)                       #                                            #
    main.begin_fill()                       #                                            #
    main.goto(-50,-50)                      #                                            #
    main.goto(50,-50)                       #                                            #
    main.goto(50,50)                        #                                            #
    main.goto(-50,50)                       #                                            #
    main.end_fill()                         #                                            #
    main.goto(0,200)                        #                                            #
    main.pencolor('#ffffff')                #                                            #
    main.pd()                               #                                            #
    main.write('cont'                       #                                            #
    , align='center'                        #                                            #
    , font=('Courier', 24, 'bold'))         #                                            #
    #                                       #                                            #
    newgame.pencolor('#000000')             #                                            #
    newgame.goto(0,0)                       #                                            #
    newgame.write('NEW', align='center'     #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    newgame.goto(0,-20)                     #                                            #
    newgame.write('GAME', align='center'    #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    cont.pencolor('#000000')                #                                            #
    cont.goto(150,-10)                      #                                            #
    cont.write('CONTINUE', align='center'   #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    back.pencolor('#000000')                #                                            #
    back.goto(-150,-10)                     #                                            #
    back.write('BACK', align='center'       #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    #                                       #                                            #
    window.update()                         #                                            #
    window.onclick(cursor)                  #                                            #
#                                           #                                            #
# main #                                    #                                            #
options()                                   #                                            #
wait = input()                              #                                            #
########################################################################################## 