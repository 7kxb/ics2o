##########################################################################################
# Author: Kevin Xiang                       #                                            #
# Class: TEJ2O1                             #                                            #
# Teacher: Jey Anandarajan                  #                                            #
# Submitted: 10 June 2022                   #                                            #
#                                           #                                            #
# Scene 4 of 7                              #                                            #
# 244 Lines                                 #                                            #
#                                           #                                            #
# packages #                                #                                            #
import turtle                               # imports package turtle                     #
import time                                 # imports package time                       #
import os                                   # imports package os                         #
import datetime                             # imports package datetime                   #
from playsound import playsound             # imports package playsound                  #
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
pc = turtle.Turtle()                        # sets variable pc to turtle.Turtle()        #
pc.ht()                                     # hides turtle with name pc                  #
pc.pu()                                     # lifts pen up from turtle with name pc      #
bg = turtle.Turtle()                        # sets variable bg to turtle.Turtle()        #
bg.ht()                                     # hides turtle with name bg                  #
bg.pu()                                     # lifts pen up from turtle with name bg      #
window.addshape('./images/discord.gif')     # add discord from folder images as a shape  #
bg.shape('./images/discord.gif')            # assigns shape to turtle with name bg       #
bg.st()                                     # shows turtle with name bg                  #
cursor = turtle.Turtle()                    # sets variable pc to turtle.Turtle()        #
cursor.ht()                                 # hides turtle with name cursor              #
cursor.pu()                                 # lifts pen up from turtle with name cursor  #
graphics = turtle.Turtle()                  # sets variable grapgics to turtle.Turtle()  #
graphics.ht()                               # hides turtle with name graphics            #
graphics.pu()                               # lifts pen up from turtle with name graphics#
close = turtle.Turtle()                     # sets close to turtle.Turtle()              #
close.ht()                                  # hides turtle close                         #
close.pu()                                  # lifts pen up from turtle close             #
close.goto(-1000,1000)                      #                                            #
#                                           #                                            #
# functions / methods #                     #                                            #
def click(x,y):                             #                                            #
    cursor.pu()                             #                                            #
    cursor.goto(x,y)                        #                                            #
    cursor.clear()                          #                                            #
    cursor.pencolor('#ffffff')              #                                            #
    cursor.pd()                             #                                            #
    cursor.fillcolor('#404040')             #                                            #
    cursor.begin_fill()                     #                                            #
    cursor.goto(x,y-14)                     #                                            #
    cursor.goto(x+2,y-12)                   #                                            #
    cursor.goto(x+4,y-16)                   #                                            #
    cursor.goto(x+8,y-14)                   #                                            #
    cursor.goto(x+6,y-10)                   #                                            #
    cursor.goto(x+10,y-10)                  #                                            #
    cursor.goto(x,y)                        #                                            #
    cursor.end_fill()                       #                                            #
    if cursor.distance(close) < 20:         #                                            #
        window.bye()                        #                                            #
        os.system('python ./dui/scene2.py') #                                            #
    if cursor.distance(pc) < 30:            #                                            #
        graphics.clear()                    #                                            #
        graphics.goto(-200,170)             #                                            #
        graphics.fillcolor('#36393E')       #                                            #
        graphics.begin_fill()               #                                            #
        graphics.goto(-200,-170)            #                                            #
        graphics.goto(370,-170)             #                                            #
        graphics.goto(370,170)              #                                            #
        graphics.goto(-200,170)             #                                            #
        graphics.end_fill()                 #                                            #
        graphics.goto(-165,-45)             #                                            #
        graphics.fillcolor('#7289DA')       #                                            #
        graphics.begin_fill()               #                                            #
        graphics.circle(10)                 #                                            #
        graphics.end_fill()                 #                                            #
        graphics.pencolor('#ffffff')        #                                            #
        graphics.goto(-140,-50)             #                                            #
        graphics.write('smeller'            #                                            #
        , align='left'                      #                                            #
        , font=('Courier', 18, 'bold'))     #                                            #
        graphics.goto(-180,-70)             #                                            #
        graphics.write('yo can you join '+  #                                            #
        'us at the pub tonight? ;)'         #                                            #
        , align='left'                      #                                            #
        , font=('Courier', 12, 'bold'))     #                                            #
        graphics.goto(-165,-95)             #                                            #
        graphics.fillcolor('#FFFF00')       #                                            #
        graphics.begin_fill()               #                                            #
        graphics.circle(10)                 #                                            #
        graphics.end_fill()                 #                                            #
        graphics.pencolor('#ffffff')        #                                            #
        graphics.goto(-140,-100)             #                                            #
        graphics.write('Yellow Square'      #                                            #
        , align='left'                      #                                            #
        , font=('Courier', 18, 'bold'))     #                                            #
        graphics.goto(-180,-120)             #                                            #
        graphics.write('bet'                #                                            #
        , align='left'                      #                                            #
        , font=('Courier', 12, 'bold'))     #                                            #
        graphics.goto(-180,-80)             #                                            #
        graphics.fillcolor('#7289DA')       #                                            #
        graphics.begin_fill()               #                                            #
        graphics.goto(-180,-160)            #                                            #
        graphics.goto(-90,-160)             #                                            #
        graphics.goto(-90,-130)             #                                            #
        graphics.goto(-180,-130)            #                                            #
        graphics.end_fill()                 #                                            #
        graphics.goto(-135,-155)            #                                            #
        graphics.write('LEAVE'              #                                            #
        , align='center'                    #                                            #
        , font=('Courier', 12, 'bold'))     #                                            #
        file = open('./data/desktop.json'   #                                            #
        , 'w')                              #                                            #
        file.write('1031')                  #                                            #
        file.close()                        #                                            #
        close.goto(-135,-145)               #                                            #
    window.update()                         #                                            #
