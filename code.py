import pgzrun
from random import randint, choice
import string
from vocabulary import *
WIDTH = 800
HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# LETTER = {"letter": "", "x": 0, "y": 0}
ON_SCREEN_LETTERS = []
VELOCITY = 1
SCORE = {"RIGHT": 0, "WRONG": 0}
inter = 0
stop = 0
pu2 = 0
toyo = Actor('play')
pu = Actor('pause')
back = Actor('backg')
endgame = Actor('end')
replaygame = Actor('replay')
resumegame = Actor('resume')
keyin = ''
mm = ''

def draw():
    toyo.draw()
    if 
    screen.clear()
    screen.fill(BLACK)
    for LETTER in ON_SCREEN_LETTERS:
        screen.draw.text(LETTER["letter"], (LETTER["x"], LETTER["y"]), fontsize=50, color=WHITE)
    screen.draw.text("RIGHT: " + str(SCORE["RIGHT"]), (WIDTH - 130, 10), fontsize=30, color=WHITE)
    screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 130, 40), fontsize=30, color=WHITE)
    screen.draw.text("TEXT: " + str(keyin), (200, HEIGHT - 50), fontsize=30, color=WHITE)

def on_mouse_down(pos):
    toyo.c

def update():
    for i, LETTER in enumerate(ON_SCREEN_LETTERS):
        LETTER["y"] += VELOCITY
        if LETTER["y"] == HEIGHT - 5:
            SCORE["WRONG"] += 1
            delete_letter(i)
    while len(ON_SCREEN_LETTERS) < 1:
        add_letter()

def on_key_down(key, mod, unicode):
    global keyin
    if keyboard.BACKSPACE:
        keyin = keyin[:-1]
    else:
        keyin += unicode

    
    for i,LETTER in enumerate(ON_SCREEN_LETTERS):
        if LETTER["letter"] == keyin:
            SCORE["RIGHT"] += 1
            delete_letter(i)
            keyin = ''
            return

        

def add_letter():
    letter = choice(vocabulary2)
    x = randint(10, WIDTH - 100)
    y = 1
    ON_SCREEN_LETTERS.append({"letter": letter, "x": x, "y": y})

def delete_letter(i):
    del ON_SCREEN_LETTERS[i]
pgzrun.go()