import pgzrun
from random import randint, choice, random
import string
f
WIDTH = 1600
HEIGHT = 900
inter = 0
Play = Actor('play')

def draw():
    Play.draw()
    if inter >= 1:
        screen.clear()


def on_mouse_down(pos):
    global inter
    if Play.collidepoint(pos):
        print("yes")
        inter += 1
        

    

pgzrun.go()