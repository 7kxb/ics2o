##########################################################################################
# Author: Kevin Xiang                       #                                            #
# Class: TEJ2O1                             #                                            #
# Teacher: Jey Anandarajan                  #                                            #
# Submitted: 10 June 2022                   #                                            #
#                                           #                                            #
# Scene 2 of 7                              #                                            #
# 460 Lines                                 #                                            #
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
window.addshape('./images/desktop.gif')     # add desktop from folder images as a shape  #
bg.shape('./images/desktop.gif')            # assigns shape to turtle with name bg       #
bg.st()                                     # shows turtle with name bg                  #
cursor = turtle.Turtle()                    # sets variable pc to turtle.Turtle()        #
cursor.ht()                                 # hides turtle with name cursor              #
cursor.pu()                                 # lifts pen up from turtle with name cursor  #
graphics = turtle.Turtle()                  # sets variable grapgics to turtle.Turtle()  #
graphics.ht()                               # hides turtle with name graphics            #
graphics.pu()                               # lifts pen up from turtle with name graphics#
firefox = turtle.Turtle()                   # sets variable firefox to turtle.Turtle(    #
firefox.ht()                                # hides turtle with name firefox             #
firefox.pu()                                # lifts pen up from turtle with name firefox #
discord = turtle.Turtle()                   # sets variable discord to turtle.Turtle()   #
discord.ht()                                # hides turtle with name discord             #
discord.pu()                                # lifts pen up from turtle with name discord #
save = turtle.Turtle()                      # sets variable discord to turtle.Turtle()   #
save.ht()                                   # hides turtle with name save                #
save.pu()                                   # lifts pen up from turtle with name save    #
load = turtle.Turtle()                      # sets variable load to turtle.Turtle()      #
load.ht()                                   # hides turtle with name load                #
load.pu()                                   # lifts pen up from turtle with name load    #
mathrun = turtle.Turtle()                   # sets mathrun to turtle.Turtle()            #
mathrun.ht()                                # hides turtle math run                      #
mathrun.pu()                                # lifts pen up from turtle math run          #
biscuittapper = turtle.Turtle()             # sets biscuittapper to turtle.Turtle()      #
biscuittapper.ht()                          # hides turtle biscuittapper                 #
biscuittapper.pu()                          # lifts pen up from turtle biscuittapper     #
window.addshape('./images/biscuit.gif')     # add desktop from folder images as a shape  #
close = turtle.Turtle()                     # sets close to turtle.Turtle()              #
close.ht()                                  # hides turtle close                         #
close.pu()                                  # lifts pen up from turtle close             #
close.goto(-1000,1000)                      #                                            #
close2 = turtle.Turtle()                    # sets close2 to turtle.Turtle()             #
close2.ht()                                 # hides turtle close2                        #
close2.pu()                                 # lifts pen up from turtle close2            #
close2.goto(-1000,1000)                     #                                            #
#                                           #                                            #
# variables #                               #                                            #
toggle_bt = True                            #                                            #
toggle_mr = True                            #                                            #
biscuits = 0                                #                                            #
file = open('./data/desktop.json', 'r')     #                                            #
code = int(file.read())                     #                                            #
file.close()                                #                                            #
if code == 1009:                            #                                            #
    file = open('./data/desktop.json', 'w') #                                            #
    file.write('1013')                      #                                            #
    file.close()                            #                                            #
if code == 1031:                            #                                            #
    window.bye()                            #                                            #
    os.system('python ./dui/scene5.py')     #                                            #
