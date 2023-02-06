##########################################################################################
# Author: Kevin Xiang                       #                                            #
# Class: TEJ2O1                             #                                            #
# Teacher: Jey Anandarajan                  #                                            #
# Submitted: 10 June 2022                   #                                            #
#                                           #                                            #
# Scene 5 of 7                              #                                            #
# 74 Lines                                  #                                            #
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
#                                           #                                            #
# functions / methods                       #                                            #
def titleText(x,y):                         #                                            #
    for _ in range(1,25):                   #                                            #
        ani.clear()                         #                                            #
        ani.goto(x-400-200+32*_,y+100)      #                                            #
        ani.fillcolor('#808080')            #                                            #
        ani.begin_fill()                    #                                            #
        ani.goto(x-400+100+32*_,y+100)      #                                            #
        ani.goto(x-400+100+32*_,y-100)      #                                            #
        ani.goto(x-400-200+32*_,y-100)      #                                            #
        ani.goto(x-400-200+32*_,y+100)      #                                            #
        ani.end_fill()                      #                                            #
        ani.goto(x-400-140+32*_,y-140)      #                                            #
        ani.fillcolor('#000000')            #                                            #
        ani.begin_fill()                    #                                            #
        ani.circle(40)                      #                                            #
        ani.end_fill()                      #                                            #
        ani.goto(x-400+40+32*_,y-140)       #                                            #
        ani.fillcolor('#000000')            #                                            #
        ani.begin_fill()                    #                                            #
        ani.circle(40)                      #                                            #
        ani.end_fill()                      #                                            #
        ani.goto(x-400-50+32*_,y+75)        #                                            #
        ani.fillcolor('#404040')            #                                            #
        ani.begin_fill()                    #                                            #
        ani.goto(x-400+50+32*_,y+75)        #                                            #
        ani.goto(x-400+50+32*_,y-25)        #                                            #
        ani.goto(x-400-50+32*_,y-25)        #                                            #
        ani.goto(x-400-50+32*_,y+75)        #                                            #
        ani.end_fill()                      #                                            #
        ani.goto(x-400-50+32*_,y+60)        #                                            #
        ani.fillcolor('#FFFF00')            #                                            #
        ani.begin_fill()                    #                                            #
        ani.goto(x-400+35+32*_,y+60)        #                                            #
        ani.goto(x-400+35+32*_,y-10)        #                                            #
        ani.goto(x-400-35+32*_,y-10)        #                                            #
        ani.goto(x-400-35+32*_,y+60)        #                                            #
        ani.end_fill()                      #                                            #
        window.update()                     #                                            #
        time.sleep(1/24)                    #                                            #
    return True                             #                                            #
#                                           #                                            #
# main #                                    #                                            #
if titleText(0,0):                          #                                            #
    window.bye()                            #                                            #
    os.system('python ./dui/scene6.py')     #                                            #
########################################################################################## 