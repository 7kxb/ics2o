# packages #
import pgzrun
import pygame
import sys
import turtle
from timer import timer
import math
import os

# classes #
class PlayerClass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10,10)) 
        self.image.fill('yellow')
        self.rect = self.image.get_rect(center = (100,100))
        self.mask = pygame.mask.from_surface(self.image)
class LevelClass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/maze0.png').convert_alpha()
        self.rect = self.image.get_rect(center = (400,400))
        self.mask = pygame.mask.from_surface(self.image)

# initializing #
os.environ['SDL_VIDEO_WINDOW_POS'] = "112,80"
pygame.init()
WIDTH = 800
HEIGHT = 800
if os.name == 'nt' or sys.platform == 'win32':
    from ctypes import windll
    hwnd = pygame.display.get_wm_info()['window']
    windll.user32.MoveWindow(hwnd,112,80,WIDTH,HEIGHT,False)
elif os.name == 'posix' and sys.platform == 'linux' and pygame.display.get_driver() == 'x11':
    import Xlib.display
    xid = pygame.display.get_wm_info()['window']
    disp = Xlib.display.Display()
    xwin = disp.create_resource_object('window', xid)
    xwin.configure(x=112, y=80, width=WIDTH, height=HEIGHT)
clock = pygame.time.Clock()
playerGroup = pygame.sprite.GroupSingle(PlayerClass())
levelGroup = pygame.sprite.GroupSingle(LevelClass())
print('init')

# actors #
playerSprite = Actor('player0', (WIDTH/2, HEIGHT/2))
levelSprite = Actor('maze0', (WIDTH/2, HEIGHT/2))

# variables #
fov = 120
res = 3
fog = 6
health = 100
delta = 1
tick30 = 30
playerSprite.x = 100
playerSprite.y = 100

# functions #
def playerMain():
    def Codefps(lasttick30):
        with timer() as t:
            tick30 = int(t.elapse)*30
            delta = tick30-lasttick30
            fps = int(30/delta)
    def Codeplayertick():
        def trymove(dx, dy):
            if pygame.sprite.spritecollide(playerGroup.sprite,levelGroup,False):
                if pygame.sprite.spritecollide(playerGroup.sprite,levelGroup,False,pygame.sprite.collide_mask):
                    temp = []
                else:
                    playerSprite.x += dx
                    playerSprite.y += dy
                    playerGroup.x += dx
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