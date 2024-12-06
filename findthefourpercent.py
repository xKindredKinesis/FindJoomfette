# code is based on DVD Corner by Tomeczekqq, modified for the purposes of creating this video
# link to original repository: https://github.com/Tomeczekqq/dvd-corner
#
# you will need python3 and the pygame package installed in order to run this!
# python3 can be installed through the windows store, and usually already comes with most linux distros
# 
# after installing python3, to install pygame, open a terminal and enter the following:
# python3 -m pip install pygame
#
# to run the app, navigate to its directory in your terminal, and enter the following:
# python3 findthefourpercent.py

from random import randint
import pygame
from pygame import mixer

exit = False

# Settings
SIZE = width, height = 256*4, 192*4  # Resolution. (4:3)!
BG_COLOR = (0, 0, 0)  # Background color in RGB
JOOMFIE_AMOUNT = 96  # Amount of Joomfies that will appear (excludes Joomfette)
JOOMFIE_SCALE = 4  # Scale of Joomfie sprites
JOOMFIE_MIN_SPEED = 1  # Minimum speed a Joomfie can travel at
JOOMFIE_MAX_SPEED = 3  # Maximum speed a Joomfie can travel at
fullscreen = False  # Fullscreen

class Joomfie:
    def __init__(self, pygobj):
        self.size_x = pygobj.get_rect().size[0] * JOOMFIE_SCALE
        self.size_y = pygobj.get_rect().size[1] * JOOMFIE_SCALE
        self.pygobj = pygame.transform.scale(pygobj, (self.size_x, self.size_y))
        self.x = randint(self.size_x * -1, SIZE[0])
        self.y = randint(self.size_y * -1, SIZE[1])
        self.x_speed = ((randint(0, 1) * 2) - 1) * randint(JOOMFIE_MIN_SPEED, JOOMFIE_MAX_SPEED)
        self.y_speed = ((randint(0, 1) * 2) - 1) * randint(JOOMFIE_MIN_SPEED, JOOMFIE_MAX_SPEED)
        self.gender = 0

mixer.init()
mixer.music.load('wanted.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Find The Four Percent!')
if fullscreen:
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)

joomfies = []
joomfette_summoned = False
joomfies.append(Joomfie(pygame.image.load('joomfie5.png')))
joomfies[0].gender = 1

for ja in range(JOOMFIE_AMOUNT):
    index = randint(1, 4)
    joomfies.append(Joomfie(pygame.image.load('joomfie' + str(index) + '.png')))

def move(j, x, y):
    if j.gender == 0 or joomfette_summoned == True:
        screen.blit(j.pygobj, (x, y))

while exit == False:
    screen.fill(BG_COLOR)
    for js in joomfies:
        js.x += js.x_speed
        js.y += js.y_speed
        js.x = js.x % (width + js.size_x)
        js.y = js.y % (height + js.size_y)
        move(js, js.x-js.size_x, js.y-js.size_y)
    pygame.display.update()
    clock.tick(60)
    if pygame.time.get_ticks() % 1200 == 0 and joomfette_summoned == False:
        print("Joomfette summoned")
        joomfette_summoned = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

pygame.quit()