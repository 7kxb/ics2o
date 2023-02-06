# packages #
import pgzrun
import pygame
import turtle
import logging
import time         
import math
from timer import timer
import os

# initializing I #
WIDTH = 800
HEIGHT = 800
hwnd = pygame.display.get_wm_info()['window']
if os.name == 'nt':
    from ctypes import windll
    windll.user32.MoveWindow(hwnd,112,80,WIDTH,HEIGHT,False)

# classes #
class PlayerClass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/player1.png').convert_alpha()
        self.rect = self.image.get_rect(center = (4,4))
        self.mask = pygame.mask.from_surface(self.image)
class LevelClass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/maze0.png').convert_alpha()
        self.rect = self.image.get_rect(center = (480,360))
        self.mask = pygame.mask.from_surface(self.image)

# sprites #
playerSprite = Actor('player1', (WIDTH/2, HEIGHT/2)) 
levelSprite = Actor('maze0', (WIDTH/2, HEIGHT/2))
raycaster = Actor('raycaster0', (WIDTH/2, HEIGHT/2))
colour = Actor('maze1', (WIDTH/2, HEIGHT/2))
entities = Actor('entities0', (WIDTH/2, HEIGHT/2))
pen = Actor('pen1', (WIDTH/2, HEIGHT/2))
collectables = Actor('collectables0', (WIDTH/2, HEIGHT/2))

# variables #
fov = 120
res = 3
fog = 6
health = 100
delta = 1
tick30 = 30
playerSprite.x = 100
playerSprite.y = 100
playerSprite.image = 'player0.png'

# initializing II #
pygame.init()
playerGroup = pygame.sprite.GroupSingle(PlayerClass())
levelGroup = pygame.sprite.GroupSingle(LevelClass())
print('init')

# functions #
def playerMain():
    def Codefps(lasttick30):
        with timer() as t:
            tick30 = int(t.elapse)*30
            delta = tick30-lasttick30
            fps = int(30/delta)
    def Codeplayertick():
        def trymove(dx, dy):
            if pygame.sprite.spritecollide(playerGroup.sprite,levelGroup,False,pygame.sprite.collide_mask):
                playerSprite.x += dx
                playerSprite.y += dy
                playerGroup.sprite.image.fill('green')
            else:
                playerGroup.sprite.image.fill('red')
        def move(steps):
            playerSprite.image = 'player1'
            trymove(steps*math.sin(math.radians(playerSprite.angle+90)), 0)
            trymove(0, steps*math.cos(math.radians(playerSprite.angle+90)))
            playerSprite.image = 'player0'
            playerSprite.angle = playerSprite.angle
        if keyboard.a:
            if keyboard.s:
                playerSprite.angle -= 3 * delta
            else:
                playerSprite.angle += 3 * delta
        if keyboard.d:
            if keyboard.s:
                playerSprite.angle += 3 * delta
            else:
                playerSprite.angle -= 3 * delta
        if keyboard.w:
            move(1*delta)
        if keyboard.s:
            move(-1*delta)
    def Codeinitializeraycaster():
        cameradir = playerSprite.angle
        dv = 240/math.tan(fov/2)
        drawdist = []
        drawtype = []
        drawx = []
        drawdist.append([999999])
        drawtype.append([])
        drawx.append([])
        drawidx = 2
    Codefps(tick30)
    Codeplayertick()
    Codeinitializeraycaster()
    #raycast()
    #entitytick()
    #paint()
def draw():
    screen.clear()
    playerSprite.draw()
    levelSprite.draw()
def update():
    playerMain()

# main #
pgzrun.go()