#                                           #                                            #
# functions / methods #                     #                                            #
def click(x,y):                             #                                            #
    global toggle_mr                        #                                            #
    global toggle_bt                        #                                            #
    global biscuits                         #                                            #
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
    if cursor.distance(firefox) < 80:       #                                            #
        if code < 1021:                     #                                            #
            file = open(                    #                                            #
                './data/desktop.json'       #                                            #
            , 'w')                          #                                            #
            file.write('1019')              #                                            #
            file.close()                    #                                            #
        window.bye()                        #                                            #
        os.system('python ./dui/scene3.py') #                                            #
    if cursor.distance(discord) < 80:       #                                            #
        if code < 1031:                     #                                            #
            file = open(                    #                                            #
                './data/desktop.json'       #                                            #
            , 'w')                          #                                            #
            file.write('1021')              #                                            #
            file.close()                    #                                            #
        window.bye()                        #                                            #
        os.system('python ./dui/scene4.py') #                                            #
    if cursor.distance(save) < 25:          #                                            #
        file = open('./data/biscuits.json'  #                                            #
        , 'w')                              #                                            #
        file.write(str(biscuits))           #                                            #
        file.close()                        #                                            #
        toggle_bt = True                    #                                            #
        graphics.clear()                    #                                            #
        biscuittapper.clear()               #                                            #
        biscuittapper.ht()                  #                                            #
        biscuittapper.shape('turtle')       #                                            #
        biscuittapper.goto(-345,-20)        #                                            #
        close.clear()                       #                                            #
        close.goto(-1000,1000)              #                                            #
        graphics.goto(-50,25)               #                                            #
        graphics.fillcolor('#C4C4C4')       #                                            #
        graphics.begin_fill()               #                                            #
        graphics.goto(-50,-25)              #                                            #
        graphics.goto(50,-25)               #                                            #
        graphics.goto(50,25)                #                                            #
        graphics.goto(-50,25)               #                                            #
        graphics.end_fill()                 #                                            #
        graphics.goto(0,-10)                #                                            #
        graphics.write('Saved!',            #                                            #
            align='center',                 #                                            #
            font=('Courier', 12, 'bold'))   #                                            #
        window.update()                     #                                            #
        time.sleep(1)                       #                                            #
        graphics.clear()                    #                                            #
    if cursor.distance(load) < 25:          #                                            #
        file = open('./data/biscuits.json'  #                                            #
        , 'r')                              #                                            #
        biscuits = int(file.read())         #                                            #
        file.close()                        #                                            #
        toggle_bt = True                    #                                            #
        graphics.clear()                    #                                            #
        biscuittapper.clear()               #                                            #
        biscuittapper.ht()                  #                                            #
        biscuittapper.shape('turtle')       #                                            #
        biscuittapper.goto(-345,-20)        #                                            #
        close.clear()                       #                                            #
        close.goto(-1000,1000)              #                                            #
        graphics.goto(-50,25)               #                                            #
        graphics.fillcolor('#C4C4C4')       #                                            #
        graphics.begin_fill()               #                                            #
        graphics.goto(-50,-25)              #                                            #
        graphics.goto(50,-25)               #                                            #
        graphics.goto(50,25)                #                                            #
        graphics.goto(-50,25)               #                                            #
        graphics.end_fill()                 #                                            #
        graphics.goto(0,-10)                #                                            #
        graphics.write('Loaded!',           #                                            #
            align='center',                 #                                            #
            font=('Courier', 12, 'bold'))   #                                            #
        window.update()                     #                                            #
        time.sleep(1)                       #                                            #
        graphics.clear()                    #                                            #
    if cursor.distance(mathrun) < 25:       #                                            #
        if toggle_mr:                       #                                            #
            toggle_mr = False               #                                            #
            mathrun.goto(-100,25)           #                                            #
            mathrun.fillcolor('#C4C4C4')    #                                            #
            mathrun.begin_fill()            #                                            #
            mathrun.goto(-100,-25)          #                                            #
            mathrun.goto(100,-25)           #                                            #
            mathrun.goto(100,25)            #                                            #
            mathrun.goto(-100,25)           #                                            #
            mathrun.end_fill()              #                                            #
            mathrun.goto(0,-10)             #                                            #
            mathrun.write(                  #                                            #
                'extras.dll not found.',    #                                            #
                align='center',             #                                            #
                font=('Courier', 8, 'bold'))#                                            #
            close2.goto(100,25)             #                                            #
            close2.fillcolor('#FF0000')     #                                            #
            close2.begin_fill()             #                                            #
            close2.goto(100,5)              #                                            #
            close2.goto(80,5)               #                                            #
            close2.goto(80,25)              #                                            #
            close2.goto(100,25)             #                                            #
            close2.end_fill()               #                                            #
            close2.goto(90,5)               #                                            #
            close2.write('X',               #                                            #
            align='center',                 #                                            #
            font=('Courier', 10, 'bold'))   #                                            #
            close2.goto(90,15)              #                                            #
    if cursor.distance(close2) < 20:        #                                            #
        if not toggle_mr:                   #                                            #
            mathrun.clear()                 #                                            #
            close2.clear()                  #                                            #
            close2.goto(-1000,1000)         #                                            #
            mathrun.goto(-345,60)           #                                            #
            toggle_mr = True                #                                            #
    if cursor.distance(biscuittapper) < 64: #                                            #
        if toggle_bt and cursor.distance(   #                                            #
            biscuittapper) < 25:            #                                            #
            toggle_bt = False               #                                            #
            graphics.goto(320,130)          #                                            #
            graphics.fillcolor('#408080')   #                                            #
            graphics.begin_fill()           #                                            #
            graphics.goto(110,130)          #                                            #
            graphics.goto(110,-90)          #                                            #
            graphics.goto(330,-90)          #                                            #
            graphics.goto(330,130)          #                                            #
            graphics.end_fill()             #                                            #
            graphics.goto(320,120)          #                                            #
            graphics.fillcolor('#80FFFF')   #                                            #
            graphics.begin_fill()           #                                            #
            graphics.goto(120,120)          #                                            #
            graphics.goto(120,-80)          #                                            #
            graphics.goto(320,-80)          #                                            #
            graphics.goto(320,120)          #                                            #
            graphics.end_fill()             #                                            #
            biscuittapper.goto(220,20)      #                                            #
            biscuittapper.shape(            #                                            #
                './images/biscuit.gif')     #                                            #
            biscuittapper.st()              #                                            #
        if not toggle_bt:                   #                                            #
            biscuits += 1                   #                                            #
            biscuittapper.clear()           #                                            #
            biscuittapper.goto(220,-70)     #                                            #
            biscuittapper.write(            #                                            #
            'Biscuits: '+str(biscuits),     #                                            #
            align='center',                 #                                            #
            font=('Courier', 12, 'bold'))   #                                            #
            biscuittapper.goto(220,30)      #                                            #
            window.update()                 #                                            #
            playsound('./sfx/click.mp3')    #                                            #
            biscuittapper.goto(220,20)      #                                            #
            close.clear()                   #                                            #
            close.goto(320,120)             #                                            #
            close.fillcolor('#FF0000')      #                                            #
            close.begin_fill()              #                                            #
            close.goto(320,100)             #                                            #
            close.goto(300,100)             #                                            #
            close.goto(300,120)             #                                            #
            close.goto(320,120)             #                                            #
            close.end_fill()                #                                            #
            close.goto(310,100)             #                                            #
            close.write('X',                #                                            #
            align='center',                 #                                            #
            font=('Courier', 10, 'bold'))   #                                            #
            close.goto(310,110)             #                                            #
    if cursor.distance(close) < 20:         #                                            #
        toggle_bt = True                    #                                            #
        graphics.clear()                    #                                            #
        biscuittapper.clear()               #                                            #
        biscuittapper.ht()                  #                                            #
        biscuittapper.shape('turtle')       #                                            #
        biscuittapper.goto(-345,-20)        #                                            #
        close.clear()                       #                                            #
        close.goto(-1000,1000)              #                                            #
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
    # bottom dock                           #                                            #
    pc.goto(-200,-215)                      #                                            #
    pc.fillcolor('#808080')                 #                                            #
    pc.begin_fill()                         #                                            #
    pc.goto(200,-215)                       #                                            #
    pc.goto(200,-185)                       #                                            #
    pc.goto(-200,-185)                      #                                            #
    pc.goto(-200,-215)                      #                                            #
    pc.end_fill()                           #                                            #
    # firefox                               #                                            #
    pc.goto(-180,-210)                      #                                            #
    pc.fillcolor('#FF9500')                 #                                            #
    pc.begin_fill()                         #                                            #
    pc.circle(10)                           #                                            #
    pc.end_fill()                           #                                            #
    pc.goto(-180,-206)                      #                                            #
    pc.fillcolor('#00539F')                 #                                            #
    pc.begin_fill()                         #                                            #
    pc.circle(6)                            #                                            #
    pc.end_fill()                           #                                            #
    pc.goto(-165,-217)                      #                                            #
    pc.write('Firefox', align='left'        #                                            #
    , font=('Courier', 20, 'bold'))         #                                            #
    firefox.goto(-125,-250)                 #                                            #
    # tab seperator                         #                                            #
    pc.goto(-2,-210)                        #                                            #
    pc.fillcolor('#ffffff')                 #                                            #
    pc.begin_fill()                         #                                            #
    pc.goto(-2,-190)                        #                                            #
    pc.goto(2,-190)                         #                                            #
    pc.goto(2,-210)                         #                                            #
    pc.goto(-2,-210)                        #                                            #
    pc.end_fill()                           #                                            #
    # discord                               #                                            #
    pc.goto(22,-210)                        #                                            #
    pc.fillcolor('#7289DA')                 #                                            #
    pc.begin_fill()                         #                                            #
    pc.circle(10)                           #                                            #
    pc.end_fill()                           #                                            #
    pc.goto(22,-206)                        #                                            #
    pc.fillcolor('#ffffff')                 #                                            #
    pc.begin_fill()                         #                                            #
    pc.circle(6)                            #                                            #
    pc.end_fill()                           #                                            #
    pc.goto(37,-217)                        #                                            #
    pc.write('Discord', align='left'        #                                            #
    , font=('Courier', 20, 'bold'))         #                                            #
    discord.goto(77,-250)                   #                                            #
    # save                                  #                                            #
    pc.goto(-370,170)                       #                                            #
    pc.begin_fill()                         #                                            #
    pc.goto(-320,170)                       #                                            #
    pc.goto(-320,120)                       #                                            #
    pc.goto(-370,120)                       #                                            #
    pc.goto(-370,170)                       #                                            #
    pc.end_fill()                           #                                            #
    pc.goto(-345,140)                       #                                            #
    pc.pencolor('#000000')                  #                                            #
    pc.write('SAVE', align='center'         #                                            #
    , font=('Courier', 8, 'bold'))          #                                            #
    save.goto(-345,140)                     #                                            #
    # load                                  #                                            #
    pc.goto(-290,170)                       #                                            #
    pc.begin_fill()                         #                                            #
    pc.goto(-240,170)                       #                                            #
    pc.goto(-240,120)                       #                                            #
    pc.goto(-290,120)                       #                                            #
    pc.goto(-290,170)                       #                                            #
    pc.end_fill()                           #                                            #
    pc.goto(-265,140)                       #                                            #
    pc.write('LOAD', align='center'         #                                            #
    , font=('Courier', 8, 'bold'))          #                                            #
    load.goto(-265,140)                     #                                            #
    # math run                              #                                            #
    pc.goto(-370,90)                        #                                            #
    pc.begin_fill()                         #                                            #
    pc.goto(-320,90)                        #                                            #
    pc.goto(-320,40)                        #                                            #
    pc.goto(-370,40)                        #                                            #
    pc.goto(-370,90)                        #                                            #
    pc.end_fill()                           #                                            #
    pc.goto(-345,65)                        #                                            #
    pc.write('Math', align='center'         #                                            #
    , font=('Courier', 8, 'bold'))          #                                            #
    pc.goto(-345,55)                        #                                            #
    pc.write('Run', align='center'          #                                            #
    , font=('Courier', 8, 'bold'))          #                                            #
    mathrun.goto(-345,60)                   #                                            #
    # biscuit tapper                        #                                            #
    pc.goto(-370,10)                        #                                            #
    pc.begin_fill()                         #                                            #
    pc.goto(-320,10)                        #                                            #
    pc.goto(-320,-40)                       #                                            #
    pc.goto(-370,-40)                       #                                            #
    pc.goto(-370,10)                        #                                            #
    pc.end_fill()                           #                                            #
    pc.goto(-345,-15)                       #                                            #
    pc.write('Biscuit', align='center'      #                                            #
    , font=('Courier', 8, 'bold'))          #                                            #
    pc.goto(-345,-25)                       #                                            #
    pc.write('Tapper', align='center'       #                                            #
    , font=('Courier', 8, 'bold'))          #                                            #
    biscuittapper.goto(-345,-20)            #                                            #
    # sequence                              #                                            #
    file = open('./data/desktop.json'       #                                            #
    , 'r')                                  #                                            #
    check = int(file.read())                #                                            #
    file.close()                            #                                            #
    if check == 1013:                       #                                            #
        window.update()                     #                                            #
        playsound('./sfx/mint.mp3')         #                                            #
    click(0,0)                              #                                            #
    if check <= 1019:                       #                                            #
        pc.goto(26,-202)                    #                                            #
        pc.fillcolor('#ff0000')             #                                            #
        pc.begin_fill()                     #                                            #
        pc.circle(6)                        #                                            #
        pc.end_fill()                       #                                            #
        pc.goto(26,-200)                    #                                            #
        pc.fillcolor('#ffffff')             #                                            #
        pc.begin_fill()                     #                                            #
        pc.circle(4)                        #                                            #
        pc.end_fill()                       #                                            #
    if check == 1013:                       #                                            #
        window.update()                     #                                            #
        playsound('./sfx/ping.mp3')         #                                            #
    window.onclick(click)                   #                                            #
#                                           #                                            #
# main #                                    #                                            #
desktop()                                   #                                            #
wait = input()                              #                                            #
########################################################################################## 