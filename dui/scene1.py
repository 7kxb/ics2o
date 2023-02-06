##########################################################################################
# Author: Kevin Xiang                       #                                            #
# Class: TEJ2O1                             #                                            #
# Teacher: Jey Anandarajan                  #                                            #
# Submitted: 10 June 2022                   #                                            #
#                                           #                                            #
# Scene 1 of 7                              #                                            #
# 93 Lines                                  #                                            #
#                                           #                                            #
# packages #                                #                                            #
import turtle                               # imports package turtle                     #
import time                                 # imports package time                       #
import os                                   # imports package os                         #
#                                           #                                            #
# initializing #                            #                                            #
width = 800                                 # sets variable width to 800                 #
height = 450                                # sets variable height to 450                #
window = turtle.Screen()                    # sets variable window to turtle.Screen()    #
window.setup(width,height,0,0)              # sets window dimensions to width and height #
window.bgcolor('#404040')                   # sets window background color to #404040    #
window.tracer(0)                            # sets window tracer to manual               #
#                                           #                                            #
# turtles #                                 #                                            #
bg = turtle.Turtle() # background           # sets variable bg to turtle.Turtle()        #
bg.ht()                                     # hides turtle with name 'bg'                #
bg.pu()                                     # lifts pen up from turtle with name 'bg'    #
ani = turtle.Turtle() # animation           # sets variable ani to turtle.Turtle()       #
ani.ht()                                    # hides turtle with name 'ani'               #
ani.pu()                                    # lifts pen up from turtle with name 'ani'   #
txt = turtle.Turtle() # text                # sets variable txt to turtle.Turtle()       #
txt.ht()                                    # hides turtle with name 'txt'               #
txt.pu()                                    # lifts pen up from turtle with name 'txt'   #
window.addshape('./images/bg.gif')          # add bg.gif from folder images as a shape   #
bg.shape('./images/bg.gif')                 # assigns shape to turtle with name 'bg'     #
bg.st()                                     # shows turtle with name 'bg'                #
#                                           #                                            #
# functions / methods                       #                                            #
def titleText(x,y):                         #                                            #
    txt.pencolor('#ffffff')                 #                                            #
    txt.goto(x,y-75)                        #                                            #
    for i in range(1, 48):                  #                                            #
        if i >= 20 and i < 30:              #                                            #
            txt.clear()                     #                                            #
            txt.write('D  ', align='center' #                                            #
            , font=('Courier', 100, 'bold'))#                                            #
        if i >= 30 and i < 40:              #                                            #
            txt.clear()                     #                                            #
            txt.write('DU ', align='center' #                                            #
            , font=('Courier', 100, 'bold'))#                                            #
        if i >= 40:                         #                                            #
            txt.clear()                     #                                            #
            txt.write('DUI', align='center' #                                            #
            , font=('Courier', 100, 'bold'))#                                            #
        ani.clear()                         #                                            #
        ani.goto(x-300/i,y+300/i)           #                                            #
        ani.fillcolor('#FDDA16')            #                                            #
        ani.begin_fill()                    #                                            #
        ani.goto(x-400/i,y+250/i)           #                                            #
        ani.goto(x-450/i,y+350/i)           #                                            #
        ani.goto(x-350/i,y+400/i)           #                                            #
        ani.end_fill()                      #                                            #
        window.update()                     #                                            #
        time.sleep(2/24)                    #                                            #
    ani.clear()                             #                                            #
    bg.ht()                                 #                                            #
    for i in range(1, 12):                  #                                            #
        ani.clear()                         #                                            #
        ani.goto(x-width/2,y)               #                                            #
        ani.fillcolor('#808080')            #                                            #
        ani.begin_fill()                    #                                            #
        ani.goto(x,y+100*(1/5)**i)          #                                            #
        ani.goto(x+width/2,y)               #                                            #
        ani.goto(x,y-100*(1/5)**i)          #                                            #
        ani.goto(x-width/2,y)               #                                            #
        ani.end_fill()                      #                                            #
        txt.clear()                         #                                            #
        txt.write(                          #                                            #
            'DUI',                          #                                            #
            align='center',                 #                                            #
            font=('Courier', 100, 'bold'))  #                                            #
        window.update()                     #                                            #
        time.sleep(2/24)                    #                                            #
    txt.goto(x,y-150)                       #                                            #
    txt.write(                              #                                            #
        'Click to continue.',               #                                            #
        align = 'center',                   #                                            #
        font = ('Courier', 25, 'bold'))     #                                            #
#                                           #                                            #
# main #                                    #                                            #
titleText(0,0)                              #                                            #
window.exitonclick()                        #                                            #
os.system('python ./dui/scene2.py')         #                                            #
########################################################################################## 