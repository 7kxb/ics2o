##########################################################################################
# Author: Kevin Xiang                       #                                            #
# Class: TEJ2O1                             #                                            #
# Teacher: Jey Anandarajan                  #                                            #
# Submitted: 10 June 2022                   #                                            #
#                                           #                                            #
# Scene 7 of 7                              #                                            #
# 54 Lines                                  #                                            #
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
ani = turtle.Turtle() # animation           # sets variable ani to turtle.Turtle()       #
ani.ht()                                    # hides turtle with name 'ani'               #
ani.pu()                                    # lifts pen up from turtle with name 'ani'   #
txt = turtle.Turtle() # background          # sets variable txt to turtle.Turtle()       #
txt.ht()                                    # hides turtle with name 'txt'               #
txt.pu()                                    # lifts pen up from turtle with name 'txt'   #
bg = turtle.Turtle() # background           # sets variable bg to turtle.Turtle()        #
bg.ht()                                     # hides turtle with name 'bg'                #
bg.pu()                                     # lifts pen up from turtle with name 'bg'    #
#                                           #                                            #
# functions / methods                       #                                            #
def titleText(x,y):                         #                                            #
    txt.pencolor('#ffffff')                 #                                            #
    txt.goto(x,y+40)                        #                                            #
    txt.write(                              #                                            #
    "Don't drink and drive"                 #                                            #
    , align='center'                        #                                            #
    , font=('Courier', 18, 'bold'))         #                                            #
    time.sleep(1)                           #                                            #
    txt.goto(x,y-40)                        #                                            #
    txt.write(                              #                                            #
    "The End."                              #                                            #
    , align='center'                        #                                            #
    , font=('Courier', 18, 'bold'))         #                                            #
    time.sleep(2)                           #                                            #
    return True                             #                                            #
#                                           #                                            #
# main #                                    #                                            #
if titleText(0,0):                          #                                            #
    window.bye()                            #                                            #
########################################################################################## 