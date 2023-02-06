# packages #
import pgzrun
import pygame
import turtle
import sys
import os
import math
from timer import timer

# initializing #
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
os.environ['SDL_VIDEO_WINDOW_POS'] = "112,80"
screen1 = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
print('init')

# variables #
fov = 120
res = 3
fog = 6
health = 100
delta = 1
tick30 = 30
playerX = 100
playerY = 100

# classes #
class PlayerClass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(center = (100,100))
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        if pygame.mouse.get_pos():
            self.rect.center = (playerX,playerY)
class LevelClass(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/maze0.png').convert_alpha()
        self.rect = self.image.get_rect(center = (400,400))
        self.mask = pygame.mask.from_surface(self.image)

# groups #
playerGroup = pygame.sprite.GroupSingle(PlayerClass())
levelGroup = pygame.sprite.GroupSingle(LevelClass())

# functions #
def playerMain():
    playerAngle = 90
    def Codefps(lasttick30):
        with timer() as t:
            tick30 = int(t.elapse)*30
            delta = tick30-lasttick30
            fps = int(30/delta)
    def Codeplayertick():
        def trymove(dx, dy):
            if pygame.sprite.spritecollide(playerGroup.sprite,levelGroup,False):
                if pygame.sprite.spritecollide(playerGroup.sprite,levelGroup,False,pygame.sprite.collide_mask):
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
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord('a'):
                    if event.key == ord('s'):
                        playerAngle -= 3 * delta
                    else:
                        playerAngle += 3 * delta
                if event.key == ord('d'):
                    if event.key == ord('s'):
                        playerAngle += 3 * delta
                    else:
                        playerAngle -= 3 * delta
                if event.key == ord('w'):
                    move(1*delta)
                if event.key == ord('s'):
                    move(-1*delta)
    def Codeinitializeraycaster():
        cameradir = playerAngle
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

# main #
pgzrun.go()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    playerGroup.update()
    levelGroup.update()
    playerGroup.draw(screen)
    levelGroup.draw(screen)
    playerMain()
    pygame.display.update()
    clock.tick(60)