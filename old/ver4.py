# Author: Kevin Xiang                           #
# Class: TEJ2O1                                 #
# Teacher: Jey Anandarajan                      #
# Submitted: 8 June 2022                        #
#                                               #
# packages #                                    #
import pygame as pg                             #imports package called pygame  (movement, collision, and raycasting)
import turtle                                   #imports package called turtle  (provides visual, may crash on nt/win32)
import sys                                      #imports package called sys     (this is to work well with pygame)
import os                                       #imports package called os      (this is for myself to defer unix)
import math                                     #imports package called math    (this is to calculate circles)
from timer import timer                         #imports package called timer   (this is to calculate fps)
# initializing #                                #
pg.init()                                       #initializes pygame
WIDTH = 600                                     #sets variable window width to 600
HEIGHT = 600                                    #sets variable window height to 600
screen = pg.display.set_mode((WIDTH,HEIGHT))    #inits screen to those variables
clock = pg.time.Clock()                         #inits variable clock from attribute
if os.name == 'nt' or sys.platform == 'win32':  #if the os running this py is nt/win32
    from ctypes import windll                   #imports package called windll from ctypes
    hwnd = pg.display.get_wm_info()['window']   #sets variable to window info
    windll.user32.MoveWindow(                   #moves window
        hwnd,40,40,WIDTH,HEIGHT,False)          #to 40,40 (top-left corner)
print('init')                                   #print 'init' for debugging purposes
# variables #                                   #
global fov                                      #makes fov global to make accessable for functions
fov = 120                                       #set fov to 120
global res                                      #makes res global to make accessable for functions
res = 3                                         #set res to 3
global fog                                      #makes fog global to make accessable for functions
fog = 6                                         #set fog to 6
global health                                   #makes health global to make accessable for functions
health = 100                                    #set health to 100
global delta                                    ##makes delta global to make accessable for functions
delta = 1                                       #set delta to 1
global tick30                                   #makes tick30 global to make accessable for functions
tick30 = 30                                     #set tick30 to 30
global playerX                                  #makes playerX global to make accessable for functions
playerX = 50                                    #set playerX to 50
global playerY                                  #makes playerY global to make accessable for functions
playerY = 50                                    #set playerY to 50
global playerAngle                              #makes playerAngle global to make accessable for functions
playerAngle = 90                                #set playerAngle to 90
# classes #                                     #
class PlayerClass(pg.sprite.Sprite):            #a class could be thought of data and functions 
    def __init__(self):                         #inside an object, and could be summoned/called 
        super().__init__()                      #multiple times w/o the ability to alter its 
        self.image = pg.Surface((10,10))        #creates an image of self
        self.image.fill('yellow')               #fills image with yellow
        self.rect = self.image.get_rect(        #creates a rectangle from the image
            center = (playerX,playerY))         #sets center to variables playerX and playerY
        self.mask = pg.mask.from_surface(       #creates a mask from surface
            self.image)                         #of image
    def update(self):                           #update function
        if pg.mouse.get_pos():                  #upon getting new position update from mouse
            self.rect.center = (playerX,playerY)#update the position of the player
class LevelClass(pg.sprite.Sprite):             #level class
    def __init__(self):                         #
        super().__init__()                      #
        self.image = pg.image.load(             #load image as
            'images/maze0.png').convert_alpha() #maze0.png from images folder in local
        self.rect = self.image.get_rect(        #creates a rectangle from the image
            center = (WIDTH/2,HEIGHT/2))        #sets center to middle of screen
        self.mask = pg.mask.from_surface(       #creates a mask from surface
            self.image)                         #of image
# groups #                                      #
playerGroup = pg.sprite.GroupSingle(            #creates a group from class for player
    PlayerClass())                              #
levelGroup = pg.sprite.GroupSingle(             #creates a group from class for level
    LevelClass())                               #
# functions #                                   #
'''
def playerMain():                               
    playerAngle = 90
    def Codefps(lasttick30):
        with timer() as t:
            global tick30
            tick30 = int(t.elapse)*30
            global delta
            delta = tick30-lasttick30
            global fps
            fps = int(30/delta)
    def Codeplayertick():
        def trymove(dx, dy):
            if pg.sprite.spritecollide(playerGroup.sprite,levelGroup,False):
                if pg.sprite.spritecollide(playerGroup.sprite,levelGroup,False,pg.sprite.collide_mask):
                    playerX += dx
                    playerY += dy
                    print(playerX, playerY)
                else:
                    playerX += dx
                    playerY += dy
                    print(playerX, playerY)
        def move(steps):
            trymove(steps*math.sin(math.radians(playerAngle+90)), 0)
            trymove(0, steps*math.cos(math.radians(playerAngle+90)))
            playerAngle = playerAngle
            turtle.listen()
        def up1():
            print('up1')
        def up2():
            print('up2')
        def down1():
            print('down1')
        def down2():
            print('down2')
        def left1():
            print('left1')
        def right1():
            print('right1')
        def left2():
            print('left2')
        def right2():
            print('right2')
        def space1():
            print('space1')
        def space2():
            print('space2')
    def Codeinitializeraycaster():
        global cameradir 
        cameradir = playerAngle
        global dv
        dv = 240/math.tan(fov/2)
        global drawdist
        drawdist = []
        global drawtype
        drawtype = []
        global drawx
        drawx = []
        drawdist.append([999999])
        drawtype.append([])
        drawx.append([])
        global drawidx
        drawidx = 1
    def Codedraw(type, x, distance):
        while drawdist[drawidx-1] > distance:
            drawidx -= 1
        while drawdist[drawidx] < distance:
            drawidx += 1
        drawtype.insert(drawidx-1, type)
        drawx.insert(drawidx-1, x)
        drawdist.insert(drawidx-1, distance)
    def Codesingleray():
        global position
        position = (playerX, playerY)
        global distance
        distance = 0
        while pg.sprite.spritecollide(playerGroup.sprite,levelGroup,False) != True:
            while pg.sprite.spritecollide(playerGroup.sprite,levelGroup,False,pg.sprite.collide_mask) != True:
                #move 4 steps
                steps = 4
                distance += 4
        while pg.sprite.spritecollide(playerGroup.sprite,levelGroup,False) != True:
            while pg.sprite.spritecollide(playerGroup.sprite,levelGroup,False,pg.sprite.collide_mask) != False:
                #move -1 steps 
                steps = -1
                distance -= 1
        distance = distance * math.cos(point-cameradir)
        if pg.sprite.spritecollide(playerGroup.sprite,colourGroup,False,pg.sprite.collide_mask):
            Codedraw(107, x, distance)
        else:
            Codedraw(108, x, distance)
    def Coderaycast():
        global x
        x = res/2-240
        if res < 4:
            x = int(x)
        global scanlines
        scanlines = 480/res
        global point
        for _ in range(int(scanlines)):
            point = cameradir + math.atan(x/dv)
            Codesingleray()
            x += res

    Codefps(tick30)
    Codeplayertick()
    Codeinitializeraycaster()
    Coderaycast()
'''
# main #
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    playerGroup = pg.sprite.GroupSingle(PlayerClass())
    levelGroup = pg.sprite.GroupSingle(LevelClass())
    playerGroup.update()
    levelGroup.update()
    playerGroup.draw(screen)
    levelGroup.draw(screen)
    '''
    playerMain()
    '''
    pg.display.update()
    clock.tick(60)