#                                           #                                            #
def desktop():                              #                                            #
    # top panel                             #                                            #
    pc.goto(-400,225)                       #                                            #
    pc.fillcolor('#808080')                 #                                            #
    pc.begin_fill()                         #                                            #
    pc.goto(400,225)                        #                                            #
    pc.goto(400,195)                        #                                            #
    pc.goto(-400,195)                       #                                            #
    pc.goto(-400,225)                       #                                            #
    pc.end_fill()                           #                                            #
    # clock                                 #                                            #
    if len(str(datetime.datetime.now(       #                                            #
    ).minute)) == 1:                        #                                            #
        pc.goto(390,193)                    #                                            #
        pc.pencolor('#ffffff')              #                                            #
        pc.write(str(                       #                                            #
        datetime.datetime.now(              #                                            #
        ).hour)+':0'+str(                   #                                            #
        datetime.datetime.now(              #                                            #
        ).minute), align='right', font=(    #                                            #
        'Courier', 20, 'bold'))             #                                            #
    elif len(str(datetime.datetime.now(     #                                            #
    ).minute)) == 2:                        #                                            #
        pc.goto(390,193)                    #                                            #
        pc.pencolor('#ffffff')              #                                            #
        pc.write(str(                       #                                            #
        datetime.datetime.now(              #                                            #
        ).hour)+':'+str(                    #                                            #
        datetime.datetime.now(              #                                            #
        ).minute), align='right', font=(    #                                            #
        'Courier', 20, 'bold'))             #                                            #
    pc.fillcolor('#ffffff')                 #                                            #
    pc.goto(300,220)                        #                                            #
    pc.begin_fill()                         #                                            #
    pc.goto(300,200)                        #                                            #
    pc.goto(295,200)                        #                                            #
    pc.goto(295,220)                        #                                            #
    pc.goto(300,220)                        #                                            #
    pc.end_fill()                           #                                            #
    # desktop                               #                                            #
    pc.goto(-385,200)                       #                                            #
    pc.begin_fill()                         #                                            #
    pc.circle(10)                           #                                            #
    pc.end_fill()                           #                                            #
    pc.goto(-365,220)                       #                                            #
    pc.begin_fill()                         #                                            #
    pc.goto(-365,200)                       #                                            #
    pc.goto(-360,200)                       #                                            #
    pc.goto(-360,220)                       #                                            #
    pc.goto(-365,220)                       #                                            #
    pc.end_fill()                           #                                            #
    pc.goto(-350,193)                       #                                            #
    pc.write('Desktop', align='left'        #                                            #
    , font=('Courier', 20, 'bold'))         #                                            #
    # close                                 #                                            #
    close.goto(360,195)                     #                                            #
    close.fillcolor('#C4C4C4')              #                                            #
    close.begin_fill()                      #                                            #
    close.goto(-400,195)                    #                                            #
    close.goto(-400,175)                    #                                            #
    close.goto(360,175)                     #                                            #
    close.goto(360,195)                     #                                            #
    close.end_fill()                        #                                            #
    close.goto(400,195)                     #                                            #
    close.fillcolor('#FF0000')              #                                            #
    close.begin_fill()                      #                                            #
    close.goto(360,195)                     #                                            #
    close.goto(360,175)                     #                                            #
    close.goto(400,175)                     #                                            #
    close.goto(400,195)                     #                                            #
    close.end_fill()                        #                                            #
    close.goto(-380,175)                    #                                            #
    close.write('Discord', align='left'     #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    close.goto(380,175)                     #                                            #
    close.write('X', align='center'         #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    #                                       #                                            #
    graphics.goto(-200,170)                 #                                            #
    graphics.fillcolor('#36393E')           #                                            #
    graphics.begin_fill()                   #                                            #
    graphics.goto(-200,-170)                #                                            #
    graphics.goto(370,-170)                 #                                            #
    graphics.goto(370,170)                  #                                            #
    graphics.goto(-200,170)                 #                                            #
    graphics.end_fill()                     #                                            #
    graphics.goto(-165,-95)                 #                                            #
    graphics.fillcolor('#7289DA')           #                                            #
    graphics.begin_fill()                   #                                            #
    graphics.circle(10)                     #                                            #
    graphics.end_fill()                     #                                            #
    graphics.pencolor('#ffffff')            #                                            #
    graphics.goto(-140,-100)                #                                            #
    graphics.write('smeller', align='left'  #                                            #
    , font=('Courier', 18, 'bold'))         #                                            #
    graphics.goto(-180,-120)                #                                            #
    graphics.write('yo can you join us at'+ #                                            #
    ' the pub tonight? ;)', align='left'    #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    graphics.goto(-180,-130)                #                                            #
    graphics.fillcolor('#7289DA')           #                                            #
    graphics.begin_fill()                   #                                            #
    graphics.goto(-180,-160)                #                                            #
    graphics.goto(-90,-160)                 #                                            #
    graphics.goto(-90,-130)                 #                                            #
    graphics.goto(-180,-130)                #                                            #
    graphics.end_fill()                     #                                            #
    graphics.goto(-135,-155)                #                                            #
    graphics.write('REPLY', align='center'  #                                            #
    , font=('Courier', 12, 'bold'))         #                                            #
    pc.goto(-135,-145)                      #                                            #
    #                                       #                                            #
    bg.goto(0,-30)                          #                                            #
    window.update()                         #                                            #
    click(0,0)                              #                                            #
    window.onclick(click)                   #                                            #
#                                           #                                            #
# main #                                    #                                            #
desktop()                                   #                                            #
wait = input()                              #                                            #
########################################################################################## 